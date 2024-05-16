from basededatos import base

class estudiante(base.Model):
    #Nombre de tabla
    
    __tablename__="estudiante"
    
    #Conjunto de atributos que van a ser los campos de la tabla
    
    #Llave primaria
    id=base.Column(base.Integer, primary_key=True)
    nombre=base.Column(base.String(50))
    email=base.Column(base.String(70))
    codigo=base.Column(base.String(15))
    
    #Metodo constructor para mapear datps a los campos definidos
    
    def __init__(self, nombre, email, codigo):
        self.nombre=nombre
        self.email=email
        self.codigo=codigo