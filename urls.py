from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('create_post', views.create_post, name='create_post'),
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
    path('create_comment', views.create_comment, name='create_comment'),
    path('edit_comment/<int:comment_id>', views.edit_comment, name='edit_comment'),
    path('delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment'),
]
