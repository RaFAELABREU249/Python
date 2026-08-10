from flask import jsonify, request, session
from app.controllers.api import bp
from app.controllers.common import login_obrigatorio
from app.services.task_service import listar_tarefas_por_usuario, contar_tarefas_por_status


@bp.route('/api/tarefas')
@login_obrigatorio
def api_tarefas():
    status = request.args.get('status', 'todos')
    user_id = session['user_id']
    tarefas = listar_tarefas_por_usuario(user_id, status)
    return jsonify([{
        'id': t.id,
        'titulo': t.titulo,
        'descricao': t.descricao,
        'status': t.status,
    } for t in tarefas])


@bp.route('/api/progresso')
@login_obrigatorio
def api_progresso():
    user_id = session['user_id']
    totals = contar_tarefas_por_status(user_id)
    return jsonify(totals)
