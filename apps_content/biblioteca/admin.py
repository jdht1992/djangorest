from django.contrib import admin
from apps_content.biblioteca.models import Store, University, Book, Author, Publisher, Student, Loan
#from django.utils.safestring import mark_safe
from django.utils.html import mark_safe

class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'direction', 'post_books')
    list_filter = ('name', 'direction')
    search_fields = ('name', 'direction',)
    readonly_fields = ('created', 'modified')
    date_hierarchy = 'created'
    ordering = ('created',)

    def post_books(self, obj):
        return ", ".join([book.name for book in obj.books.all().order_by("name")])
    post_books.short_description = "Books"


admin.site.register(Store, StoreAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'university', 'marital_status', 'gender', 'address', 'telephone_number', 'additional_data', 'birthday', 'image')
    list_filter = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    readonly_fields = ('created', 'modified', 'student_image',)
    date_hierarchy = 'created'
    ordering = ('created',)


    def student_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
        )
    )


admin.site.register(Student, StudentAdmin)
admin.site.register(University)


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'book_code', 'pages', 'gender', 'created_by')


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Loan)
