from app import db

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(30), nullable=False, default='pendente')
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
