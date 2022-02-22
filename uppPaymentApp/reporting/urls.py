from django.urls import path
from . import views

urlpatterns = [   
    path('reporting/', views.ReportingList.as_view()),
    path('reporting/<int:pk>', views.ReportingDetail.as_view()),
]