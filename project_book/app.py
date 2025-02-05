from flask import Flask, render_template, request, redirect, url_for
from models import db, Book


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mssql+pyodbc://LAPTOP-RHELF47O/22tb0093?driver=ODBC+Driver+17+for+SQL+Server'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Home - Display books
@app.route("/")
def index():
    books = Book.query.all()
    return render_template("index.html", books=books)

# Add book
@app.route("/add", methods=["POST"])
def add_book():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    published_year = request.form["published_year"]

    new_book = Book(title=title, author=author, genre=genre, published_year=published_year)
    db.session.add(new_book)
    db.session.commit()
    
    return redirect(url_for("index"))

# Delete book
@app.route("/delete/<int:id>")
def delete_book(id):
    book = Book.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
    
    return redirect(url_for("index"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Creates tables if they don't exist
    app.run(debug=True)
