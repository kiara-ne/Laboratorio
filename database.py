from sqlalchemy import create_engine, Column, Integer, String, Float, Date, Time, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///database.db', echo=True)

# Declarar la base
Base = declarative_base()


# Crear una clase que representa una tabla
class Producto(Base):  #La clase es la estructura
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True, autoincrement = True, nullable=False) #el nullable tiene que ser falso, eso significa que no puede ser null
    nombre = Column(String, nullable = False)
    precio = Column(Float, nullable = False)

class Venta(Base):
    __tablename__ = 'ventas'
    id = Column(Integer, primary_key=True, autoincrement = True, nullable=False)
    fecha = Column(Date, nullable=False)
    fecha = Column(Time, nullable=False)
    id_producto = Column(ForeignKey('productos.id'), nullable=False)
    fecha = Column(Integer, nullable=False)
    precio_total = Column(Float, nullable = False)

# Crear las tablas en el archivo si no existen
Base.metadata.create_all(engine)

# Crear una sesión para interactuar con la base
Session = sessionmaker(bind=engine) # Que la base de datos esta activa y esperando a una consulta
session = Session() #Renombra a la base como sesion

