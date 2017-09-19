from django.contrib.auth.models import User as Author
from rest_framework import generics, permissions, viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authtoken.models import Token
from .models import Post
from .serializers import PostSerializer, PostDateSerializer, AuthorSerializer
from .permissions import IsOwnerOrReadOnly, IsAdminOrTargetUser

@api_view(['GET'])
@permission_classes((IsOwnerOrReadOnly,))
def api_root(request, format=None):
    return Response({
        'authors': reverse('author-list', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format)
    })


class PostDateList(generics.ListAPIView):
    """
    get:
        Return all post dates.
    """
    queryset = Post.objects.all()
    serializer_class = PostDateSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a post instance.

    list:
        Return all posts, ordered by post id.

    create:
        Create a new post.

    delete:
        Remove an existing post.

    partial_update:
        Update one or more fields on an existing post.

    update:
        Update a post.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class AuthorViewSet(viewsets.ModelViewSet):
    """
    create:
        Create an author instance

    retrieve:
        Return an author instance.

    list:
        Return all authors, ordered by author id.

    delete:
        Remove an existing author.

    partial_update:
        Update one or more fields on an existing author.

    update:
        Update an author.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user = serializer.instance)
        return Response({'token': token.key}, status = status.HTTP_201_CREATED,
                        headers = headers)


    def get_permissions(self):
        return (permissions.AllowAny() if self.request.method == 'POST'
                else IsAdminOrTargetUser()),

