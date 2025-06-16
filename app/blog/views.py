from rest_framework import generics, permissions, pagination
from blog.models import Post
from blog.serializers import PostSerializer
from rest_framework.exceptions import PermissionDenied


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Post.objects.all().order_by('-fecha_creacion')

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Post.objects.all()

    def perform_update(self, serializer):
        if serializer.instance.autor != self.request.user:
            raise PermissionDenied("No tienes permiso para editar este post")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.autor != self.request.user:
            raise PermissionDenied("No tienes permiso para eliminar este post")
        instance.delete()
