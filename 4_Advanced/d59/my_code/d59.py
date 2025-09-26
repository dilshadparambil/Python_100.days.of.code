# Blog Capstone Project (Part 2 – Adding Styling)

import requests
from flask import Flask,render_template

app = Flask(__name__)

headers={
'USER-AGENT' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
}

url='https://api.npoint.io/0b940d2938d1896afaf4'
# https://www.npoint.io/ go to this site and create a json bin and add the data in blog-data.txt to get the api endpoint
response=requests.get(url,headers=headers)
data=response.json()
@app.route('/')
@app.route("/index.html")
def home():
    title='Home'
    return render_template('index.html',title=title ,blogs=data)

@app.route('/about.html')
def about():
    title = 'About'
    return render_template('about.html',title=title)

@app.route('/contact.html')
def contact():
    title = 'Contact'
    return render_template('contact.html',title=title)

@app.route('/post/<int:blog_id>')
def post(blog_id):
    title='Post'
    blog = ''
    for post_data in data:
        if post_data['id']==blog_id:
            blog=post_data
    return render_template('post.html',title=title,blog=blog)


if __name__=='__main__':
    app.run(debug=True)
