from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

medicines = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":

        # Add medicine
        if "medicine_name" in request.form:
            name = request.form.get("medicine_name")
            stock = request.form.get("stock")

            medicines.append({
                "name": name,
                "stock": int(stock)
            })

        # Mark as taken
        if "taken_name" in request.form:
            taken_name = request.form.get("taken_name")

            for med in medicines:
                if med["name"] == taken_name and med["stock"] > 0:
                    med["stock"] -= 1

        return redirect(url_for("home"))

    return render_template("index.html", medicines=medicines)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

