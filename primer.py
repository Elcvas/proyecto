from flask import Flask, redirect, url_for, render_template, request, session 
from pymongo import MongoClient
from datetime import date
import json

app = Flask(__name__)
app.secret_key = "hello"#Se debe crear una llave (key) con el nombre que sea
# FUNCION PARA ACCEDER AL JSON
def abrir():
    with open('data.json') as file:#abrimos el json como archivo
        data = json.load(file)#lo cargamos en la variable "data"
    return data#y retornamos esa variable con ese archivo
# CONEXION PARA USUARIOS
def conexion():
    data = abrir()#en "data" guardamos lo que nos retorna abrir() que es el JSON
    for y in data['con']:#recorremos lo que haya en "con" y con "y" accedemos a sus valores
        MONGO_URI = y['endpoint']#MONGO_URI va a ser = a lo que haya en "endpoint"
        client = MongoClient(MONGO_URI)#client va a ser = al host
        db = client[y['database']]#db va a ser = a la base de datos del host
        collection = db[y['coll']]#collection va a ser = de la base de datos, lo que haya en "coll"
        return collection#Retornamos la coleccion
# CONEXION PARA EDITORES 
def conexionEditores():
    data = abrir()#en "data" guardamos lo que nos retorna abrir() que es el JSON
    for y in data['con']:#recorremos lo que haya en "con" y con "y" accedemos a sus valores
        MONGO_URI = y['endpoint']#MONGO_URI va a ser = a lo que haya en "endpoint"
        client = MongoClient(MONGO_URI)#client va a ser = al host
        db = client[y['database']]#db va a ser = a la base de datos del host
        collection = db[y['colltres']]#collection va a ser = de la base de datos, lo que haya en "coll"
        return collection#Retornamos la coleccion
# CONEXION PARA ADMINISTRADORES 
def conexionAdmins():
    data = abrir()#en "data" guardamos lo que nos retorna abrir() que es el JSON
    for y in data['con']:#recorremos lo que haya en "con" y con "y" accedemos a sus valores
        MONGO_URI = y['endpoint']#MONGO_URI va a ser = a lo que haya en "endpoint"
        client = MongoClient(MONGO_URI)#client va a ser = al host
        db = client[y['database']]#db va a ser = a la base de datos del host
        collection = db[y['colldos']]#collection va a ser = de la base de datos, lo que haya en "coll"
        return collection#Retornamos la coleccion
# CONEXION PARA AVISOS 
def conexionAvisos():
    data = abrir()#en "data" guardamos lo que nos retorna abrir() que es el JSON
    for y in data['con']:#recorremos lo que haya en "con" y con "y" accedemos a sus valores
        MONGO_URI = y['endpoint']#MONGO_URI va a ser = a lo que haya en "endpoint"
        client = MongoClient(MONGO_URI)#client va a ser = al host
        db = client[y['database']]#db va a ser = a la base de datos del host
        collection = db[y['collcuatro']]#collection va a ser = de la base de datos, lo que haya en "coll"
        return collection#Retornamos la coleccion
# CONEXION PARA CONTROL 
def conexionControl():
    data = abrir()#en "data" guardamos lo que nos retorna abrir() que es el JSON
    for y in data['con']:#recorremos lo que haya en "con" y con "y" accedemos a sus valores
        MONGO_URI = y['endpoint']#MONGO_URI va a ser = a lo que haya en "endpoint"
        client = MongoClient(MONGO_URI)#client va a ser = al host
        db = client[y['database']]#db va a ser = a la base de datos del host
        collection = db[y['collcinco']]#collection va a ser = de la base de datos, lo que haya en "coll"
        return collection#Retornamos la coleccion
#ELIMINAR AVISOS POR FECHA PASADA
def eliminarAviso():
    collection = conexionAvisos()#en "collection" guardamos lo que me retorna "conexionAvisos()"
    fecha = date.today()#en "fecha" guardamos la fecha actual
    for x in collection.find():#recorremos la colección de avisos
        if str(fecha) > x['fecha_final']:#convertimos a string la fecha y comparamos si es mayor a la fecha final
            collection.delete_many({})#eliminamos la colección
