from django.contrib import admin
from collection.models import Book


# Makes a nice slug
class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('book_name', 'author', 'description', 'pub_date', 'image')
    prepopulated_fields = {'slug': ('book_name',)}

admin.site.register(Book, BookAdmin)




