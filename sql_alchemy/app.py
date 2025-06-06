import os

from flask import Flask
from flask import render_template

from database import db, Book, Genre

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

    fiction = Genre(name="Жарн 1")
    db.session.add(fiction)
    mystery = Genre(name="Жанр 2")
    db.session.add(mystery)

    book1 = Book(title="Книга 1", genre=fiction)
    db.session.add(book1)
    book2 = Book(title="Книга 2", genre=mystery)
    db.session.add(book2)
    book3 = Book(title="Книга 3", genre=fiction)
    db.session.add(book3)

    db.session.commit()

@app.route("/")
def all_books():
    books = Book.query.order_by(Book.added.desc()).limit(15).all()
    return render_template("all_books.html", books=books)

@app.route("/genre/<int:genre_id>")
def books_by_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    return render_template(
        "books_by_genre.html",
        genre_name=genre.name,
        books=genre.books,
    )

if __name__ == '__main__':
    app.run()