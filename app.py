from fastapi import FastAPI, HTTPException, status #Primero pongo de donde lo voy a sacar, y depues que voy a sacar
                            #Para los codigos #status son los buenos
from database import Producto, Venta, session # importar la base de datos, escribiendo las clases 
                                              # y tamb importas session que es nuestro
app = FastAPI()

# GET es para obetener algo, en este caso todos los productos
@app.get("/productos")
def listar_productos():
    productos = session.query(Producto).all()
    return [vars (p) for p in productos]  # es como un bucle que le va a devolver los productos uno a uno

# GET es para obtener, en este caso con id especifico
@app.get("/productos/{id}")
def obtener_producto(id: int):
    producto = session.query(Producto).filter(Producto.id == id).first()
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return vars(producto)


#POST para agregar datos
@app.post("/productos", status_code = status.HTTP_201_CREATED)
def agregar_producto(datos_producto):  ####Me da error porque no sabe que es datos_productos
    try:
        producto_nuevo = Producto(
            nombre = datos_producto.nombre,
            precio = datos_producto.precio
        )
        session.add(producto_nuevo) #agrega el objeto nuevo a la sesión, "ponerlo en la fila de espera"
        session.commit()              #confirma y escribe de verdad en la base de datos
    except:
        session.rollback()
        raise HTTPException(status_code=400, detail="Error al crear producto (datos inválidos)")
    return vars(producto_nuevo)