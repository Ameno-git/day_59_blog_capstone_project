from flask import Flask, render_template
import requests

API_URL = "https://api.npoint.io/4c47f0e10a593ebaab57"

response = requests.get(API_URL)
all_post = response.json()

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html", all_post=all_post)


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return render_template("post.html", post=all_post[post_id - 1])


if __name__ == "__main__":
    app.run(debug=True)

