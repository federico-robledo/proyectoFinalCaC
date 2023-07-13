# Importa las clases Flask, jsonify y request del módulo flask
from flask import Flask, jsonify, request
from app import app, ma
from modelos import *

### En este archivo van todos los endpoints de cada tabla ###

# Definición del esquema para la clase Contacto
class ContactoSchema(ma.Schema):
    """
    Esquema de la clase Contacto.

    Este esquema define los campos que serán serializados/deserializados
    para la clase Contacto.
    """
    class Meta:
        fields = ("id_contacto", "nombre", "apellido", "correo_electronico", "telefono", "direccion")

contacto_schema = ContactoSchema()  # Objeto para serializar/deserializar un contacto
contactos_schema = ContactoSchema(many=True)  # Objeto para serializar/deserializar múltiples contactos


@app.route("/index", methods=["GET"])
def get_Contactos():
    """
    Endpoint para obtener todos los contactos de la base de datos.

    Retorna un JSON con todos los registros de la tabla de contactos.
    """
    all_contactos = Contacto.query.all()  # Obtiene todos los registros de la tabla de contactos
    result = contactos_schema.dump(all_contactos)  # Serializa los registros en formato JSON
    
    return jsonify(result)  # Retorna el JSON de todos los registros de la tabla
    

### Metodos tabla contactos ###

@app.route("/index/<id>", methods=["GET"])
def get_contacto(id):
    """
    Endpoint para obtener un contacto específico de la base de datos.

    Retorna un JSON con la información del contacto correspondiente al ID proporcionado.
    """
    contacto = Contacto.query.get(id)  # Obtiene el contacto correspondiente al ID recibido
    return contacto_schema.jsonify(contacto)  # Retorna el JSON del contacto

@app.route("/index/<id>", methods=["DELETE"])
def delete_producto(id):
    """
    Endpoint para eliminar un contacto de la base de datos.

    Elimina el contacto correspondiente al ID proporcionado y retorna un JSON con el registro eliminado.
    """
    contacto = Contacto.query.get(id)  # Obtiene el contacto correspondiente al ID recibido
    db.session.delete(contacto)  # Elimina el contacto de la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return contacto_schema.jsonify(contacto)  # Retorna el JSON del contacto eliminado

@app.route("/index", methods=["POST"])  # Endpoint para crear un contacto
def create_contacto():
    """
    Endpoint para crear un nuevo contacto en la base de datos.

    Lee los datos proporcionados en formato JSON por el cliente y crea un nuevo registro de contacto en la base de datos.
    Retorna un JSON con el nuevo contacto creado.
    """
    nombre = request.json["nombre"]  # Obtiene el nombre del contacto del JSON proporcionado
    apellido = request.json["apellido"]  # Obtiene el precio del contacto del JSON proporcionado
    correo_electronico = request.json["correo_electronico"]  # Obtiene el stock del contacto del JSON proporcionado
    telefono = request.json["telefono"]  # Obtiene la imagen del contacto del JSON proporcionado
    direccion = request.json["direccion"]  # Obtiene la imagen del contacto del JSON proporcionado
    new_contacto = Contacto(nombre, apellido, correo_electronico, telefono, direccion)  # Crea un nuevo objeto contacto con los datos proporcionados
    db.session.add(new_contacto)  # Agrega el nuevo contacto a la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return contacto_schema.jsonify(new_contacto)  # Retorna el JSON del nuevo contacto creado

@app.route("/index/<id>", methods=["PUT"])  # Endpoint para actualizar un contacto
def update_contacto(id):
    """
    Endpoint para actualizar un contacto existente en la base de datos.

    Lee los datos proporcionados en formato JSON por el cliente y actualiza el registro del contacto con el ID especificado.
    Retorna un JSON con el contacto actualizado.
    """
    contacto = Contacto.query.get(id)  # Obtiene el contacto existente con el ID especificado

    # Actualiza los atributos del contacto con los datos proporcionados en el JSON
    contacto.nombre = request.json["nombre"]
    contacto.apellido = request.json["apellido"]
    contacto.correo_electronico = request.json["correo_electronico"]
    contacto.telefono = request.json["telefono"]
    contacto.direccion = request.json["direccion"]

    db.session.commit()  # Guarda los cambios en la base de datos
    return contacto_schema.jsonify(contacto)  # Retorna el JSON del contacto actualizado