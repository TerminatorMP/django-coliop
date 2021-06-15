from django.urls import path

from . import views

urlpatterns = [
    path('getJobId', views.GetJobId.as_view(), name='GetJobId'),
    path('getMessages', views.GetMessages.as_view(), name='getMessages'),
    path('checkForSolution', views.CheckForSolution.as_view(), name='checkForSolution'),
    path('getSolution', views.GetSolution.as_view(), name='getSolution'),
    path('sendXML', views.SendXML.as_view(), name='sendXML'),
]