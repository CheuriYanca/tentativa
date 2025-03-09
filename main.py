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

@app_Cheuri.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome_completo = request.form["name"]
        cpf = request.form["cpf"]
        email = request.form["email"]
        
        telefone = request.form["phone"]
        endereco = request.form["address"]
        senha = request.form["password"]
        confirmar_senha = request.form["confirm_password"]

        if senha != confirmar_senha:
            flash("As senhas inseridas não coincidem. Tente novamente!", "error")
            return redirect(url_for("cadastro"))
        
        flash("Cadastro efetuado com sucesso!", "success")
        return redirect(url_for("login"))

    return render_template("cadastro.html")

@app_Cheuri.route("/contato")
def contato():
    return render_template("contato.html")

if __name__ == "__main__":
    app_Cheuri.run(debug=True)
    