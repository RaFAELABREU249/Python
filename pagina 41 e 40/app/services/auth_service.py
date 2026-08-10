from app import db
from app.models.user import User


def validar_credenciais(email: str, senha: str):
    if not email or not senha:
        return None, 'Email e senha são obrigatórios.'

    usuario = User.query.filter_by(email=email).first()
    if not usuario or not usuario.checar_senha(senha):
        return None, 'Credenciais inválidas.'

    return usuario, None


def registrar_usuario(nome: str, email: str, senha: str, confirma: str):
    if not nome or not email or not senha or not confirma:
        return None, 'Todos os campos são obrigatórios.'
    if senha != confirma:
        return None, 'As senhas não coincidem.'
    if User.query.filter_by(email=email).first():
        return None, 'Email já cadastrado.'

    usuario = User(nome=nome, email=email)
    usuario.set_senha(senha)
    db.session.add(usuario)
    db.session.commit()
    return usuario, None
