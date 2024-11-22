from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_form, name='customer_form'),  # Root path will show the form
    path('thank-you/', views.thank_you, name='thank_you'),
]
