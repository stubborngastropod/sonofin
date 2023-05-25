from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Board, Comment
from .forms import BoardForm, CommentForm
from django.views.decorators.http import require_http_methods
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import BoardListSerializer, BoardSerializer, CommentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


# Create your views here.
# @require_http_methods(["GET"])
@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        boards = get_list_or_404(Board)
        serializer = BoardListSerializer(boards, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def comment_index(request): #댓글목록 가져오기 
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    
  

# @require_http_methods(["GET", "POST"])
@api_view(['GET'])

def detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    
    if request.method == 'GET':
        serializer = BoardListSerializer(board)
        # print(serializer.data)
        return Response(serializer.data)

@api_view(['DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def detail_edit(request, pk):
    board = get_object_or_404(Board, pk=pk)

    # 게시글 작성자와 요청한 사용자가 일치하는지 확인
    if board.author != request.user:
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    else:
        if request.method == 'DELETE':
            board.delete()
            data = {
                f'{pk}번 리뷰가 삭제되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)

        elif request.method == 'PUT':
            serializer = BoardListSerializer(board, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    return Response({'detail': '잘못된 요청입니다.'}, status=status.HTTP_400_BAD_REQUEST)



    # comments = board.comments.all()
    # comment_form = CommentForm()
    
    # context = {
    #     'board': board,
    #     'comments': comments,
    #     'comment_form': comment_form,
    # }
    # return render(request, 'boards/detail.html', context)

@require_http_methods(["GET", "POST"])
def update(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm(instance=board)
    context = {
        'board': board,
        'form': form,
    }        
    return render(request, 'boards/update.html', context)


# @api_view(['POST'])
# def create(request):
#     if request.method == 'POST':
#         serializer = BoardSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             # serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        


# @api_view(['POST'])
# def create(request):
#     serializer = BoardListSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save(author=request.user)  # 현재 로그인된 사용자를 작성자로 저장
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    if request.method == 'POST':
        serializer = BoardListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # if request.method == 'POST':
    #     form = BoardForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         board = form.save(commit=False)
    #         board.author = request.user
    #         board.save()
    #         return redirect('boards:index')
    # else:
    #     form = BoardForm()
    # context = {
    #     'form': form,
    # }
    # return render(request, 'boards/create.html', context)

# @require_http_methods(["POST"])
# def comment(request, board_pk):
#     board = get_object_or_404(Board, pk=board_pk)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.board = board
#             comment.save()
#             return redirect('boards:detail', board.pk)
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def comment(request, board_pk):
#     board = get_object_or_404(Board, pk=board_pk)
#     serializer = CommentSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(board=board, comment_author=request.user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def comment(request, board_pk):
#     board = get_object_or_404(Board, pk=board_pk)
#     serializer = CommentSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(board=board, comment_author=request.user)  # 저장 시 작성자 정보 추가
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(author=request.user, board=board)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_edit(request, board_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk, board=board_pk)
    if comment.author != request.user:
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    else:
        if request.method == 'DELETE':
            comment.delete()
            data = {
                f'{comment_pk}번 리뷰가 삭제되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'PUT':
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    return Response({'detail': '잘못된 요청입니다.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# @require_http_methods(["POST"])
# def comment_detail(request, board_pk, comment_pk):
#     comment = get_object_or_404(Comment, pk=comment_pk)
#     if request.method == 'POST':
#         comment.delete()
#         return redirect('boards:detail', board_pk)

@require_http_methods(["POST"])
def likes(request, board_pk):
    if request.user.is_authenticated:
        board = Board.objects.get(pk=board_pk)
        if board.like_users.filter(pk=request.user.pk).exists():
            board.like_users.remove(request.user)
        else:
            board.like_users.add(request.user)
        return redirect('boards:index')
    return redirect('accounts:login')