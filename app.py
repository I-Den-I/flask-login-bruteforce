from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "venom"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if username == "admin" and password == "supersecret123":
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
        "🤫 Секретний факт #1: Кіт має більше кісток, ніж людина.",
        "🔐 Секретний факт #2: У 90% випадків Wi-Fi мережі з іменем 'Free Wifi' — це пастка.",
        "🕵️‍♂️ Секретний факт #3: Найкращий спосіб запам'ятати пароль — придумати цілу історію."
    ]
    return render_template("dashboard.html", secret_data=secret_data)

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
