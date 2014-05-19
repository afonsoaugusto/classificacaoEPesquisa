import os
import sys
import datetime
from sqlalchemy.sql import func
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Algoritimo(Base):
	__tablename__ = 'algoritimo'

	id = Column(Integer, primary_key=True)
	classe = Column(String(250))
	estruturaDados = Column(String(50))
	complexidadePiorCaso = Column(String(50))
	complexidadeMedioCaso = Column(String(50))
	complexidadeMelhorCaso = Column(String(50))
	complexidadeEspacos = Column(String(250))


class Execucao(Base):
	__tablename__ = 'execucao'

	id = Column(Integer, primary_key=True)
	N = Column(Integer, default=100)
	LOW = Column(Integer, default=0)
	HIGH = Column(Integer, default=100000)
	SEED = Column(Integer, default=1234554321)
	NUM_FIND = Column(Integer, default=87)
	NUM_SECOND_FIND = Column(Integer, default=100001)
	DATE_EXECUTION  = Column(DateTime, default=datetime.datetime.utcnow)
	MODE = Column(String(3), default='-A')

class Detalhes(Base):
	__tablename__ = 'detalhes'

	id = Column(Integer, primary_key=True)
	quantidadeComparacoes = Column(Integer)
	quantidadeTrocas = Column(Integer)
	data = (DateTime)

	algoritimo_id = Column(Integer, ForeignKey('execucao.id'))
	#algoritimo = relationship(Algoritimo)
	execucao_id = Column(Integer, ForeignKey('execucao.id'))
	#execucao = relationship(Execucao)

# Create an engine that stores data in the local directory's
engine = create_engine('sqlite:///classificacao_pesquisa.db')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
