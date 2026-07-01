from flask import Blueprint, redirect, render_template, request, url_for, flash
from models import Filme, Sala, Sessao, db

cinema_bp = Blueprint("cinema", __name__, url_prefix="/cinema")


@cinema_bp.route("/")
def index():
    try:
        sessoes = Sessao.listar_com_detalhes()
    except Exception as e:
        flash(f"Erro ao carregar sessões: {e}", "error")
        sessoes = []
    return render_template("cinema/lista_sessoes.html", sessoes=sessoes)


@cinema_bp.route("/sessao/cadastrar", methods=["GET", "POST"])
def cadastrar_sessao():
    try:
        filmes = Filme.listar()
        salas = Sala.listar()
    except Exception as e:
        flash(f"Erro ao carregar filmes ou salas: {e}", "error")
        return redirect(url_for("cinema.index"))

    if request.method == "POST":
        filme_id = request.form.get("filme_id")
        sala_id = request.form.get("sala_id")
        data_hora = request.form.get("data_hora")
        preco = request.form.get("preco")

        if not filme_id or not sala_id or not data_hora or not preco:
            flash("Todos os campos são obrigatórios.", "error")
        else:
            try:
                nova_sessao = Sessao(
                    filme_id=filme_id,
                    sala_id=sala_id,
                    data_hora=data_hora,
                    preco=float(preco),
                )
                db.session.add(nova_sessao)
                db.session.commit()
                flash("Sessão cadastrada com sucesso!", "success")
                return redirect(url_for("cinema.index"))
            except Exception as e:
                db.session.rollback()
                flash(f"Erro ao cadastrar sessão: {e}", "error")

    return render_template("cinema/formulario_sessao.html", filmes=filmes, salas=salas)


@cinema_bp.route("/sessao/editar/<int:sessao_id>", methods=["GET", "POST"])
def editar_sessao(sessao_id):
    try:
        sessao = Sessao.query.get_or_404(sessao_id)
        filmes = Filme.listar()
        salas = Sala.listar()
    except Exception as e:
        flash(f"Erro ao carregar dados para edição: {e}", "error")
        return redirect(url_for("cinema.index"))

    if request.method == "POST":
        sessao.filme_id = request.form.get("filme_id")
        sessao.sala_id = request.form.get("sala_id")
        sessao.data_hora = request.form.get("data_hora")
        sessao.preco = request.form.get("preco")

        if not sessao.filme_id or not sessao.sala_id or not sessao.data_hora or not sessao.preco:
            flash("Todos os campos são obrigatórios.", "error")
        else:
            try:
                db.session.commit()
                flash("Sessão atualizada com sucesso!", "success")
                return redirect(url_for("cinema.index"))
            except Exception as e:
                db.session.rollback()
                flash(f"Erro ao atualizar sessão: {e}", "error")

    return render_template(
        "cinema/formulario_sessao.html",
        filmes=filmes,
        salas=salas,
        sessao=sessao,
    )


@cinema_bp.route("/sessao/deletar/<int:sessao_id>", methods=["POST"])
def deletar_sessao(sessao_id):
    try:
        sessao = Sessao.query.get_or_404(sessao_id)
        db.session.delete(sessao)
        db.session.commit()
        flash("Sessão deletada com sucesso!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Erro ao deletar sessão: {e}", "error")

    return redirect(url_for("cinema.index"))