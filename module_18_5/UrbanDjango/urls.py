from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from task5 import views

urlpatterns = [
    path('', views.sign_up_by_django),
    path('x/', views.sign_up_by_html),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)