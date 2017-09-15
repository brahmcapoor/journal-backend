from django.contrib.auth.models import User as Author
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Post
from .serializers import PostSerializer, PostDateSerializer, AuthorSerializer
from .permissions import IsOwnerOrReadOnly

@api_view(['GET'])
@permission_classes((IsOwnerOrReadOnly,))
def api_root(request, format=None):
    return Response({
        'authors': reverse('author-list', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format)
    })


class PostDateList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDateSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Automatically provides list and details
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


