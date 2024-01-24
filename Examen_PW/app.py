from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    nombre= None
    edad= None
    total= None
    total_des= None
    des= None
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        vtarro=9000
        total=tarros*vtarro
        if edad>=18 and edad<=30:
            des=total*0.15
        elif edad>30:
            des=total*0.25
        else:
            des=0
        total_des=total-des
    return render_template('ejercicio1.html', nombre=nombre, edad=edad, total=total, total_des=total_des, des=des)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    error = None
    mensaje= None
    usuarios={'juan':{'contraseña':'admin', 'rol':'administrador'}, 'pepe':{'contraseña':'user', 'rol':'usuario'}}
    if request.method == 'POST':
        usuario= request.form['usuario']
        contraseña= request.form['contraseña']
        if usuario in usuarios and contraseña == usuarios[usuario]['contraseña']:
            mensaje= 'Bienvenido {} {}'.format(usuarios[usuario]['rol'], usuario)
        else:
             error= 'Usuario o contraseña incorrecta.'

    return render_template('ejercicio2.html', error=error, mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)