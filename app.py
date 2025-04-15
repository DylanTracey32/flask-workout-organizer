from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = "terminator-two"


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/view')
def view():
    return render_template("view.html")

@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        pass
    return render_template("add.html")

if __name__ == '__main__':
    app.run(debug=True)
