# My top 10 movies website

import os
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

TMDB_AUTH_TOKEN=os.getenv('TMDB_AUTH_TOKEN')
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///movie-list.db'
Bootstrap5(app)

headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_AUTH_TOKEN}"
    }

MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/original"

# CREATE DB
class Base(DeclarativeBase):
    pass

db=SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Movies(db.Model):
    id : Mapped[int]=mapped_column(Integer,primary_key=True)
    title : Mapped[str]=mapped_column(String(250),unique=True,nullable=False)
    year : Mapped[int]=mapped_column(Integer,nullable=False)
    description : Mapped[str]=mapped_column(String(500),nullable=False)
    rating : Mapped[float]=mapped_column(Float,nullable=True)
    ranking : Mapped[int]=mapped_column(Integer,nullable=True)
    review : Mapped[str]=mapped_column(String(250),nullable=True)
    img_url : Mapped[str]=mapped_column(String(250),nullable=False)

with app.app_context():
    db.create_all()

class EditForm(FlaskForm):
    form_rating=StringField('Your rating out of 10 e.g. 7.5')
    form_review=StringField('Your review')
    submit_bt=SubmitField('Done')

class AddForm(FlaskForm):
    movie_title=StringField('Movie Title',validators=[DataRequired()])
    add_bt=SubmitField('Add Movie')

@app.route("/")
def home():
    results=db.session.execute(db.select(Movies).order_by(Movies.rating))
    all_movies=results.scalars().all()
    for i in range(len(all_movies)):
        all_movies[i].ranking=len(all_movies)-i
    db.session.commit()

    return render_template("index.html",all_movies=all_movies)

@app.route("/edit",methods=['GET','POST'])
def edit():
    movie_id=request.args.get('id')
    my_form=EditForm()
    movie = db.get_or_404(Movies, movie_id)
    if my_form.validate_on_submit():
        movie.rating=my_form.form_rating.data
        movie.review=my_form.form_review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html",form=my_form,movie=movie)

@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movies, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add',methods=['GET','POST'])
def add():
    my_form = AddForm()
    if my_form.validate_on_submit():
        movie_title=my_form.movie_title.data
        params={
            'query':movie_title
        }
        response = requests.get(MOVIE_DB_SEARCH_URL, headers=headers,params=params)
        return render_template('select.html',data=response.json()['results'])

    return render_template('add.html',form=my_form)

@app.route('/get_movie',methods=['GET','POST'])
def get_movie():
    tmdb_movie_id = request.args.get('id')
    url=f'{MOVIE_DB_INFO_URL}/{tmdb_movie_id}'
    response = requests.get(url, headers=headers)
    search_result=response.json()
    movie_title=search_result['original_title']
    new_movie=Movies(
        title=movie_title,
        img_url=MOVIE_DB_IMAGE_URL+search_result['poster_path'],
        year=search_result['release_date'][:4],
        description=search_result['overview'])
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit',id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)





# for testing db

# with app.app_context():
#     new_movie = Movie(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#     )
#     second_movie = Movies(
#         title="Avatar The Way of Water",
#         year=2022,
#         description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )
#     db.session.add(second_movie)
#     db.session.commit()
