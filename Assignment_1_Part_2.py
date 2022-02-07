class Book(object):
    def __init__(self, author,title):
        self.author = author
        self.title = title
    def display(self):
        print(self.title + ", written by " + self.author)
Book1 = Book("John Steinbeck","Of Mice and Men")
Book2 = Book("Harper Lee","To Kill a Mockingbird")

Book1.display()
Book2.display()