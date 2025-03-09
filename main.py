from flask import Flask, render_template, request, redirect, url_for, flash
app_Cheuri = Flask (__name__)

app_Cheuri.secret_key = "cheurimaria"

Usuario = {
    "email": "maria@gmail.com",
    "senha": "seg@123"
}

@app_Cheuri.route("/")
def login():
    return render_template("login.html")

@app_Cheuri.route("/login", methods = ["POST"])
def autenticar():
    email = request.form.get("email")
    senha = request.form.get("passoword")
    
    if email == Usuario["email"] and senha == Usuario["senha"]:
        flash("Lpgin realizado com sucesso!", "sucess")
    else:
        flash("Credenciais inválidas. Tente novamente.", "danger")
        return redirect(url_for("login"))
    