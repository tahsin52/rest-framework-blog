from django.urls import path, include

from comment.api.views import CommentUpdateAPIView, CommentDeleteAPIView, CommentCreateAPIView, CommentListAPIView

app_name = "comment"

urlpatterns = [
    path('create', CommentCreateAPIView.as_view(), name='create'),
    path('list', CommentListAPIView.as_view(), name='list'),
    path('delete/<pk>', CommentDeleteAPIView.as_view(), name='delete'),
    path('update/<pk>', CommentUpdateAPIView.as_view(), name='update'),

]
