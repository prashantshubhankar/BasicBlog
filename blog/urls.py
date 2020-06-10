from django.urls import path
from blog import views
from blog.views import (AboutView, PostListView,
                        PostDetailView, CreatePostView,
                        PostUpdateView, PostDeleteView,
                        DraftListView)

urlpatterns = [

    path('', PostListView.as_view(), name='post_list'),
    path('about/', AboutView.as_view(), name='about'),
    path('post/<str:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', CreatePostView.as_view(), name='post_new'),
    path('post/<str:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<str:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('drafts/', DraftListView.as_view(), name='draft_list'),
    path('post/<str:pk>/comment/', views.add_comment_to_post, name='add_comment'),
    path('comment/<str:pk>/aprrove/', views.comment_approve, name='comment_approve'),
    path('comment/<str:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('post/<str:pk>/publish/', views.post_publish, name='post_publish'),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    
]
