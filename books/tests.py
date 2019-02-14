import datetime

from django.test import TestCase

# Create your tests here.
from books.models import BookInfo


def book_info_test():
    b = BookInfo()
    b.name = "三体"
    b.author = "刘慈欣"
    b.price = 80
    b.pub_date = datetime.datetime()

    b.save()

    a = BookInfo.objects.get(id=1)
    print(a)

    a.price = 50
    a.save()

    a2 = BookInfo.objects.get(id=1)
    print(a2)


if __name__ == '__main__':
    book_info_test()
