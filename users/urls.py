from django.urls import path
from rest_framework.routers import DefaultRouter
from . import apis as views

router = DefaultRouter()
urlpatterns = router.urls

urlpatterns += [
    path("create/user", views.CreateUserView.as_view())
]
