from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

SECRET_KEY = "hardcoded-secret-123"   # intentional vulnerability

notes = []

TEMPLATE = """
<h1>My Notes</h1>
<form method="POST" action="/add">
  <input name="note" placeholder="Add a note">
  <button type="submit">Add</button>
</form>
<ul>{% for n in notes %}<li>{{ n }}</li>{% endfor %}</ul>
<p>Search: <a href="/search?q={{ query }}">{{ query }}</a></p>
"""

@app.route("/")
def index():
    return render_template_string(TEMPLATE, notes=notes, query="")

@app.route("/add", methods=["POST"])
def add():
    note = request.form.get("note")  # no validation — intentional
    notes.append(note)
    return index()

@app.route("/search")
def search():
    q = request.args.get("q", "")
    return render_template_string(TEMPLATE, notes=notes, query=q)

if __name__ == "__main__":
    app.run(debug=True)   # debug=True in production — intentional vulnerability