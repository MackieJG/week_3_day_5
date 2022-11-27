from flask import render_template, request, redirect
from models.book import *
from models.book_list import *
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/library/')
def show_library():
    return render_template('library.html', library=books)

@app.route('/library/<int:book_index>')
def book(book_index):
    current_book = books[book_index]
    return render_template('book.html', book=current_book)

@app.route('/library/new/')
def new_book():
    return render_template('new_book.html')

@app.route('/library/', methods=['POST'])
def save_book():
    form_data = request.form
    book_title = form_data['book_title']
    book_author = form_data['book_author']
    book_genre = form_data['book_genre']
    checked_out = True if "checkbox" in request.form else False

    new_book = Book(title=book_title, author=book_author, genre=book_genre, checked_out=checked_out)
    add_book(new_book)

    return redirect('/library')

@app.route('/library/remove/<title>', methods=['POST'])
def delete_book(title):
    remove_book(title)
    return redirect('/library/')

