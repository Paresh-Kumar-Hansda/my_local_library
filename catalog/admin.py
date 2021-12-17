from django.contrib import admin

# Register your models here.
from .models import Language, Author, Genre, Book, BookInstance

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
#admin.site.register(BookInstance)

# Define the admin class
#class AuthorAdmin(admin.ModelAdmin):
 #   pass

# Register the admin class with the associated model
#admin.site.register(Author, AuthorAdmin)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
admin.site.register(Author, AuthorAdmin)
# Register the Admin classes for Book using the decorator
#@admin.register(Book)
#class BookAdmin(admin.ModelAdmin):
 #   pass
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'display_language')
    inlines = [BooksInstanceInline]
#admin.site.register(Book, BookAdmin)
# Register the Admin classes for BookInstance using the decorator
#@admin.register(BookInstance)
#class BookInstanceAdmin(admin.ModelAdmin):
 #   pass
#class BookInstanceAdmin(admin.ModelAdmin):
 #   list_filter = ('status', 'due_back')

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display =("book","status",'borrower',"due_back","id",)
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )

