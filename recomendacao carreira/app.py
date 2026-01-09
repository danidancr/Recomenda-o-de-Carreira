from flask import Flask, render_template, request
from facts import Facts
from inference import forward_chaining

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []

    if request.method == "POST":
        facts = Facts()

        answers = request.form.getlist("interreses")

        for answer in answers:
            facts.add_fact(answer)

        recommendations = forward_chaining(facts)

    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
