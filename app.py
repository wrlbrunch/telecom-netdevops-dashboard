from flask import Flask, render_template, request
from network.ssh_client import executar_configuracao

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/configurar", methods=["POST"])
def configurar():
    dados = {
        "fabricante": request.form.get("fabricante"),
        "ip": request.form.get("ip"),
        "usuario": request.form.get("usuario"),
        "senha": request.form.get("senha"),
        "interface": request.form.get("interface"),
        "descricao": request.form.get("descricao"),
    }

    # Validação de campos vazios
    if not all(dados.values()):
        return render_template("index.html", sucesso=False, resultado="Preencha todos os campos.")

    sucesso, mensagem = executar_configuracao(
        fabricante=dados["fabricante"],
        ip=dados["ip"],
        usuario=dados["usuario"],
        senha=dados["senha"],
        interface=dados["interface"],
        descricao=dados["descricao"],
    )

    return render_template("index.html", sucesso=sucesso, resultado=mensagem)

if __name__ == "__main__":
    app.run(debug=True)