from django.urls import path
from . import views

urlpatterns = [   
    path('payment/', views.PaymentList.as_view()),
    path('payment/<int:pk>', views.PaymentDetail.as_view()),
]