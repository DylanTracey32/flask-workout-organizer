from flask import Flask, render_template, session, request, url_for, redirect
from werkzeug.utils import secure_filename
import os

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
        image = request.files.get("image")
        image_filename = None

        if image and image.filename != "":
            filename = secure_filename(image.filename)
            image_path = os.path.join("static", "uploads", filename)
            image.save(image_path)
            image_filename = filename

        exercise = {
            "name": name,
            "muscle": muscle,
            "equipment": equipment,
            "instructions": instructions,
            "image": image_filename
        }

        session.setdefault("exercises", [])
        session["exercises"].append(exercise)
        session["exercises"] = session["exercises"]

        return redirect(url_for("view"))

    return render_template("add.html")

@app.route('/delete', methods=["POST"])
def delete():
    index = int(request.form.get('index'))

    if "exercises" in session and 0 <= index < len(session["exercises"]):
        session["exercises"].pop(index)
        session["exercises"] = session["exercises"]

    return redirect(url_for("view"))

if __name__ == '__main__':
    app.run(debug=True)
