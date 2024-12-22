from django.contrib import admin
from .models import genre, movies

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

class MovieAdmin(admin.ModelAdmin):
   # list_display = ('title', 'release_year', 'number_in_stock', 'daily_rate', 'genre', )
    exclude = ('date_created',)
    list_display = ('title', 'release_year', 'number_in_stock', 'daily_rate', 'genre')
    


admin.site.register(genre, GenreAdmin)
admin.site.register(movies, MovieAdmin)