#BUSCAR AVISOS DE TIPO RAPIDO
def avisos_Tipo_Rapido():
    collection = conexionAvisos()#en "collection" guardamos lo que retorna "conexionAvisos()"
    r = collection.find({'tipo':'rapido'}).sort('fecha_inicial',-1).limit(3)#en "r" guardamos las 3 ultimas colecciones de tipo "rapido"
    cot = []#creamos una lista
    for a in r:#recorremos esas colecciones
        cot.append(a)#las vamos almacenando en la lista "cot" que se creó
    return cot#y finalmente retornamos esa lista con las 3 colecciones
#BUSCAR AVISOS DE TIPO TRABAJO
def avisos_Tipo_Trabajo():
    collection = conexionAvisos()#en "collection" guardamos lo que retorna "conexionAvisos()"
    r = collection.find({'tipo':'trabajo'}).sort('fecha_inicial',-1).limit(3)#en "r" guardamos las 3 ultimas colecciones de tipo "trabajo"
    cot = []#creamos una lista
    for a in r:#recorremos esas colecciones
        cot.append(a)#las vamos almacenando en la lista que se creó
    return cot#y finalmente retornamos esa lista con las 3 colecciones
#BUSCAR AVISOS DE TIPO CONFERENCIA
def avisos_Tipo_Conferencia():
    collection = conexionAvisos()#en "collection" guardamos lo que retorna "conexionAvisos()"
    r = collection.find({'tipo':'conferencia'}).sort('fecha_inicial',-1).limit(3)#en "r" guardamos las 3 ultimas colecciones de tipo "conferencia"
    cot = []#creamos una lista
    for a in r:#recorremos esas colecciones
        cot.append(a)#las vamos almacenando en la lista que se creó
    return cot#y finalmente retornamos esa lista con las 3 colecciones
#BUSCAR AVISOS DE TIPO PROYECTO
def avisos_Tipo_Proyecto():
    collection = conexionAvisos()#en "collection" guardamos lo que retorna "conexionAvisos()"
    r = collection.find({'tipo':'proyecto'}).sort('fecha_inicial',-1).limit(3)#en "r" guardamos las 3 ultimas colecciones de tipo "proyecto"
    cot = []#creamos una lista
    for a in r:#recorremos esas colecciones
        cot.append(a)#las vamos almacenando en la lista que se creó
    return cot#y finalmente retornamos esa lista con las 3 colecciones
# ----------------------------    INDEX     -----------------------------
@app.route('/')
def index():
    eliminarAviso()#llamamos a la función "eliminarAviso()" para que compruebe si debe eliminar un aviso
    collection = conexionAvisos()#en collection guardamos lo que retorna "conexionAvisos()" que son los avisos
    rapido = avisos_Tipo_Rapido()#en "rapido" almacenamos los avisos de tipo "rapido"
    trabajo = avisos_Tipo_Trabajo()#en "trabajo" almacenamos los avisos de tipo "trabajo"
    conferencia = avisos_Tipo_Conferencia()#en "conferencias" almacenamos los avisos de tipo "conferencia"
    proyecto = avisos_Tipo_Proyecto()#y en "proyecto" almacenamos los avisos de tipo "proyecto"
    if "user" in session:#si hay una sesión llamada "user"
        user = session["user"]#almacenamos en user ese nombre 
        return render_template('index.html', usr=user, colle=collection,rap=rapido,tra=trabajo,con=conferencia,pro=proyecto)#y al correr el template index.html, le enviamos las variables declaradas
    else:
        return render_template('index.html', colle=collection,rap=rapido,tra=trabajo,con=conferencia,pro=proyecto)#de lo contrario, enviamos las variables excepto la del usuario porque quiere decir que no hay unas sesión
