from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .modeloBase import ModeloBase
from .filme import Filme
from .sala import Sala
from .sessao import Sessao
from .ingresso import Ingresso

__all__ = ["db", "ModeloBase", "Filme", "Sala", "Sessao", "Ingresso"]