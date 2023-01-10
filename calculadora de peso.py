# calculadora de IMC
# IMC = / (Altura x altura)
# < 19: delgadez
# entre 20 y 25 normal
# entre 26 y 30 sobre peso
# > de 30: obesidad

def calcularIMC(peso, alturaEnMetros):
    imc = peso / alturaEnMetros * alturaEnMetros
    return imc

def pedirIMC():

peso = int(input('ingrese su peso en kg'))
alturaEnCM = int(input('ingrse su altura  en cm'))
alturaEnMetros = alturaEnCM / 100
imc = calcularIMC(peso, alturaEnMetros)

print('su IMC es de ' + str(imc))

if imc < 20:
    print('estado de delgadez')
if imc >= 20 and imc < 26:
    print('peso normal')
if imc >= 26 and imc < 30:
    print('estado de sobre peso')pesó 
if imc >=30:
    print('estado de obesidad')