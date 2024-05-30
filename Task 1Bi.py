class Book:
    def __init__(self, title, author, publisher, price, author_royalty):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._price = price
        self._author_royalty = author_royalty

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def author_royalty(self):
        return self._author_royalty

    @author_royalty.setter
    def author_royalty(self, value):
        self._author_royalty = value

    def royalty(self, copies_sold):
        if copies_sold <= 500:
            royalty_amount = self._price * copies_sold * self._author_royalty / 100
        elif copies_sold <= 1500:
            royalty_amount = 500 * self._price * self._author_royalty / 100 + (copies_sold - 500) * self._price * (self._author_royalty + 2.5) / 100
        else:
            royalty_amount = 500 * self._price * self._author_royalty / 100 + 1000 * self._price * (self._author_royalty + 2.5) / 100 + (copies_sold - 1500) * self._price * (self._author_royalty + 5) / 100
        return royalty_amount

class Ebook(Book):
    def __init__(self, title, author, publisher, price, author_royalty, format):
        super().__init__(title, author, publisher, price, author_royalty)
        self._format = format

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, value):
        self._format = value

    def royalty(self, copies_sold):
        royalty_amount = super().royalty(copies_sold)
        gst_amount = royalty_amount * 12 / 100
        return royalty_amount - gst_amount

# Example usage
book = Book('The Catcher in the Rye', 'J.D. Salinger', 'Little, Brown and Company', 10, 0.1)
print('Book royalty:', book.royalty(1000))

ebook = Ebook('The Catcher in the Rye', 'J.D. Salinger', 'Little, Brown and Company', 10, 0.1, 'EPUB')
print('Ebook royalty:', ebook.royalty(1000))