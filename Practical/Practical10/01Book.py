class Book:
    def __init__(self, name="Unknown", author="Unknown", price=0.0):
        """Default constructor initializes book details."""
        self.name = name
        self.author = author
        self.price = price

    def display_details(self):
        """Displays book details."""
        print(f"Book Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")

# Creating a book object with default values
default_book = Book()
default_book.display_details()

print("\n")

# Creating a book object with specific values
book1 = Book("The Alchemist", "Paulo Coelho", 15.99)
book1.display_details()
