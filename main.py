from flask import Flask, render_template, request
from post import Post

app = Flask(__name__)


@app.route("/")
def home():
    posts = Post()
    return render_template("index.html", posts=posts.get_posts())


@app.route("/index")
def index():
    home()


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<post_id>")
def get_specific_post(post_id):
    post_id = int(post_id)
    post = Post()
    single_post = post.get_a_post(post_id=post_id)
    print(single_post)
    return render_template("post.html", post=single_post)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    contact_sent = False
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        print(name, email, phone, message)
        contact_sent = True

    return render_template("contact.html", contact_sent=contact_sent)


if __name__ == "__main__":
    app.run(debug=True)
