from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from task4 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('second/', views.second_page),
    path('third/', views.third_page),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
