from rest_framework import mixins, viewsets

class BaseListCreateViewSet(mixins.ListModelMixin,
                            mixins.CreateModelMixinm
                            viewsets.GenericViewSet):
    """Базовый класс для методов list и create"""
    pass