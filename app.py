from flask import Flask, render_template, request, redirect, url_for
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

app = Flask(__name__)

medicines = []

def check_reminders():
    now = datetime.now().strftime("%H:%M")
    for med in medicines:
        if med["reminder_time"] == now and med["stock"] > 0:
            print(f"🔔 Reminder: Take {med['name']}")

scheduler = BackgroundScheduler()
scheduler.add_job(check_reminders, 'interval', minutes=1)
scheduler.start()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":

        if "name" in request.form:
            name = request.form.get("name").strip()
            stock = int(request.form.get("stock"))
            reminder_time = request.form.get("reminder_time")

            for med in medicines:
                if med["name"].lower() == name.lower():
                    med["stock"] += stock
                    return redirect(url_for("home"))

            medicines.append({
                "name": name,
                "stock": stock,
                "reminder_time": reminder_time
            })

        if "taken_name" in request.form:
            taken_name = request.form.get("taken_name")
            for med in medicines:
                if med["name"] == taken_name and med["stock"] > 0:
                    med["stock"] -= 1

        if "delete_name" in request.form:
            delete_name = request.form.get("delete_name")
            medicines[:] = [m for m in medicines if m["name"] != delete_name]

        return redirect(url_for("home"))

    return render_template("index.html", medicines=medicines)

if __name__ == "__main__":
    app.run(debug=True)
