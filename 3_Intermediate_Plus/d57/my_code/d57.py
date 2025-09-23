# Blog Capstone Project (Part 1 – Templating)

from flask import Flask, render_template
from post import Post

app = Flask(__name__)
post=Post()

@app.route('/')
def home():
    blogs=post.blogs
    return render_template("index.html",blogs=blogs)

@app.route('/post/<int:blog_id>')
def blog_content(blog_id):
    post_title, subtitle, body=post.get_data(blog_id)

    return render_template("post.html",post_title=post_title,subtitle=subtitle,body=body)


if __name__ == "__main__":
    app.run(debug=True)
