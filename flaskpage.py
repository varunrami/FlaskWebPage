from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'sonaalpathlaipradeep'

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


@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def home():
    return render_template('home.html')

@app.route("/", methods=['POST'])
@app.route("/home", methods=['POST'])
def home2():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = "About")

@app.route("/upload", methods=['POST'])
def upload():
    return redirect(url_for('home'))

@app.route("/upload", methods=['GET'])
def upload2():
    return render_template('upload.html', title = "Submit")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("Account Created for : {}!".format(form.username.data), 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title = "Registration", form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = "Login", form = form)

if __name__ == "__main__":
    app.run(debug = True)
