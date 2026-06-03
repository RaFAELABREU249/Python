"""
AtividadeSQLalchemy 2.0 — Loja de produtos tecnológicos
Complete os trechos marcados com TODO ALUNO.

Execute após corrigir: python app.py
"""

import os

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

# TODO ALUNO: importe SQLAlchemy
# from flask_sqlalchemy import ___________


app = Flask(__name__)
pasta_aula = os.path.abspath(os.path.dirname(__file__))

# TODO ALUNO: configure a URI do SQLite (arquivo loja.db nesta pasta)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(pasta_aula, "___________")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(pasta_aula, "loja.db")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# TODO ALUNO: crie o objeto db
# db = SQLAlchemy(app)
db = SQLAlchemy(app)

# --- MODEL: tabela produtos (COMPLETE A CLASSE) ---
class Produto(db.Model):
    # TODO ALUNO: nome da tabela
    __tablename__ = "produtos"

    # TODO ALUNO: id (Integer, primary_key=True)
    id = db.Column(db.Integer, primary_key=True)

    # TODO ALUNO: nome String(120), nullable=False
    nome = db.Column(db.String(120), nullable=False)

    # TODO ALUNO: categoria String(60), nullable=False
    categoria = db.Column(db.String(60), nullable=False)

    # TODO ALUNO: preco Float, nullable=False
    preco = db.Column(db.Float, nullable=False)

    # TODO ALUNO: estoque Integer, nullable=False, default=0
    estoque = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"<Produto {self.id} {self.nome}>"



# TODO ALUNO: criar tabelas no banco
# with app.app_context():
#     db.create_all()
with app.app_context():
    db.create_all()

def _ler_formulario():
    """Lê campos do POST — nomes devem bater com o HTML (name=)."""
    return {
        "nome": request.form.get("nome", "").strip(),
        "categoria": request.form.get("categoria", "").strip(),
        "preco": request.form.get("preco", "").strip(),
        "estoque": request.form.get("estoque", "").strip(),
    }


def _validar(dados):
    if not dados["nome"] or not dados["categoria"] or not dados["preco"]:
        return "Preencha nome, categoria e preço."
    try:
        preco = float(dados["preco"].replace(",", "."))
        estoque = int(dados["estoque"] or 0)
    except ValueError:
        return "Preço ou estoque inválido."
    if preco < 0 or estoque < 0:
        return "Preço e estoque não podem ser negativos."
    return None


# --- READ ---
@app.route("/")
def index():
    produtos = Produto.query.order_by(Produto.nome).all()
    return render_template("lista.html", produtos=produtos)


# --- CREATE ---
@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        dados = _ler_formulario()
        erro = _validar(dados)
        if erro:
            return render_template(
                "formulario.html",
                titulo="Cadastrar produto",
                erro=erro,
                **dados,
            )
        produto = Produto(
            nome=dados["nome"],
            categoria=dados["categoria"],
            preco=float(dados["preco"].replace(",", ".")),
            estoque=int(dados["estoque"] or 0),
        )
        db.session.add(produto)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("formulario.html", titulo="Cadastrar produto")


@app.route("/editar/<int:produto_id>", methods=["GET", "POST"])
def editar(produto_id):
    produto = db.session.get(Produto, produto_id)

    if not produto:
        return redirect(url_for("index"))

    if request.method == "POST":
        dados = _ler_formulario()
        erro = _validar(dados)
        if erro:
            return render_template(
                "formulario.html",
                titulo="Editar produto",
                erro=erro,
                produto_id=produto.id,
                **dados,
            )
        produto.nome = dados["nome"]
        produto.categoria = dados["categoria"]
        produto.preco = float(dados["preco"].replace(",", "."))
        produto.estoque = int(dados["estoque"] or 0)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template(
        "formulario.html",
        titulo="Editar produto",
        nome=produto.nome,
        categoria=produto.categoria,
        preco=produto.preco,
        estoque=produto.estoque,
        produto_id=produto.id,
    )


@app.route("/excluir/<int:produto_id>", methods=["POST"])
def excluir(produto_id):
    produto = db.session.get(Produto, produto_id)
    if produto:
        db.session.delete(produto)
        db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
