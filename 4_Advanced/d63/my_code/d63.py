# Virtual Bookshelf 📚  

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer,Float,String
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///all-books.db'

# creating db
class Base(DeclarativeBase):
    pass
db=SQLAlchemy(model_class=Base)
db.init_app(app)

# create table
class Books(db.Model):
    id : Mapped[int]=mapped_column(primary_key=True)
    title: Mapped[str]=mapped_column(String(250),nullable=False,unique=True)
    author: Mapped[str]=mapped_column(String(250),nullable=False)
    rating: Mapped[float]=mapped_column(nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():

    result = db.session.execute(db.select(Books))
    all_books=result.scalars().all()
    return render_template('index.html',all_books=all_books)


@app.route("/add",methods=['GET','POST'])
def add():
    if request.method=='POST':
        add_data=Books(title=request.form['book_name'], author=request.form['book_author'],
              rating=request.form['book_rating'])
        db.session.add(add_data)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/edit',methods=['GET','POST'])
def edit():
    book_id = request.args.get('id')
    book_data=db.get_or_404(Books,book_id)
    if request.method=='POST':

        book_data.rating=float(request.form['new_rating'])
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html',book=book_data)

@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    book_data = db.get_or_404(Books, book_id)
    db.session.delete(book_data)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

