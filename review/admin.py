from django.contrib import admin
from .models import Like, FavouriteDriver, FavouriteLocation, Rating, Comment


admin.site.register(Like)
admin.site.register(FavouriteDriver)
admin.site.register(FavouriteLocation)
admin.site.register(Rating)
admin.site.register(Comment)