# ----------------------------    AVISOS RAPIDOS     -----------------------------
@app.route('/avisosrapidos')
def avisosrapidos():
    eliminarAviso()#llamamos a la función "eliminarAviso()" para que compruebe si debe eliminar un aviso
    collection = conexionAvisos()#en "collection" almacenamos lo que retorna "conexionAvisos()" que son los avisos
    collectiondos = conexionControl()#en "collectiondos" almacenamos lo que retorna "conexionControl()" 
    rapido = avisos_Tipo_Rapido()#en "rapido" almacenamos los avisos de tipo "rapido"
    trabajo = avisos_Tipo_Trabajo()#en "trabajo" almacenamos los avisos de tipo "trabajo"
    conferencia = avisos_Tipo_Conferencia()#en "conferencias" almacenamos los avisos de tipo "conferencia"
    proyecto = avisos_Tipo_Proyecto()#y en "proyecto" almacenamos los avisos de tipo "proyecto"
    if "user" in session:#si hay una session llamada "user"
        user = session["user"]#almacenamos en user ese nombre 
        return render_template('avisosrapidos.html', usr=user, colle=collection,colledos=collectiondos,rap=rapido,tra=trabajo,con=conferencia,pro=proyecto)#y al correr el template index.html, le enviamos las variables declaradas
    else:
        return render_template('avisosrapidos.html', colle=collection,rap=rapido,tra=trabajo,con=conferencia,pro=proyecto)#de lo contrario, enviamos las variables excepto la del usuario porque quiere decir que no hay unas sesión
# ----------------------------    TRABAJOS     -----------------------------
@app.route('/trabajos')
def trabajos():
    eliminarAviso()#llamamos a la función "eliminarAviso()" para que compruebe si debe eliminar un aviso
    collection = conexionAvisos()#en collection guardamos lo que retorna "conexionAvisos()" que son los avisos
    collectiondos = conexionControl()#en "collectiondos" almacenamos lo que retorna "conexionControl()" 
    rapido = avisos_Tipo_Rapido()#en "rapido" almacenamos los avisos de tipo "rapido"
    trabajo = avisos_Tipo_Trabajo()#en "trabajo" almacenamos los avisos de tipo "trabajo"
    conferencia = avisos_Tipo_Conferencia()#en "conferencias" almacenamos los avisos de tipo "conferencia"
    proyecto = avisos_Tipo_Proyecto()#y en "proyecto" almacenamos los avisos de tipo "proyecto"
    if "user" in session:#si hay una sesión llamada "user"
        user = session["user"]#almacenamos en user ese nombre 
        return render_template('trabajos.html', usr=user, colle=collection,colledos=collectiondos,rap=rapido,tra=trabajo,con=conferencia,pro=proyecto)#y al correr el template index.html, le enviamos las variables declaradas
    else:
        return render_template('trabajos.html', colle=collection,rap=rapido,tra=trabajo,con=conferencia,pro=proyecto)#de lo contrario, enviamos las variables excepto la del usuario porque quiere decir que no hay unas sesión
# ----------------------------    CONFERENCIAS     -----------------------------
@app.route('/conferencias')
def conferencias():
    eliminarAviso()#llamamos a la función "eliminarAviso()" para que compruebe si debe eliminar un aviso
    collection = conexionAvisos()#en collection guardamos lo que retorna "conexionAvisos()" que son los avisos
    collectiondos = conexionControl()#en "collectiondos" almacenamos lo que retorna "conexionControl()" 
    rapido = avisos_Tipo_Rapido()#en "rapido" almacenamos los avisos de tipo "rapido"
    trabajo = avisos_Tipo_Trabajo()#en "trabajo" almacenamos los avisos de tipo "trabajo"
    conferencia = avisos_Tipo_Conferencia()#en "conferencias" almacenamos los avisos de tipo "conferencia"
    proyecto = avisos_Tipo_Proyecto()#y en "proyecto" almacenamos los avisos de tipo "proyecto"
    if "user" in session:#si hay una sesión llamada "user"
        user = session["user"]#almacenamos en user ese nombre 
        return render_template('conferencias.html', usr=user, colle=collection,colledos=collectiondos,rap=rapido,tra=trabajo,con=conferencia,pro=proyecto)#y al correr el template index.html, le enviamos las variables declaradas
    else:
        return render_template('conferencias.html', colle=collection,rap=rapido,tra=trabajo,con=conferencia,pro=proyecto)#de lo contrario, enviamos las variables excepto la del usuario porque quiere decir que no hay unas sesión
