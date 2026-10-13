from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    books = [
        {"title": "Python Basics", "author": "John Smith"},
        {"title": "Cloud Computing", "author": "David Miller"},
        {"title": "Docker Essentials", "author": "Mark Lee"},
        {"title": "Kubernetes Guide", "author": "Alex Brown"}
    ]
    return render_template("index.html", books=books)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
