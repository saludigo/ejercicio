from flask import Flask, redirect, render_template,request, url_for
from basededatos import base
from estudiante import estudiante

class programa:
    def __init__(self):
       self.app=Flask(__name__)
       self.app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///estudiantes.sqlite3"
       
       #Agregar la db a nuestra aplicacion
       base.init_app(self.app)
       
       self.app.add_url_rule('/', view_func=self.buscarTodos)
       self.app.add_url_rule('/nuevo', view_func=self.agregar, methods=["GET","POST"])
       
       #iniciar el servidor para poder exponer las rutas y que las personas obtengan la funcionalidad que necesitan del programa
       with self.app.app_context():
           base.create_all()
       self.app.run(debug=True)
       
    def buscarTodos(self):
        return render_template('mostrarTodos.html', estudiante=estudiante.query.all())
    
    def agregar(self):
        #Verificar si debe enviar los datos o procesarlos
        if request.method=="POST":
            nombre=request.form['nombre']
            email=request.form['email']
            codigo=request.form['codigo']
            
            miestudiante=estudiante(nombre, email, codigo)
            #Guardar el objeto en la base de datos
            base.session.add(miestudiante)
            base.session.commit()
            return redirect(url_for('buscarTodos'))

        
        
        return render_template('intento.html')

miPrograma=programa()