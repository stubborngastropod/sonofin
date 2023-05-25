from django.urls import path
from . import views

app_name="boards"
urlpatterns = [
    path('', views.index, name="index"),
    path('comments/', views.comment_index, name="comment_index"),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'), 
    path('<int:pk>/edit/', views.detail_edit, name='detail_edit'), 
    # path('<int:pk>/update/', views.update, name='update'),   
    # path('<int:pk>/delete/', views.delete, name='delete'),   
    path('<int:board_pk>/comment/', views.comment, name='comment'),
    path('<int:board_pk>/comment/<int:comment_pk>/', views.comment_edit, name='comment_edit'),
    path('<int:board_pk>/likes/', views.likes, name='likes'),
]
