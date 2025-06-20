from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "venom"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if username == "abobus" and password == "venomvenom":
            session["logged_in"] = True
            return redirect(url_for("dashboard"))
        else:
            message = "❌ Невірний логін або пароль"
            return render_template("login.html", message=message)
    return render_template("login.html", message="")

@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
  secret_data = [
    "🎮 Факт #1: Roblox було створено у 2006 році і з того часу зібрало мільйони активних гравців по всьому світу.",
    "🛠️ Факт #2: У Roblox гравці можуть створювати власні ігри за допомогою мови програмування Lua.",
    "🌍 Факт #3: Roblox має власний внутрішній ринок, де гравці можуть купувати та продавати віртуальні речі за валюту Robux.",
    "🚀 Факт #4: Roblox підтримує кросплатформену гру — гравці можуть грати разом на ПК, мобільних пристроях і консолях.",
    "👾 Факт #5: Найпопулярніші ігри на Roblox можуть збирати мільйони гравців одночасно і навіть приносити авторам мільйонні доходи.",
    "⚠️ Факт #6: На початку існування Roblox майже не було модерації, через що в іграх іноді зʼявлялися фашистські угрупування і неприпустимий контент."
]
    return render_template("dashboard.html", secret_data=secret_data)

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
