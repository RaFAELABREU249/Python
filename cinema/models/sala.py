from . import db
from .modeloBase import ModeloBase

class Sala(ModeloBase):
    __tablename__ = "salas"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)
    
    sessao = db.relationship('Sessao', back_populates='sala')

    @classmethod
    def listar(cls):
        return cls.query.order_by(cls.numero).all()