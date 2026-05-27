import math
import requests
from flask import render_template, request

def calcular():
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]


    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro: número negativo"
            etapas = f"Não existe raiz real de {num1}."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"
    else:
        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultados="",
            )
        num2 = float(num2_valor)


        if operacao == "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado}"

        elif operacao == "-":
            resultado = num1 - num2
            etapas = f"{num1} - {num2} = {resultado}"
        
        elif operacao == "*":
            resultado = num1 * num2
            etapas = f"{num1} * {num2} = {resultado}"

        elif operacao == "/":
            if num2 == 0:
                resultado = "Erro: divisão por zero"
                etapas = f"Não é possível dividir {num1} por zero."
            else:
                resultado = num1 / num2
                etapas = f"{num1} / {num2} = {resultado}"

        elif operacao == "**":
            resultado = math.pow(num1, num2)
            etapas = f"{num1} + {num2} = {resultado}"

        elif operacao == 'log':
            if num1 <= 0:
                resultado = "Erro: logaritmo de número não positivo"
                etapas = f"Não é possível calcular o logaritmo de {num1}."
            elif num2 <= 0 or num2 == 1:
                resultado = "Erro: base do logaritmo inválida"
                etapas = f"A base do logaritmo ({num2}) deve ser maior que 0 e diferente de 1."
            else:
                resultado = math.log(num1, num2)
                etapas = f"log_{num2}({num1}) = {resultado}"

    return render_template(
        "calculadora.html",
        etapas=etapas,
        resultados=resultado,
    )