from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ViewSet


class ParentViewSet(ViewSet):
    """视图集"""

    def list(self, request):
        qs =

