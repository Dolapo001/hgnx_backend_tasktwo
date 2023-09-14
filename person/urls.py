from django.urls import path
from .views import CreatePersonView, PersonDetailView, PersonByNameView

urlpatterns = [
    path('api/', CreatePersonView.as_view(), name='create-person'),
    path('api/<str:pk>/', PersonDetailView.as_view(), name='person-detail'),
    path('api/<str:name__iexact>', PersonByNameView.as_view(), name='person-by-name'),
]
