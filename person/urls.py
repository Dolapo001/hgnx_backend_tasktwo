from django.urls import path
from . import views

urlpatterns = [
    path('api/<int:pk>/', views.PersonDetailView.as_view(), name='person-detail'),
    path('api/<str:name__iexact>/', views.PersonByNameView.as_view(), name='person-by-name'),
    path('api/', views.CreatePersonView.as_view(), name='create-person'),
]
