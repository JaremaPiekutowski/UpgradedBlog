from flask import Flask, render_template
import requests

app = Flask(__name__)


def get_posts():
    # Set URL for our JSON in NPoint JSON bin
    blog_url = "https://api.npoint.io/21275bfda00ba71536c2"
    # Get data
    response = requests.get(blog_url)
    # Return JSON
    return response.json()


@app.route('/')
def home():
    # Get posts
    all_posts = get_posts()
    print (all_posts)
    # Render template of the homepage with all posts as a kwarg
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about():
    # Render template with all posts as a kwarg
    return render_template("about.html")


@app.route('/contact')
def contact():
    # Render template with all posts as a kwarg
    return render_template("contact.html")


@app.route('/post/<num>')
def display_post(num):
    # Get post with a chosen number
    selected_post = get_posts()[int(num)-1]
    # Return post.html
    return render_template("post.html", post=selected_post)


if __name__ == "__main__":
    app.run(debug=True)
