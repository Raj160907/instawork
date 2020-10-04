from django.conf.urls import include, url
from rest_framework import routers
from django.urls import path

from .views import UserView, UserDeleteView
router = routers.DefaultRouter()

urlpatterns = [
    url('^user/$', UserView.as_view(), name='user'),
    path(r'user_delete/<int:user_id>/', UserDeleteView.as_view(), name='user-delete'),
]

urlpatterns += router.urls
