from fastapi import FastAPI, HTTPException, status #Primero pongo de donde lo voy a sacar, y depues que voy a sacar
                            #Para los codigos #status son los buenos
app = FastAPI()

@app.get("/productos")
def listar_productos():
    productos = session.query(Producto).all()
    return productos

@app.get("/productos/{id}")
def obtener_producto(id: int):
    producto = session.query(Producto).filter(Producto.id == id).first()
    if producto is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return producto