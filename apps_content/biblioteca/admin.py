from django.contrib import admin
from apps_content.biblioteca.models import Store, University, Book, Author, Publisher, Student, Loan
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


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'salutation', 'email')
    list_filter = ('name', 'email')
    search_fields = ('name', 'email',)
    readonly_fields = ('created', 'modified')
    date_hierarchy = 'created'
    ordering = ('created',)


admin.site.register(Author, AuthorAdmin)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'city', 'state_province', 'country', 'website')
    list_filter = ('name',)
    search_fields = ('name', 'address',)
    readonly_fields = ('created', 'modified')
    date_hierarchy = 'created'
    ordering = ('created',)


admin.site.register(Publisher, PublisherAdmin)


class LoanAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_number', 'post_books', 'student', 'date_s', 'date_e', 'date_d')
    list_filter = ('order_number',)
    search_fields = ('order_number', 'stident')
    readonly_fields = ('created', 'modified')
    date_hierarchy = 'created'
    ordering = ('created',)

    def post_books(self, obj):
        return ", ".join([book.name for book in obj.book.all().order_by("name")])
    post_books.short_description = "Books"


admin.site.register(Loan, LoanAdmin)
