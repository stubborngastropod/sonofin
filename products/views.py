from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import DepositOptions, DepositProducts
from .serializers import DepositOptionsSerializer, DepositProductsSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.

BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def save_deposit_products(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': settings.PRODUCTS_API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1,
    }
    response = requests.get(URL, params=params).json()
    serializer = DepositProductsSerializer(data=response['result']['baseList'], many=True)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return JsonResponse({ 'status': 'success' })
    else:
        return JsonResponse({ 'status': 'fail', 'message': serializer.errors })

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def save_deposit_options(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': settings.PRODUCTS_API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1,
    }
    try:
        response = requests.get(URL, params=params).json()
        data = response['result']['optionList']  # 응답 데이터에서 optionList 가져오기
    except Exception as e:
        return JsonResponse({'status': 'fail', 'message': str(e)})  # 응답을 정상적으로 받지 못한 경우 에러 메시지 반환

    if data:  # 응답 데이터가 존재할 경우에만 직렬화 및 저장
        serializer = DepositOptionsSerializer(data=data, many=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'fail', 'message': serializer.errors})

@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        deposits = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(deposits, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse({ 'status': 'success'})
        else:
            return JsonResponse({ 'status': 'fail', 'message': serializer.errors })

@api_view(['GET', 'POST'])
def deposit_options(request):
    if request.method == 'GET':
        options = DepositOptions.objects.all()
        serializer = DepositOptionsSerializer(options, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DepositOptionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def deposit_products_detail(request, pk):
    product = get_object_or_404(DepositProducts, pk=pk)
    if request.method == 'GET':
        serializer = DepositProductsSerializer(product)
        return Response(serializer.data)




@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    deposit = DepositOptions.objects.get(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(deposit)
    return JsonResponse(serializer.data)

@api_view(['GET'])
def top_rate(request):
    deposit = DepositOptions.objects.order_by('-intr_rate').first()
    serializer = DepositOptionsSerializer(deposit)
    return JsonResponse(serializer.data)

# 상품 가입
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def subscription(request, product_pk):
    try:
        product = DepositProducts.objects.get(pk=product_pk)
    except DepositProducts.DoesNotExist:
        return Response({'error': '상품을 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)
    
    if product.customers.filter(pk=request.user.pk).exists():
        product.customers.remove(request.user)
        return Response({'message': '상품을 즐겨찾기에서 삭제했습니다.'}, status=status.HTTP_200_OK)
    else:
        product.customers.add(request.user)
        return Response({'message': '상품을 즐겨찾기에 추가했습니다.'}, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def subscribed_products(request):
    if request.method == 'GET':
        user = request.user  # 현재 인증된 사용자
        subscribed_products = user.subscriped_products.all()  # 현재 사용자가 구독한 상품들

        serializer = DepositProductsSerializer(subscribed_products, many=True)
        return Response(serializer.data)
