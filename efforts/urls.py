from django.urls import path, include
from rest_framework.routers import DefaultRouter
from efforts import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'customers', views.CustomerViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'efforts', views.EffortViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
