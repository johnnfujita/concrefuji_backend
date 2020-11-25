
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('administrativo/', include('cp.urls', namespace='administrativo')),
]