# ----------------------------    PROYECTOS     -----------------------------
@app.route('/proyectos')
def proyectos():
    eliminarAviso()#llamamos a la función "eliminarAviso()" para que compruebe si debe eliminar un aviso
    collection = conexionAvisos()#en "collection" almacenamos lo que retorna "conexionAvisos()" que son los avisos
    collectiondos = conexionControl()#en "collectiondos" almacenamos lo que retorna "conexionControl()" 
    rapido = avisos_Tipo_Rapido()#en "rapido" almacenamos los avisos de tipo "rapido"
    trabajo = avisos_Tipo_Trabajo()#en "trabajo" almacenamos los avisos de tipo "trabajo"
    conferencia = avisos_Tipo_Conferencia()#en "conferencias" almacenamos los avisos de tipo "conferencia"
    proyecto = avisos_Tipo_Proyecto()#y en "proyecto" almacenamos los avisos de tipo "proyecto"
    if "user" in session:#si hay una sesión llamada "user"
        user = session["user"]#almacenamos en user ese nombre 
        return render_template('proyectos.html', usr=user, colle=collection,colledos=collectiondos,rap=rapido,tra=trabajo,con=conferencia,pro=proyecto)#y al correr el template index.html, le enviamos las variables declaradas
    else:
        return render_template('proyectos.html', colle=collection,rap=rapido,tra=trabajo,con=conferencia,pro=proyecto)#de lo contrario, enviamos las variables excepto la del usuario porque quiere decir que no hay unas sesión
# ----------------------------INICIAR SESION ALUMNOS-----------------------------
@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":#si se envia por POST
        if request.form["iniciar"] != None:#si presionó en el botón "iniciar"
            collection = conexion()#en "collection" guardamos lo que retorna "conexion()"
            user = request.form["user"]#en "user" guardamos lo que recibimos por "user" del formulario
            passwd = request.form["passwd"]#en "passwd" guardamos lo que recibimos por "passwd" del formulario
            for x in collection.find():#recorremos la colección a la que se haya hecho la conexión
                if (x['correo'] == user and x['contraseña'] == passwd):#si el usuario y la contraseña que recibimos del formulario son iguales a las de la colección
                    session["user"] = user#guardamos en 'session["user"]' el usuario que nos haya pasado por el formulario
                    n = x['_id']#en "n" el id del usuario
                    session["aidi_usu"] = str(n)#en 'session["aidi_usu"]' convertimos ese id a string
                    return redirect(url_for("index"))#y redirijimos al index
        return render_template('login.html', err=1)#si no se cumple la condicion cargamos el index.html con una variable "err" = 1
    else:#si no ha mandado nada por POST 
        return render_template('login.html')#solo cargamos el login.html
# ----------------------------INICIAR SESION EDITORES-----------------------------
@app.route('/login-editor', methods=["POST", "GET"])
def loginEditor():
    if request.method == "POST":#si se envia algo por POST
        if request.form["iniciar"] != None:#si presionó en el botón "iniciar"
            collection = conexionEditores()#en "collection" guardamos lo que retorna "conexionEditores()"
            usuario = request.form["usuarioeditor"]#en "usuario" almacenamos lo que llega del formulario como "usuarioeditor"
            contra = request.form["contraeditor"]#en "contra" almacenamos lo que llega del formulario como "contraeditor"
            for x in collection.find():#recorremos la colección de editores
                if (x['usuario'] == usuario and x['contraseña'] == contra):#si el usuasrio de la colección es = a usuario y contraseña es= a la contra que llego del formulario
                    session["editor"] = usuario#almacenamos en una 'session["editor"]' el usuario que llego del formulario
                    return render_template('editores.html',usu=x['nombre'])#y enviamos el nombre del usuarioEditor
        return render_template('editores.html',usu=x['nombre'])
    else:
        return render_template('editores.html')#si no se ha enviado nada por POST solo cargamos editores.html
# ----------------------------INICIAR SESION ADMINS-----------------------------
@app.route('/login-admin', methods=["POST", "GET"])
def loginAdmin():
    if request.method == "POST":#si se envia algo por POST
        if request.form["iniciar"] != None:#si presiono en el botón "iniciar"
            collection = conexionAdmins()#en "coleccion" almacenamos lo que retorna en "conexionAdmins()" 
            usuario = request.form["usuarioadmin"]#en "usuario" almacenamos lo que llega del formulario como "usuarioadmin"
            contra = request.form["contraadmin"]#en "contra" almacenamos lo que llega del formulario como "contraadmin"
            for x in collection.find():#recorremos la colecion de los administradores
                if (x['usuario'] == usuario and x['contra'] == contra):#y si el usuario es= el usuario del form y contra es = a la contra del form
                    session["admin"] = usuario#guardamos en 'una session["admin"]' el usuario del administrador
                    return render_template('administradores.html')#y cargamos administradores.html
        return render_template('administradores.html')
    else:
        return render_template('administradores.html')#si no se ha enviado nada por POST solo cargamos administradores.html
