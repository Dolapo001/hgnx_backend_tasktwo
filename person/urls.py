from django.urls import path
from .views import CreatePersonView, PersonDetailView

urlpatterns = [
    path('', CreatePersonView.as_view(), name='create-person'),
    path('<str:pk>', PersonDetailView.as_view(), name='person-detail-by-id'),
]
