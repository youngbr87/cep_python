from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cep = request.form['cep']
        url = f'https://viacep.com.br/ws/{cep}/json/'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return render_template('result.html', data=data)
        return render_template('index.html', error='CEP não encontrado')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)