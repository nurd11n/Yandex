from django.db import models
from django.contrib.auth import get_user_model
from account.models import DriverProfile
from map.models import Locations


User = get_user_model()


class Comment(models.Model):
    body = models.TextField()
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    driver = models.ForeignKey(DriverProfile, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    driver = models.ForeignKey(DriverProfile, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.name} liked {self.ticket.title}'


class Rating(models.Model):
    rating = models.PositiveSmallIntegerField()
    driver = models.ForeignKey(DriverProfile, on_delete=models.CASCADE, related_name='ratings')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')

    def __str__(self):
        return f'{self.rating} - {self.ticket}'


class FavouriteDriver(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourites')
    driver = models.ForeignKey(DriverProfile, on_delete=models.CASCADE, related_name='favourites')

    def __str__(self):
        return f'{self.author} {self.ticket}'


class FavouriteLocation(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourite_location')
    location = models.ForeignKey(Locations, on_delete=models.CASCADE, related_name='favourite_location')

    def __str__(self):
        return f'{self.author} {self.ticket}'


