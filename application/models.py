from app import app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), unique = True)    
    passhash = db.Column(db.String(256), nullable = False)    
    name = db.Column(db.String(64), nullable = True)    
    is_admin = db.Column(db.Boolean(), nullable = False, default = False)

class Section(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), nullable = True)


    books = db.relationship('Book', backref ='section', lazy = True)

class Book(db.Model):   
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), nullable = True)
    content = db.Column(db.String(64), nullable = True)
    author = db.Column(db.String(64), nullable = True)
    # date_issued = db.Column(db.Date)
    return_date = db.Column(db.Date)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=False)

    carts = db.relationship('Cart', backref ='book', lazy = True)

class Cart(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
   username = db.Column(db.String(64), db.ForeignKey('user.username'), nullable = False)
   book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable = False)
   

class AdminIssued(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer)
    username = db.Column(db.String(64))
    bookname = db.Column(db.String(64))
    content = db.Column(db.String(256))
    author = db.Column(db.String(64))
    date_issued = db.Column(db.Date)
    return_date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    request_id = db.Column(db.Integer, db.ForeignKey("cart.id"))
    

class UserBooks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookname = db.Column(db.String(64))  
    content = db.Column(db.String(256))
    author = db.Column(db.String(64))
    book_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # return_date = db.Column(db.Date)
    #  # Add foreign key to AdminIssued
    # admin_issued_id = db.Column(db.Integer, db.ForeignKey("admin_issued.id"))

with app.app_context():
    db.create_all()

    #Checking if this is the admin/librarian

    admin = User.query.filter_by(is_admin=True).first()
    if not admin:
        password_hash = generate_password_hash('admin')
        admin = User(username='admin', passhash=password_hash, name='Admin', is_admin=True)
        db.session.add(admin)
        db.session.commit()

