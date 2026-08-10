from flask import render_template, request, redirect, url_for, flash, session
from app.controllers.tasks import bp
from app.controllers.common import login_obrigatorio, STATUS_OPTIONS
from app.services.advice_service import obter_conselho_diario
from app.services.task_service import (
    listar_tarefas_por_usuario,
    criar_tarefa,
    obter_tarefa_do_usuario,
    atualizar_tarefa,
    excluir_tarefa,
)


@bp.route('/dashboard')
@login_obrigatorio
def dashboard():
    status = request.args.get('status', 'todos')
    user_id = session['user_id']
    tarefas = listar_tarefas_por_usuario(user_id, status)
    advice = obter_conselho_diario()
    return render_template('dashboard.html', tarefas=tarefas, status=status, advice=advice, status_options=STATUS_OPTIONS)


@bp.route('/nova_tarefa', methods=['GET', 'POST'])
@login_obrigatorio
def nova_tarefa():
    if request.method == 'POST':
        titulo = request.form.get('titulo', '').strip()
        descricao = request.form.get('descricao', '').strip()
        status = request.form.get('status', 'pendente')

        tarefa, erro = criar_tarefa(session['user_id'], titulo, descricao, status)
        if erro:
            flash(erro, 'danger')
            return redirect(url_for('tasks.nova_tarefa'))

        flash('Tarefa criada com sucesso.', 'success')
        return redirect(url_for('tasks.dashboard'))

    return render_template('nova_tarefa.html', status_options=STATUS_OPTIONS)


@bp.route('/editar<int:id>', methods=['GET', 'POST'])
@login_obrigatorio
def editar(id):
    tarefa = obter_tarefa_do_usuario(id, session['user_id'])
    if not tarefa:
        flash('Tarefa não encontrada.', 'danger')
        return redirect(url_for('tasks.dashboard'))

    if request.method == 'POST':
        titulo = request.form.get('titulo', '').strip()
        descricao = request.form.get('descricao', '').strip()
        status = request.form.get('status', tarefa.status)

        erro = atualizar_tarefa(tarefa, titulo, descricao, status)
        if erro:
            flash(erro, 'danger')
            return redirect(url_for('tasks.editar', id=id))

        flash('Tarefa atualizada com sucesso.', 'success')
        return redirect(url_for('tasks.dashboard'))

    return render_template('editar.html', tarefa=tarefa, status_options=STATUS_OPTIONS)


@bp.route('/excluir<int:id>', methods=['POST'])
@login_obrigatorio
def excluir(id):
    tarefa = obter_tarefa_do_usuario(id, session['user_id'])
    erro = excluir_tarefa(tarefa)
    if erro:
        flash(erro, 'danger')
        return redirect(url_for('tasks.dashboard'))

    flash('Tarefa removida com sucesso.', 'success')
    return redirect(url_for('tasks.dashboard'))


@bp.route('/progresso')
@login_obrigatorio
def progresso():
    return render_template('progresso.html')
