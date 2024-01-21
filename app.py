from flask import Flask, flash, redirect, url_for, render_template, request, session

app = Flask(__name__)

@app.route("/")
def main():
    return redirect("/home")

@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True, port=8800)
