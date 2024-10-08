from django.db import models
from library.models.media_model import Media


class Book(Media):
    author = models.CharField(max_length=255, null=False)
    pages = models.IntegerField(null=False)
    language = models.CharField(max_length=50, null=False)
    release_date = models.DateField(null=False)
    publisher = models.CharField(max_length=150, null=False)

    class Meta:
        verbose_name_plural = "Books"

    def __str__(self):
        """
        Displays the title of the book, followed by the name of the author.

        Returns:
            str: The title and author of the book.
        """
        return f'LIVRE: {self.title}'

    def update_book_available(book_id):
        """
        Toggles the availability of a book.

        Args:
            book_id (int): The id of the book to update.
        """
        get_book = Book.objects.get(id=book_id)
        get_book.available = not get_book.available
        get_book.save()
