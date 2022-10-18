# ORM (sqlalchemy) II dalis - ryšiai

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# sqlite - protokolas, data - folderis, tevai_vaikai.db - failas
engine = create_engine('sqlite:///data/tevai_vaikai.db')
# baze, kuri jungia klases
Base = declarative_base()

# Tevas lentele
class Tevas(Base):
    __tablename__ = "tevas"
    id = Column(Integer, primary_key=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)

    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.pavarde})"

# Vaikas lentele, vaikas gali tureti teva, sujungta su tevas lentele
class Vaikas(Base):
    __tablename__ = "vaikas"
    id = Column(Integer, primary_key=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    # nullable reiskia, kad gali buti be mokymo istaigos
    mokymo_istaiga = Column("mokykla", String, nullable=True)
    # ForeignKey("tevas.id") lenteles pavadinimas, ne objekto pavadinimas, sitas skirtas sql'ui
    tevas_id = Column("tevas_id", Integer, ForeignKey("tevas.id"))
    # Relationship veda i objekto pavadinimą, relationship skirtas pythonui, kad zinot, jog sujungtas su class Tevas
    tevas = relationship("Tevas")

    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.pavarde}, {self.tevas})"

if __name__ == "__main__":
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
