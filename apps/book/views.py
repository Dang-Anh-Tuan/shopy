from rest_framework import viewsets
from rest_framework.response import Response
from .models import Book, Publisher, Category, Author
from .serializers import PublisherSerializer, CategorySerializer, AuthorSerializer, BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        list_book = Book.objects.all()
        return list_book

    def create(self, request, *args, **kwargs):
        data = request.data
        new_book = None
        author_id = data['author']['id']
        publisher_id = data['publisher']['id']
        category_id = data['category']['id']

        if author_id != None and publisher_id != None and category_id != None:
            book_author = Book.objects.get(id=data['author']['id'])
            book_publisher = Book.objects.get(id=data['publisher']['id'])
            book_category = Book.objects.get(id=data['category']['id'])
            new_book = Book.objects.create(
                title=data['title'], summary=data['summary'], numOfPages=data['num'], language=data['language'], publisher=book_publisher, author=book_author, category=book_category)

        else:
            if author_id == None:
                author_name = data['author']['name']
                author_country = data['author']['country']
                book_author = Author.objects.create(name=author_name, country=author_country)
                book_publisher = Book.objects.get(id=data['publisher']['id'])
                book_category = Book.objects.get(id=data['category']['id'])
                book_author.save()
                new_book = Book.objects.create(
                    title=data['title'], summary=data['summary'], numOfPages=data['num'], language=data['language'], publisher=book_publisher, author=book_author, category=book_category)

            if publisher_id == None:
                publisher_name = data['publisher']['name']
                publisher_address = data['publisher']['addreess']
                book_publisher = Publisher.objects.create(name=publisher_name, country=publisher_address)
                book_author = Book.objects.get(id=data['author']['id'])
                book_category = Book.objects.get(id=data['category']['id'])
                book_publisher.save()
                new_book = Book.objects.create(
                    title=data['title'], summary=data['summary'], numOfPages=data['num'], language=data['language'], publisher=book_publisher, author=book_author, category=book_category)

            if category_id == None:
                category_name = data['category']['name']
                book_category = Category.objects.create(name=category_name)
                book_author = Book.objects.get(id=data['author']['id'])
                book_publisher = Book.objects.get(id=data['publisher']['id'])
                book_category.save()
                new_book = Book.objects.create(
                    title=data['title'], summary=data['summary'], numOfPages=data['num'], language=data['language'], publisher=book_publisher, author=book_author, category=book_category)

            new_book.save()

        serializer = BookSerializer(new_book)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        current_book = self.get_object()
        data = request.data
        author_id = data['author']['id']
        publisher_id = data['publisher']['id']
        category_id = data['category']['id']
        book_update = None

        if author_id != None and publisher_id != None and category_id != None:
            author_update = Author.objects.get(id=author_id)
            publisher_update = Author.objects.get(id=publisher_id)
            category_update = Author.objects.get(id=category_id)
            current_book.author = author_update
            current_book.publisher = publisher_update
            current_book.category = category_update

        else:
            if author_id == None:
                author_name = data['author']['name']
                author_country = data['author']['country']
                author_update = Author.objects.create(name=author_name, country=author_country)
                author_update.save()
                current_book.author = author_update

            if category_id == None:
                category_name = data['category']['name']
                category_update = Category.objects.create(name=category_name)
                category_update.save()
                current_book.category = category_update

            if publisher_id == None:
                publisher_name = data['publisher']['name']
                publisher_address = data['publisher']['address']
                publisher_update = Publisher.objects.create(name=publisher_name, address=publisher_address)
                author_update.save()
                current_book.publisher = author_update

        current_book.title = data['title']
        current_book.summary = data['summary']
        current_book.num = data['num']
        current_book.language = data['language']
        current_book.save()

        serializer = BookSerializer(current_book)

        return Response(serializer.data)


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        list_author = Author.objects.all()
        return list_author

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        list_category = Category.objects.all()
        return list_category

class PublisherViewSet(viewsets.ModelViewSet):
    serializer_class = PublisherSerializer

    def get_queryset(self):
        list_publisher = Publisher.objects.all()
        return list_publisher
