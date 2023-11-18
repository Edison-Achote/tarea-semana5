from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
# se importa el engine
from base_datos import engine

# se crea la clase llamada Base que permite definir las clases bajo las
# características de SQLAlchemy
Base = declarative_base()

# Se crea la una entidad llamada Autor, que hereda
# de Base
class Ciudades(Base):
    __tablename__ = 'ciudades' # El nombre de la entidad en sqlite
    # Se definen los atributos
    id = Column(Integer, primary_key=True) # este atributo es entero y
                                        # se lo considera como llave
                                        # primaria
    nombreciudad = Column(String) # atributo de tipo String
    pais = Column(String)
    continente = Column(String)


    def __str__(self):
        return "%s %s %s %s", (self.nombreciudad, self.pais, self.continente)
    
class Estadio(Base):
    __tablename__ = 'estadio' # El nombre de la entidad en sqlite
    # Se definen los atributos
    id = Column(Integer, primary_key=True) # este atributo es entero y
                                        # se lo considera como llave
                                        # primaria
    nombreestadio = Column(String) # atributo de tipo String
    ciudades = Column(String)
    direccion = Column(String)


    def __str__(self):
        return "%s %s %s %s",  (self.nombreestadio, self.ciudades, self.direccion)
# Sentencia que permite crear o migrar las clases en Python al
# gestor de base de datos, expresado en el engine.
Base.metadata.create_all(engine)
