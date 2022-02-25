from rest_framework.routers import DefaultRouter
from django.urls import path, include

from users import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user-list')
router.register(r'login', views.LoginView, basename='login')
router.register(r'events', views.EventViewSet, basename='event-list')
router.register(r'tickets', views.TicketViewSet, basename='ticket-list')

urlpatterns = [
    path('', include(router.urls)),
    path('account/logout/', views.LogoutView.as_view(), name='logout')
]