# ----------------------------ALTA AVISOS-----------------------------   
@app.route('/alta-avisos', methods=["POST", "GET"])
def altaAvisos():
    if request.method == "POST":#si se envia algo por POST
        if request.form["alta-aviso"] != None:#si presionó en el botón "alta-aviso"
            collection = conexionAvisos()#en "collection" almacenamos lo que retorna en "conexionAvisos()" 
            titulo = request.form["titulo"]#"titulo" será = a lo que llega por "titulo"
            tipo = request.form["tipo"]#"tipo" será = a lo que llega por "tipo"
            descripcion = request.form["descripcion"]#"descripcion" será = a lo que llega por "descripcion"
            fecha_inicial = request.form["fecha_inicial"]#"fecha_inicial" será = a lo que llega por "fecha_inicial"
            fecha_final = request.form["fecha_final"]#"fecha_final" será = a lo que llega por "fecha_final"
            editor = request.form["editor"]#"editor" será = a lo que llega por "editor"
            coll = {'titulo': titulo,'tipo':tipo,'descripcion':descripcion,'fecha_inicial':fecha_inicial,'fecha_final':fecha_final,'editor':editor}#"coll" será = a una colección con su llave - valor de lo que vamos a almacenar
            collection.insert_one(coll)#insertamos en la colección de avisos
            return render_template('editores.html')#cargamos editores.html
    return render_template('editores.html')#cargamos editores.html
# ----------------------------MODIFICAR AVISOS-----------------------------
@app.route('/modificaravisos', methods=["POST", "GET"])
def modificaravisos():
    if request.method == "POST":#si se envia algo por POST
        collection = conexionAvisos()#"collection" será = lo que retorna "conexionAvisos()"
        titulo = request.form["titulo"]#"titulo" será = lo que llega por "titulo"
        tipo = request.form["tipo"]#"tipo" será = lo que llega por "tipo"
        descripcion = request.form["descripcion"]#"descripcion" será = lo que llega por "descripcion"
        fecha_inicial = request.form["fecha_inicial"]#"fecha_inicial" será = lo que llega por "fecha_inicial"
        fecha_final = request.form["fecha_final"]#"fecha_final" será = lo que llega por "fecha_final"
        editor = request.form["editor"]#"editor" será = lo que llega por "editor"
        if request.form.get("modaviso"):#Si "presionó" en "modaviso"
            collmod = {'editor':editor}#"collmod" será = al editor
            collection.update_one(collmod, {"$set": {'titulo': titulo, 'tipo':tipo, 'descripcion':descripcion,'fecha_inicial':fecha_inicial,'fecha_final':fecha_final}})#y se actualiza el titulo, tipo, descripcion, fecha_inicial y fecha_final con el editor que le pasamos
            return redirect(url_for("loginEditor"))#y redirijimos al ednpoint "logineditor"
        elif request.form.get("bajaaviso"):#de lo contrario si presionó en "bajaaviso"
            collbaja = {'titulo': titulo}#igual almacenamos el "titulo"
            collection.delete_one(collbaja)#y eliminamos esa colección con ese titulo que le hayamos pasado
            return redirect(url_for("loginEditor"))#y redirijimos a "loginEditor"
# ----------------------------CERRAR SESION-----------------------------
@app.route('/logout')
def logout():
    if 'user' in session:#si hay una sesión "user"
        session.pop('user')#la eliminamos
        return redirect(url_for('login'))#y redirijimos al endpoint "login"
    if 'editor' in session:#si hay una sesión "editor"
        session.pop('editor')#la borramos
        return redirect(url_for('loginEditor'))#y redirijimos a "loginEditor"
    if 'admin' in session:#si hay una sesión "admin"
        session.pop('admin')#la borramos
        return redirect(url_for('loginAdmin'))#y redirijimos a "loginAdmin"
