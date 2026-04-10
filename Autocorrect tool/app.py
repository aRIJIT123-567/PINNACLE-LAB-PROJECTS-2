from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    corrected_text = ""

    if request.method == "POST":
        text = request.form["text"]
        corrected_text = str(TextBlob(text).correct())

    return render_template("index.html", corrected_text=corrected_text)

if __name__ == "__main__":
    app.run(debug=True)