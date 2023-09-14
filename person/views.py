from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse
from .models import Person
from .serializers import PersonSerializer


class CreatePersonView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def perform_create(self, serializer):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK, headers={'Location': reverse('person-detail', args=[serializer.instance.pk])})

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class PersonByNameView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'name__iexact'

    def get_object(self):
        lookup_value = self.kwargs[self.lookup_field]
        try:
            return self.queryset.get(**{self.lookup_field: lookup_value})
        except Person.DoesNotExist:
            raise Http404("Person does not exist")

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK, headers={'Location': reverse('person-detail', args=[serializer.instance.pk])})

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
