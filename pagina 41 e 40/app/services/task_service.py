from app import db
from app.models.tarefa import Tarefa
from app.controllers.common import STATUS_OPTIONS


def listar_tarefas_por_usuario(usuario_id: int, status: str = 'todos'):
    query = Tarefa.query.filter_by(usuario_id=usuario_id)
    if status in STATUS_OPTIONS:
        query = query.filter_by(status=status)
    return query.order_by(Tarefa.id.desc()).all()


def obter_tarefa_do_usuario(id: int, usuario_id: int):
    return Tarefa.query.filter_by(id=id, usuario_id=usuario_id).first()


def criar_tarefa(usuario_id: int, titulo: str, descricao: str, status: str):
    if not titulo or not descricao:
        return None, 'Título e descrição são obrigatórios.'
    if status not in STATUS_OPTIONS:
        status = 'pendente'

    tarefa = Tarefa(titulo=titulo, descricao=descricao, status=status, usuario_id=usuario_id)
    db.session.add(tarefa)
    db.session.commit()
    return tarefa, None


def atualizar_tarefa(tarefa: Tarefa, titulo: str, descricao: str, status: str):
    if not tarefa:
        return 'Tarefa não encontrada.'
    if not titulo or not descricao:
        return 'Título e descrição são obrigatórios.'
    if status not in STATUS_OPTIONS:
        status = tarefa.status

    tarefa.titulo = titulo
    tarefa.descricao = descricao
    tarefa.status = status
    db.session.commit()
    return None


def excluir_tarefa(tarefa: Tarefa):
    if not tarefa:
        return 'Tarefa não encontrada.'
    db.session.delete(tarefa)
    db.session.commit()
    return None


def contar_tarefas_por_status(usuario_id: int):
    totals = {}
    for status in STATUS_OPTIONS:
        totals[status] = Tarefa.query.filter_by(usuario_id=usuario_id, status=status).count()
    return totals