#----------------------------REGISTRO USUARIOS-----------------------------
@app.route('/add', methods=["POST", "GET"])
def add():
    if request.method == "POST":#si se envia algo por POST
        if request.form["registro"] != None:#si presionó en "registro"
            collection = conexion()#"collection" será = a lo que retorna "conexion()"
            nombre = request.form["nombre"]#"nombre" será = a lo que llega de "nombre"
            apellidos = request.form["apellido"]#"apellidos" será = a lo que llega de "apellidos"
            turno = request.form["turno"]#"turno" será = a lo que llega de "turno"
            codigo = request.form["codigo"]#"codigo" será = a lo que llega de "codigo"
            correo = request.form["correo"]#"correo" será = a lo que llega de "correo"
            passwd = request.form["passwd"]#"passwd" será = a lo que llega de "passwd"
            coll = {'nombre': nombre, 'apellidos': apellidos, 'turno': turno,
                    'codigo_alumno': codigo, 'correo': correo, 'contraseña': passwd}#"coll" será = una coleccion con sus llave - valor de las variables
            collection.insert_one(coll)#insertamos esa coleccion en usuarios
            session["user"] = correo#almacenamos en session["user"] el correo 
            return redirect(url_for("index"))#y redireccionamos a index
# ----------------------------    ADMINS    -----------------------------
@app.route('/admins', methods=["POST", "GET"])
def admins():
    if request.method == "POST":#si se envia algo por POST
        if request.form.get('btnalta') == 'ALTA':#si presionó en el boton "btnalta"
            return render_template('administradores.html', alt="mostraralta")#carga administradores.html y enviamos el valor "mostraralta"
        elif request.form.get('btnbuscar') == 'BUSCAR':#de lo contrario si presionó "btnbuscar"
            collection = conexionEditores()#"collection" será = a la colección de editores
            return render_template('administradores.html', bus="mostrareditor",coll=collection)#y al cargar administradores.html enviamos "mostraralta" y la colección
    return render_template('administradores.html')#cargamos administradores.html
# ----------------------------    EDITORES    -----------------------------
@app.route('/editores', methods=["POST", "GET"])
def editores():
    if request.method == "POST":#si se envia algo por POST
        if request.form.get('btnalta') == 'ALTA':#si presionó en el boton "btnalta"
            collectiondos = conexionEditores()#"collectiondos" será = a la colección de editores
            return render_template('editores.html', alt="mostraralta",colle=collectiondos)#cargamos editores.html y enviamos "mostraralta" y la colección de editores
        elif request.form.get('btnbuscar') == 'BUSCAR':#de lo contrario si presionó "btnbuscar"
            collection = conexionAvisos()#"collection" será = a la colección de avisos
            return render_template('editores.html', bus="mostrareditor",coll=collection)#y cargamos editores.html y enviamos "mostrareditor" y la colección de avisos
    return render_template('editores.html')#cargamos editores.html
# ----------------------------ALTA EDITORES-----------------------------
@app.route('/altaeditor', methods=["POST", "GET"])
def altaeditor():
    if request.method == "POST":#si se envia algo por POST
        if request.form["altaeditor"] != None:#si presionó en el boton "alteditor"
            collection = conexionEditores()#"collection" será = a la colección de editores
            nombre = request.form["nombre"]#"nombre" será = a lo que llega de "nombre"
            puesto = request.form["puesto"]#"puesto" será = a lo que llega de "puesto"
            contacto = request.form["contacto"]#"contacto" será = a lo que llega de "contacto"
            usuario = request.form["usuario"]#"usuario" será = a lo que llega de "usuario"
            contra = request.form["passwd"]#"passwd" será = a lo que llega de "passwd"
            coll = {'usuario': usuario, 'contraseña': contra,
                    'nombre': nombre, 'puesto': puesto, 'contacto': contacto}#"coll" será = las llave - valor de usuario, contraseña, nombre, puesto y contacto
            collection.insert_one(coll)#insertamos esas llaves y valores
            return redirect(url_for("admins"))#redirijimos a admins
