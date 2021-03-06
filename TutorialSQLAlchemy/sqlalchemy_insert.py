from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from sqlalchemy_declarative import Address, Base, Person
 
engine = create_engine('sqlite:///sqlalchemy_example.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
 
# Insert a Person in the person table
new_person = Person(name='new person')
new_person.padrao = '-A'
print new_person.name
print new_person.padrao
session.add(new_person)
session.commit()
 
# Insert an Address in the address table
new_address = Address(post_code='00011', person=new_person)
session.add(new_address)
session.commit()

nova_pessoa = session.query(Address).filter(Address.post_code == '00015').all()
print ''
print ''
print ''
print len(nova_pessoa)
print ''
print ''
print ''


import sqlite3
conn = sqlite3.connect('sqlalchemy_example.db')
 
c = conn.cursor()
c.execute('SELECT * FROM person')
print c.fetchall()
conn.close()
