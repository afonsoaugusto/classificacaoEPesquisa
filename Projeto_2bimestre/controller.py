from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from define import Base

class Controller:
	engine = create_engine('sqlite:///classificacao_pesquisa.db')
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

