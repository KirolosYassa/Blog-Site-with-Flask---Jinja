from flask import Flask, render_template, request
from post import Post
from email.message import EmailMessage
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()
Email = os.getenv("MY_EMAIL")
PassWord = os.getenv("EMAIL_PASSWORD")

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
        user_email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        print(name, user_email, phone, message)
        contact_sent = True

        message = f"""
        Name: {name}
        Email: {user_email}
        Phone: {phone}
        Message: {message}
        """

        msg = EmailMessage()
        msg["Subject"] = f"A new contact has been created"
        msg["From"] = Email
        msg["To"] = user_email
        msg.set_content(message)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=Email, password=PassWord)
            connection.send_message(msg)

    return render_template("contact.html", contact_sent=contact_sent)


if __name__ == "__main__":
    app.run(debug=True)
