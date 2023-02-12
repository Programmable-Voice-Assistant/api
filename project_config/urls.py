from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('scripts/', include('scripts.urls')),
    path('rest-framework-accounts/', include('rest_framework.urls')),

]
