from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    #dados que serao! calculados python
    titulo_pagina = "Face Page"
    aluno = {"nome": "João", "curso": "Python", "nota": 4.5}
    status = "Aprovado" if aluno["nota"] >= 5 else "Reprovado"
    #passando dados para o template HTML
    return render_template("index.html", 
                           titulo=titulo_pagina, 
                           usuario=aluno, 
                           resultado=status)
if __name__ == "__main__":
    app.run(debug=True)