from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, date

app = Flask(__name__)

medicines = []

@app.route("/", methods=["GET", "POST"])
def home():
    global medicines

    today = date.today().isoformat()

    if request.method == "POST":

        # ADD MEDICINE
        if "add_medicine" in request.form:
            name = request.form.get("name").strip()
            stock = int(request.form.get("stock"))
            reminder = request.form.get("reminder")

            # Prevent duplicate names
            for med in medicines:
                if med["name"].lower() == name.lower():
                    return redirect(url_for("home"))

            medicines.append({
                "name": name,
                "stock": stock,
                "reminder": reminder,
                "last_taken": None
            })

        # MARK AS TAKEN
        if "taken" in request.form:
            name = request.form.get("taken")
            for med in medicines:
                if med["name"] == name and med["stock"] > 0:
                    med["stock"] -= 1
                    med["last_taken"] = today  # ✅ Mark taken today

        # DELETE MEDICINE
        if "delete" in request.form:
            name = request.form.get("delete")
            medicines = [m for m in medicines if m["name"] != name]

        return redirect(url_for("home"))

    now_time = datetime.now().strftime("%H:%M")

    return render_template(
        "index.html",
        medicines=medicines,
        now_time=now_time,
        today=today
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
