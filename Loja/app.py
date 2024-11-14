from flask import Flask, render_template, request, redirect
from db import login

app = Flask(__name__)
user = {}

@app.route('/')
def index():
    return render_template('login.html', e=False)

@app.route("/logar", methods=['POST'])
def logar():
    global user

    usuario = request.form["id"]
    senha = request.form["senha"]

    user = login(usuario, senha)

    if "erro" in user:
        return render_template('login.html', e=True)
    else:
        return redirect('/fabrica')
    

if __name__ == '__main__':
    app.run(debug=True)