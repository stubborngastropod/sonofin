from django.urls import path
from accounts.views import UserDetailView


app_name = 'accounts'
urlpatterns = [
    path('/user/', UserDetailView.as_view(), name='user_detail'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    # path('signup/', views.signup, name='signup'),
    # path('profile/<username>/', views.profile, name='profile'),
    # path('<int:user_pk>/follow/', views.follow, name='follow'),

]
