from app import app, db

### En este archivo van todas las tablas y al final se abren ###

        
class Contacto(db.Model):  # Contacto hereda de db.Model
    """
    Definición de la tabla Contacto en la base de datos.
    La clase Contacto hereda de db.Model.
    Esta clase representa la tabla "Contacto" en la base de datos.
    """
    id_contacto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    correo_electronico = db.Column(db.String(100))
    telefono = db.Column(db.Integer)
    direccion = db.Column(db.String(100))

    def __init__(self, nombre, apellido, correo_electronico, telefono, direccion):
        """
        Constructor de la clase Contacto.

        Args:
            nombre (str): Nombre del contacto.
            apellido (str): Apellido del contacto.
            correo_electronico (str): correo electronico
            telefono (int): nro de telefono del contacto
            direccion (str): domicilio del contacto.
        """
        self.nombre = nombre
        self.apellido =  apellido
        self.correo_electronico = correo_electronico
        self.telefono = telefono
        self.direccion = direccion

with app.app_context():
    db.create_all()  # Crea todas las tablas en la base de datos