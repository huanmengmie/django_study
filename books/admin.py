from django.contrib import admin

# Register your models here.
from books.models import BookInfo, HeroInfo


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "author", "price"]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "gender", "skill", "book_id"]


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
