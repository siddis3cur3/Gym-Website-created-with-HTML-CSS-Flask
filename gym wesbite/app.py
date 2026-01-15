from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    highlights = [
        "Modern Equipment",
        "Certified Trainers",
        "Clean & Safe Environment"
    ]
    return render_template("home.html", highlights=highlights)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/membership")
def membership():
    plans = [
        {"name": "Monthly", "price": "$30"},
        {"name": "Quarterly", "price": "$80"},
        {"name": "Annual", "price": "$300"}
    ]
    return render_template("membership.html", plans=plans)

if __name__ == "__main__":
    app.run(debug=True)
