from django.urls import path
from . import views
from rest_framework_simplejwt.views import(TokenObtainPairView, TokenRefreshView) 
app_name='administrativo'

urlpatterns = [
    path('empresas/', views.EmpresaList.as_view(), name='empresas-list'),
    path('empresas/<int:pk>/', views.EmpresaDetail.as_view(), name='empresas-detail'),
    path('obras/', views.ObraList.as_view(), name='obras-list'),
    path('obras/<int:pk>/', views.ObraDetail.as_view(), name='obras-detail'),
    path('cpgroups/', views.CPGroupList.as_view(), name='cpgroups-list'),
    path('cpgroups/<int:pk>/', views.CPGroupDetail.as_view(), name='cpgroups-detail'),
    path('cps/', views.CPList.as_view(), name='cps-list'),
    path('cps/<int:pk>/', views.CPDetail.as_view(), name='cps-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create/', views.create_user, name='create_user')
]
