from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    book_author = db.Column(db.String(80))
    book_publisher = db.Column(db.String(80))

    def __repr__(self):
        return f"{self.book_name} - {self.book_author} - {self.book_publisher}"

    @app.route('/')
    def index():
        return 'Welcome to the Book Shelf!'

    @app.route('/books')
    def get_books():
        books = Book.query.all()
        output = []

        for book in books:
         book_data = {'book_name': book.book_name, 'book_author': book.book_author, 'book_publisher': book.book_publisher}
        output.append(book_data)

        return {"books": output}
   
    @app.route('/books/<id>')
    def get_book(id):
        book = Book.query.get_or_404(id)
        return {"book_name": book.book_name, "book_author": book.book_author}