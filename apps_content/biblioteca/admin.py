from django.contrib import admin
from apps_content.biblioteca.models import Store, University, Book, Author, Publisher, Student, Loan


class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'direction', 'post_books']
    list_filter = ('name', 'direction')
    search_fields = ('name', 'direction',)
    readonly_fields = ('created', 'modified')
    date_hierarchy = 'created'

    def post_books(self, obj):
        return ", ".join([c.name for c in obj.books.all().order_by("name")])
    post_books.short_description = "Books"


admin.site.register(Store, StoreAdmin)
admin.site.register(University)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Student)
admin.site.register(Loan)
