import logging
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from review.models import Comment, Rating, FavouriteDriver, FavouriteLocation
from review.serializers import CommentSerializer, RatingSerializer, FavouritesSerializer, FavouriteLocationSerializer

logger = logging.getLogger(__name__)


def my_view(request):
    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')
    logger.error('Error message')
    logger.critical('Critical message')


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]


class FavouriteViewSet(ModelViewSet):
    queryset = FavouriteDriver.objects.all()
    serializer_class = FavouritesSerializer
    permission_classes = [IsAuthenticated]


class FavouriteLocationsViewSet(ModelViewSet):
    queryset = FavouriteLocation.objects.all()
    serializer_class = FavouriteLocationSerializer
    permission_classes = [IsAuthenticated]