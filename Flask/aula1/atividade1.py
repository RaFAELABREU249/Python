from flask import Flask

app = Flask(__name__)

@app.route ("/decorator")
def conceitos():
    return "Decorators em Python são funções que modificam ou estendem o comportamento de outras funções, métodos ou classes sem alterar seu código original. " \
    "Eles atuam como embalagens inteligentes (wrappers), permitindo executar ações antes ou depois da função principal, ideal para logging, controle de acesso ou medição de " \
    "performance."

if __name__ == '__main__':
    app.run(debug=True)