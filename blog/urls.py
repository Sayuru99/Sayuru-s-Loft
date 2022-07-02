from . import views
from django.urls import path, url
from blog.views import about

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    url(r'^/about/$', about.as_view()),
]