# ----------------------------BUSCAR EDITORES-----------------------------
@app.route('/buscareditor', methods=["POST", "GET"])
def buscareditor():
    if request.method == "POST":#si se envia algo por POST
        if request.form["buscar"] != None:#si presionó en "buscar"
            collection = conexionEditores()#"collection" será = la colección de editores
            try:
                usuarioeditor = request.form["buscareditor"]#"usuarioeditor" será = a lo que llega de "buscareditor"
            except:
                return render_template('administradores.html', coll=collection)#cargamos administradores.html y enviamos la colección de editores
            for x in collection.find():#iteramos esa colección de editores
                if (x['usuario'] == usuarioeditor):#y si el usuario existe
                    nombre = x['nombre']#"nombre" será = a lo que llega de "nombre"
                    puesto = x['puesto']#"puesto" será = a lo que llega de "puesto"
                    contacto = x['contacto']#"contacto" será = a lo que llega de "contacto"
                    usuario = x['usuario']#"usuario" será = a lo que llega de "usuario"
                    contra = x['contraseña']#"contraseña" será = a lo que llega de "contraseña"
                    return render_template('administradores.html', bus="mostrareditor", nom=nombre, pues=puesto, conta=contacto, usu=usuario, contra=contra,coll=collection)#cargamos administradores.html y enviamos las variables previamente declaradas
# ----------------------------BUSCAR AVISOS-----------------------------
@app.route('/buscaraviso', methods=["POST", "GET"])
def buscaraviso():
    if request.method == "POST":#si se envia algo por POST
        if request.form["buscar"] != None:#si presionó en "buscar"
            collection = conexionAvisos()#"collection" será = a la colección de avisos
            try:
                tituloaviso = request.form["buscaraviso"]#"tituloaviso" será = a "buscaraviso"
            except:
                return render_template('editores.html', coll=collection)#cargamos editores.html y enviamos la colección de avisos
            for x in collection.find():#iteramos esa colección de avisos
                if x['titulo'] == tituloaviso:#y si el titulo existe
                    titulo = x['titulo']#"titulo" será = a lo que llega de "titulo"
                    tipo = x['tipo']#"tipo" será = a lo que llega de "tipo"
                    descripcion = x['descripcion']#"descripcion" será = a lo que llega de "descripcion"
                    fecha_inicial = x['fecha_inicial']#"fecha_inicial" será = a lo que llega de "fecha_inicial"
                    fecha_final = x['fecha_final']#"fecha_final" será = a lo que llega de "fecha_final"
                    editor = x['editor']#"editor" será = a lo que llega de "editor"
                    return render_template('editores.html', bus="mostrareditor", tit=titulo, tip=tipo, des=descripcion, fechi=fecha_inicial, fechf=fecha_final,edi=editor,coll=collection)#cargamos editores.html enviando las variables previamente declaradas
# ----------------------------MODIFICAR EDITORES-----------------------------
@app.route('/modificareditor', methods=["POST", "GET"])
def modificareditor():
    if request.method == "POST":#verificamos si envió algo por POST
        collection = conexionEditores()#en "collection" almacenamos lo que retorna "conexioneEditores()" 
        nombre = request.form["nombre"]#en "nombre" almacenamos lo que llega por "nombre"
        puesto = request.form["puesto"]#en "puesto" almacenamos lo que llega por "puesto"
        contacto = request.form["contacto"]#en "contacto" almacenamos lo que llega por "contacto"
        usuario = request.form["usuario"]#en "usuario" almacenamos lo que llega por "usuario"
        contra = request.form["passwd"]#en "passwd" almacenamos lo que llega por "passwd"
        if request.form.get("modeditor"):#si presionó en "modeitor"
            collmod = {'usuario':usuario}#"collmod" será = al usuario
            collection.update_one(collmod, {"$set": {'nombre': nombre, 'puesto':puesto, 'contacto':contacto,'contraseña':contra}})#actualizamos la colección donde el usuario sea = al usuario que almacenamos en "collmod" y si es así, se actualiza el nombre, puesto, contacto y contraseña
            return redirect(url_for("admins"))#y redirijimos al endpoint de admins
        elif request.form.get("bajaeditor"):#de lo contrario si presionó "bajaeditor"
            collbaja = {'usuario': usuario}#"collbaja" será = al usuario
            collection.delete_one(collbaja)#eliminamos esa colección que tenga ese usuario
            return redirect(url_for("admins"))#y redirijimos al endpoint admins
