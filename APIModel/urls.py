from cryptography.x509 import name
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from APIModel import views

urlpatterns = [
    path('ui_list/', views.UIList.as_view(), name='ui_list'),
    path('ui_detail/<int:pk>/', views.UIDetail.as_view(), name='ui_detail'),
    # path('ai_list/', views.AIList.as_view(), name='ai_list'),
    # path('ai_detail/<int:pk>/', views.AIDetail.as_view(), name='ai_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
