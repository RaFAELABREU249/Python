from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <div style="font-family: sans-serif; text-align: center; margin-top: 50px;">
        <h1>Bem-vindo ao Gerador de Currículos!</h1>
        <p>Clique no link abaixo para visualizar o perfil profissional:</p>
        <a href="/curriculo" style="display: inline-block; background: #2980b9; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">Ver Currículo de Mentirinha</a>
    </div>
    """

@app.route("/curriculo")
def curriculo():
    return render_template("curriculo.html")

if __name__ == '__main__':
    app.run(debug=True)
