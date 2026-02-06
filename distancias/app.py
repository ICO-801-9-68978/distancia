from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calcular_distancia():
    distancia = None
    if request.method == 'POST':
        # Obtener datos del formulario
        x1 = float(request.form.get('x1'))
        y1 = float(request.form.get('y1'))
        x2 = float(request.form.get('x2'))
        y2 = float(request.form.get('y2'))
        
        # Lógica de la fórmula
        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        distancia = round(distancia, 2)

    return render_template('layout.html', distancia=distancia)

if __name__ == '__main__':
    app.run(debug=True)
