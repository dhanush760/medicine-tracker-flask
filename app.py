from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# In-memory storage
medicines = []

@app.route("/", methods=["GET", "POST"])
def home():
    global medicines

    if request.method == "POST":

        # ADD MEDICINE
        if "add_medicine" in request.form:
            name = request.form.get("name").strip()
            stock = int(request.form.get("stock"))
            reminder = request.form.get("reminder")

            # ❌ Prevent duplicate medicine names
            for med in medicines:
                if med["name"].lower() == name.lower():
                    return redirect(url_for("home"))

            medicines.append({
                "name": name,
                "stock": stock,
                "reminder": reminder
            })

        # MARK AS TAKEN
        if "taken" in request.form:
            name = request.form.get("taken")
            for med in medicines:
                if med["name"] == name and med["stock"] > 0:
                    med["stock"] -= 1

        # DELETE MEDICINE
        if "delete" in request.form:
            name = request.form.get("delete")
            medicines = [m for m in medicines if m["name"] != name]

        return redirect(url_for("home"))

    # Current time for reminder comparison
    now = datetime.now().strftime("%H:%M")

    return render_template("index.html", medicines=medicines, now=now)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
