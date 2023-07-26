from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('comment/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/',views.CommentDestroyView.as_view(), name='cpmment_delete'),
    path('user/<int:pk>/', views.UserDeleteView.as_view(), name='user_delete'),
    path('users/', views.UserListView.as_view(), name='users_list'),

]