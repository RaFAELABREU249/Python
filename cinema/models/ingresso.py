from . import db
from .modeloBase import ModeloBase


class Ingresso(ModeloBase):
    __tablename__ = "ingressos"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    assento = db.Column(db.String(10), nullable=False)
    nome_comprador = db.Column(db.String(120), nullable=False)

    sessao_id = db.Column(db.Integer, db.ForeignKey('sessoes.id'), nullable=False)
    sessao = db.relationship('Sessao', back_populates='ingressos')