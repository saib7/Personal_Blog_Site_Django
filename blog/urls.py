from django.urls import path

from . import views

urlpatterns = [
    path(route="", view=views.StartingPageView.as_view(), name="starting-page"),
    path(route="posts", view=views.AllPostsView.as_view(), name="posts-page"),
    path(route="posts/<slug:slug>", view=views.SinglePostView.as_view(),
         name="post-detail-page"),  # /posts/my-first-post
    path("read-later", view=views.ReadLaterView.as_view(), name="read-later")
]
