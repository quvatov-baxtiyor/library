from django.contrib import admin

from .models import Book,User,Review

admin.site.register([Book,User,Review])


#admin panel code:
# Username: library,  Password: 2024