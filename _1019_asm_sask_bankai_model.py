# ASMENYS, SĄSKAITOS, BANKAI
# Padaryti programą, kurį leistų įvesti asmenis, bankus, asmenims priskirti 
# sąskaitas bankuose.

#     Asmuo turi vardą, pavardę, asmens kodą, tel. numerį.
#     Bankas turi pavadinimą, adresą, banko kodą, SWIFT kodą
#     Sąskaita turi numerį, balansą, priskirtą asmenį ir banką
#     Asmuo gali turėti daug sąskaitų tame pačiame arba skirtinguose bankuose

#     Padaryti duomenų bazės schemą (galima ją parodyti dėstytojui).
#     Sukurti programą su UI konsolėje, kuri leistų įvesti asmenis, bankus, 
# sąskaitas. Leistų vartotojui peržiūrėti savo sąskaitas ir jų informaciją, 
# pridėti arba nuimti iš jų pinigų. Taip pat leistų bendrai peržiūrėti 
# visus bankus, vartotojus, sąskaitas ir jų informaciją.

from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data/saskaitos.db')
Base = declarative_base()

class Asmuo(Base):
    __tablename__="asmuo"
    id = Column(Integer, primary_key=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    asm_kodas = Column("asmens kodas", Integer, unique=True)
    mobilus = Column("tel. nr.", Integer)
    saskaitos = relationship("Saskaita", back_populates="asmenys")
    
    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.pavarde}, {self.asm_kodas}, {self.mobilus})"

class Bankas(Base):
    __tablename__="bankas"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("pavadinimas", String)
    adresas = Column("adresas", String)
    b_kodas = Column("banko kodas", Integer)
    swift = Column("SWIFT kodas", String)
    saskaitos = relationship("Saskaita", back_populates="bankai")

    def __repr__(self):
        return f"({self.id}, {self.pavadinimas}, {self.adresas}, {self.b_kodas}, {self.swift})"

class Saskaita(Base):
    __tablename__="saskaita"
    id = Column(Integer, primary_key=True)
    numeris = Column("sąskaitos numeris", Integer)
    balansas = Column("balansas", Float)
    asmuo_id = Column("asmuo_id", Integer, ForeignKey("asmuo.id"))
    asmenys = relationship("Asmuo", back_populates="saskaitos")
    bankas_id = Column("bankas_id", Integer, ForeignKey("bankas.id"))
    bankai = relationship("Bankas", back_populates="saskaitos")

    def __repr__(self):
        return f"({self.id}, {self.numeris}, {self.balansas}"

if __name__ == "__main__":
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

