from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        "title": "Post 1",
        "author": "John",
        "content": "This is the first blog",
        "date_posted": "April 21st, 2010"
    },
    {
        "title": "Post 2",
        "author": "Doe",
        "content": "This is the second blog",
        "date_posted": "May 21st, 2010"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = "About")

if __name__ == "__main__":
    app.run(debug = True)
