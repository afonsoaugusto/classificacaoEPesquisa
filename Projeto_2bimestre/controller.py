# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from define import Algoritimo, Execucao,Detalhes
from define import Base

class Controller:
	engine = create_engine('sqlite:///classificacao_pesquisa.db')
	engine.raw_connection().connection.text_factory = str
	#engine = create_engine('oracle:/ADMSIREP:ADMSIREP@localhost:1521/xe')
	Base.metadata.bind = engine
	DBSession = sessionmaker(bind=engine)

	def persistirObjeto(self, objeto):
		try:
			session = self.DBSession()
			session.add(objeto)
			session.commit()
		except:
			session.rollback()
			raise

	def removerObjeto(self, objeto):
		try:
			session = self.DBSession()
			session.delete(objeto)
			session.commit()
		except:
			session.rollback()
			raise
	
	def findAlgoritimo(self,algoritimo):
		try:
			session = self.DBSession()
			algoritimo = session.query(Algoritimo).filter(Algoritimo.nomeAlgoritimo == algoritimo.nomeAlgoritimo).one()
			return algoritimo
		except:
			session.rollback()
			return None
