#!/usr/bin/env python
import cgi

# Função para adição
def adicionar(x, y):
    return x + y

# Função para subtração
def subtrair(x, y):
    return x - y

# Função para multiplicação
def multiplicar(x, y):
    return x * y

# Função para divisão
def dividir(x, y):
    return x / y

# Obter dados do formulário
form = cgi.FieldStorage()
valor1 = float(form.getvalue('valor1'))
valor2 = float(form.getvalue('valor2'))
operacao = form.getvalue('operacao')

# Calcular o resultado
if operacao == 'soma':
    resultado = adicionar(valor1, valor2)
elif operacao == 'subtracao':
    resultado = subtrair(valor1, valor2)
elif operacao == 'multiplicacao':
    resultado = multiplicar(valor1, valor2)
elif operacao == 'divisao':
    resultado = dividir(valor1, valor2)

# Exibir o resultado na página
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Resultado da Calculadora</title>")
print("</head>")
print("<body>")
print("<h1>Resultado da Calculadora</h1>")
print("<p>Valor 1: %s</p>" % valor1)
print("<p>Valor 2: %s</p>" % valor2)
print("<p>Operação: %s</p>" % operacao)
print("<p>Resultado: %s</p>" % resultado)
print("</body>")
print("</html>")
