#define URL route for index() view
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter(trailing_slash=False)
router.register(r'table', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/items', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
    path('booking/', include(router.urls)),
]