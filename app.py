from flask import Flask, render_template

app = Flask(__name__)

# configure app
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "should-not-be-seen"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