# ----------------------------CONTROL LIKES-----------------------------
@app.route('/control_likes', methods=["POST", "GET"])
def control_likes():
    if request.method == 'POST':#verificamos si envió algo por POST
        if request.form.get('diolike') != None:#luego verificamos si presiono en 'diolike'
            collection = conexionAvisos()#en "collection" almacenamos lo que retorna "conexionAvisos()"
            collectiondos = conexionControl()#y en "collectiondos" lo que retorna "conecionControl()"
            id_aviso = request.form['aidi']#en "id_aviso" almacenamos lo que recibamos de "aidi"
            id_usu = session["aidi_usu"]#en "id_usu" almacenmaos lo que hay en "session['aidi_usu']"
            colle = {'id_aviso':id_aviso,'id_usuario':id_usu}#"colle" será donde almacenamos el id_aviso y el id_usuario
            collectiondos.insert_one(colle)#insertamos en la colección control lo que tenga "colle"
            for x in collection.find():#iteramos la colección de avisos
                if str(x['_id']) == id_aviso:#si el id del aviso de la colección es igual al id del aviso que se leyo anteriormente
                    if x['tipo'] == 'rapido':#y si el tipo de aviso de la colección es = a 'rapido'
                        return redirect(url_for('avisosrapidos',colle=collection,colledos=collectiondos))#redirijimos a la misma página
                    elif x['tipo'] == 'trabajo':#y si el tipo de aviso de la colección es = a 'trabajo'
                        return redirect(url_for('trabajos',colle=collection,colledos=collectiondos))#redirijimos a la misma página
                    elif x['tipo'] == 'conferencia':#y si el tipo de aviso de la colección es = a 'conferencia'
                        return redirect(url_for('conferencias',colle=collection,colledos=collectiondos))#redirijimos a la misma página
                    elif x['tipo'] == 'proyecto':#y si el tipo de aviso de la colección es = a 'proyecto'
                        return redirect(url_for('proyectos',colle=collection,colledos=collectiondos))#redirijimos a la misma página
        if request.form.get('diodislike') != None:#si presiono en 'diodislike'
            collection = conexionAvisos()#en "collection" almacenamos lo que retorna "conexionAvisos()"
            collectiondos = conexionControl()#y en "collectiondos" lo que retorna "conecionControl()"
            id_aviso = request.form['aidi']#en "id_aviso" almacenamos lo que recibamos de "aidi"
            id_usu = session["aidi_usu"]#en "id_usu" almacenmaos lo que hay en "session['aidi_usu']"
            colle = {'id_aviso':id_aviso,'id_usuario':id_usu}#"colle" será donde almacenamos el id_aviso y el id_usuario
            collectiondos.delete_one(colle)#eliminamos en la colección control lo que tenga "colle"
            for x in collection.find():#iteramos la colección de avisos
                if str(x['_id']) == id_aviso:#si el id del aviso de la colección es igual al id del aviso que se leyo anteriormente
                    if x['tipo'] == 'rapido':#y si el tipo de aviso de la colección es = a 'rapido'
                        return redirect(url_for('avisosrapidos',colle=collection,colledos=collectiondos))#redirijimos a la misma página
                    elif x['tipo'] == 'trabajo':#y si el tipo de aviso de la colección es = a 'trabajo'
                        return redirect(url_for('trabajos',colle=collection,colledos=collectiondos))#redirijimos a la misma página
                    elif x['tipo'] == 'conferencia':#y si el tipo de aviso de la colección es = a 'conferencia'
                        return redirect(url_for('conferencias',colle=collection,colledos=collectiondos))#redirijimos a la misma página
                    elif x['tipo'] == 'proyecto':#y si el tipo de aviso de la colección es = a 'proyecto'
                        return redirect(url_for('proyectos',colle=collection,colledos=collectiondos))#redirijimos a la misma página
        return redirect(url_for('index'))#redirijimos a index
    return render_template('index.html')#cargamos el indes.html
# ----------------------------DIRECTORIO-----------------------------
@app.route('/directorio')
def directorio():
    return render_template('directorio.html')#cargamos directorio.html

if __name__ == "__main__":
    app.run(debug=True)