from django.conf.urls import url

from .views import (
    UserCreateAPIView,
    UserUpdateAPIView,
    UserListAPIView
)

urlpatterns = [

    url(r'^$',UserListAPIView.as_view(),name='List'),
    url(r'^create/$',UserCreateAPIView.as_view(),name='create'),
    url(r'^update/$',UserUpdateAPIView.as_view(),name='edit'),

    
]