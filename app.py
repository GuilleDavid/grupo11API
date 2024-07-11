from flask import Flask, jsonify , request 
import mysql.connector
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 

#lista usuarios
@app.route('/usuarios', methods=['GET'] )
def lista_usuarios():
    db = mysql.connector.connect(
        host='localhost',
        user='root', #mi usuario
        password='Gds.1234', #mi contraseña
        database='usuarios_pcac' #nombre de la base de datos
    )
    
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    
    usuarios = cursor.fetchall()
    
    cursor.close()
    return jsonify(usuarios)


#borrar usuario
@app.route('/borrar/<int:id>', methods=['DELETE'] )
def borrar(id):
    db = mysql.connector.connect(
        host='localhost',
        user='root', #mi usuario
        password='Gds.1234', #mi contraseña
        database='usuarios_pcac' #nombre de la base de datos    
    )
    
    cursor = db.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = %s",(id,))
    db.commit() 
    cursor.close()
    return jsonify({"mensaje":"Usuario Borrado"})

#nuevo
@app.route('/nuevo', methods=['POST'] )
def agregar():
    info = request.json
    db = mysql.connector.connect(
        host='localhost',
        user='root', #mi usuario
        password='Gds.1234', #mi contraseña
        database='usuarios_pcac' #nombre de la base de datos
    )
    
    cursor = db.cursor()
    cursor.execute("INSERT INTO usuarios (email, nombre, localidad, pais, password) VALUES (%s,%s,%s,%s,%s)", (info["email"],info["nombre"],info["localidad"],info["pais"],info["password"]))
    db.commit() 
    cursor.close()
    return jsonify({"mensaje":"Nuevo usuario agregado!"})

# actualizar usuario
@app.route('/modificar/<int:id>', methods=['PUT'] )
def modificar(id):
    info = request.json
    db = mysql.connector.connect(
        host='localhost',
        user='root', #mi usuario
        password='Gds.1234', #mi contraseña
        database='usuarios_pcac' #nombre de la base de datos
    )
    
    cursor = db.cursor()
    #cursor.execute("UPDATE usuarios SET email= %s, nombre= %s, localidad= %s, pais= %s, password= %s WHERE id= %s", (info["email"],info["nombre"],info["localidad"],info["pais"],info["password"],id))
    cursor.execute("UPDATE usuarios SET email = %s, nombre = %s, localidad = %s, pais = %s, password = %s WHERE id = %s", (info["email"], info["nombre"], info["localidad"], info["pais"], info["password"], id))
    db.commit() 
    cursor.close()
    return jsonify({"mensaje":"MODIFICADO CON EXITO!"})


if __name__ == '__main__':
    app.run(debug=True)
