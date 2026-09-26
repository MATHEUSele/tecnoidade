from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nome = db.Column(db.String(120), nullable=False)
    senha_hash = db.Column(db.String(256), nullable=True) # Senha criptografada
    tipo = db.Column(db.String(20), nullable=False) # 'idoso' ou 'familiar'
    codigo_vinculo = db.Column(db.String(20), unique=True, nullable=True) # Ex: 123456 (usado pelo idoso)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

class Vinculo(db.Model):
    __tablename__ = 'vinculos'
    
    id = db.Column(db.Integer, primary_key=True)
    familiar_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    idoso_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    data_vinculo = db.Column(db.DateTime, default=datetime.utcnow)

    familiar = db.relationship('Usuario', foreign_keys=[familiar_id], backref='idosos_vinculados')
    idoso = db.relationship('Usuario', foreign_keys=[idoso_id], backref='familiares_vinculados')

class Progresso(db.Model):
    __tablename__ = 'progressos'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    nome_curso = db.Column(db.String(100), nullable=False) # Ex: 'curso_banco', 'curso_pix'
    aula_numero = db.Column(db.Integer, nullable=False)
    data_conclusao = db.Column(db.DateTime, default=datetime.utcnow)

    usuario = db.relationship('Usuario', backref='aulas_concluidas')
