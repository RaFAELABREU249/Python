from . import db 
from .modeloBase import ModeloBase

class Filme(ModeloBase):
    __tablename__ = "filmes"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    titulo = db.Column(db.String(150), nullable=False)
    duracao_min = db.Column(db.Integer, nullable=False)
    classificacao = db.Column(db.String(5), nullable=False)

    sessao = db.relationship('Sessao', back_populates='filme')

    @classmethod
    def listar(cls):
        return cls.query.order_by(cls.titulo).all()