from flask import Flask, render_template, session, request, url_for, redirect

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
        name = request.form.get("name")
        muscle = request.form.get("muscle")
        equipment = request.form.get("equipment")
        instructions = request.form.get("instructions")
        image = request.form.get("image")

        exercise = {
            "name": name,
            "muscle": muscle,
            "equipment": equipment,
            "instructions": instructions,
            "image": image
        }

        session.setdefault("exercises", [])
        session["exercises"].append(exercise)
        session["exercises"] = session["exercises"]

        return redirect(url_for("view"))

    return render_template("add.html")

if __name__ == '__main__':
    app.run(debug=True)
