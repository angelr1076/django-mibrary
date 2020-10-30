from django.contrib import admin
from .models import Book, Review, Profile


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Book, BookAdmin)
admin.site.register(Review)
admin.site.register(Profile)
