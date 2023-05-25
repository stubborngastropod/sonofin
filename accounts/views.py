from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.views.decorators.http import require_POST, require_safe, require_http_methods
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http.response import JsonResponse
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from dj_rest_auth.serializers import UserDetailsSerializer

from .models import User

User = get_user_model()
class UserDetailView(APIView):
    def get(self, request):
        serializer = UserDetailsSerializer(request.user)
        return Response(serializer.data)



















# Create your views here.
# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             auth_login(request, form.get_user())
#             return redirect('home:home')
#     else:
#         form = AuthenticationForm()
        
#     context = {'form': form}
#     return render(request, 'accounts/login.html', context)

# def logout(request):
#     auth_logout(request)
#     return redirect('home:home')

# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect('boards:index')
#     else:
#         form = CustomUserCreationForm()
        
#     context = {'form': form}
#     return render(request, 'accounts/signup.html', context)

# def profile(request, username):
#     User = get_user_model()
#     person = User.objects.get(username=username)
#     context = {
#         'person': person
#     }
#     return render(request, 'accounts/profile.html', context)

# def follow(request, user_pk):
#     if request.method == 'POST':
#         pass

# @require_POST
# def follow(request, user_pk):
#     if request.user.is_authenticated:
#         User = get_user_model()
#         person = User.objects.get(pk=user_pk)
#         if person != request.user:
#             if person.followers.filter(pk=request.user.pk).exists():
#                 person.followers.remove(request.user)
#             else:
#                 person.followers.add(request.user)
#         return redirect('accounts:profile', person.username)
#     return redirect('accounts:login')