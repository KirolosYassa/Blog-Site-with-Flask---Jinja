from flask import Flask, render_template
from post import Post

app = Flask(__name__)


@app.route("/")
def home():
    posts = Post()
    return render_template("index.html", posts=posts.get_posts())


@app.route("/index")
def index():
    posts = Post()
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post")
def post():
    return render_template("post.html")


@app.route("/post/<post_id>")
def get_specific_post(post_id):
    post_id = int(post_id)
    post = Post()
    single_post = post.get_a_post(post_id=post_id)
    return render_template("post.html", post=single_post)


if __name__ == "__main__":
    app.run(debug=True)
