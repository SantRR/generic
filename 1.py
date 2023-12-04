import random
import numpy
from collections import Counter


def ConvertirDadoACarta(dado):
    if dado==1:
        dado="9"
    elif dado==2:
        dado="10"
    elif dado==3:
        dado="J"
    elif dado==4:
        dado="Q"
    elif dado==5:
        dado="K"
    else:
        dado="A"
    return dado

def ConvertirCartaADado(dado):
    if dado == "9":
        dado=1
    elif dado == "10":
        dado=2
    elif dado == "J":
        dado=3
    elif dado == "Q":
        dado=4
    elif dado == "K":
        dado=5
    else:
        dado =6
    return dado

def ReRollear(cubilete):
    cuantos = int(input("¿Cuantos dados desea cambiar hasta un máximo de 4? "))
    if cuantos > 0 and cuantos <= 4:
        dadosElegidos = [] 
        for i in range(0,cuantos):
            numeroDado = int(input(f"¿Qué número de dado desea cambiar (1-5)? "))
            if numeroDado >= 1 and numeroDado <= 5 and numeroDado not in dadosElegidos:
                nuevoDado = random.randint(1, 6)
                cubilete[numeroDado - 1] = ConvertirDadoACarta(nuevoDado)
                dadosElegidos.append(numeroDado)
            elif numeroDado in dadosElegidos:
                print("Este dado ya ha sido seleccionado. Elija otro número.")
            else:
                print("Número de dado fuera de rango. Debe ser entre 1 y 5.")
    else:
        print("La cantidad de dados a cambiar debe estar entre 1 y 4.")
    print("Nuevo cubilete:", cubilete)
    return cubilete

def GenerarCubilete():
    cubilete=[]
    for i in range(0,5):
        dado=random.randint(1,6)
        print(dado)
        dadoconvertido=ConvertirDadoACarta(dado)
        print(dadoconvertido)
        cubilete.append(dadoconvertido)
    print(cubilete)
    respuesta=int(input("Desea cambiar algun dado?: Escriba 1 para si, Escriba 2 para no: "))
    if respuesta==1:
        cubilete=ReRollear(cubilete)
        print(cubilete)
    return cubilete

def CrearJugadores(numero_jugadores):
    jugadores=[]
    for i in range(0, numero_jugadores):
        nombre_jugador = input(f"Introduce tu nombre, jugador #{i + 1}: ")
        credito_jugador = float(input("Introduce la cantidad de creditos a utilizar: "))
        if credito_jugador <= 0:
            print("Cantidad invalida, intente nuevamente")
            credito_jugador = float(input("Introduce la cantidad de creditos a utilizar: "))
        jugador = [nombre_jugador, credito_jugador]
        jugadores.append(jugador)
    return jugadores

def ChecarValorApuesta(lista_jugadores):
    for i in range(0, len(lista_jugadores)):
        if lista_jugadores[i][1] <= 0:
            print(f"el jugador numero {i} no puede apostar porque su credito es menor o igual a cero")
            print(f"el jugador numero {i} sera expulsado del casino")
            lista_jugadores.pop(i)
    return lista_jugadores

def VerificarFrecuencia(cubilete):
    valores = []
    for carta in cubilete:
        valor_carta = ConvertirCartaADado(carta)
        valores.append(valor_carta)
    contador = Counter(valores)
    print(contador)
    tiene_poker = ChecarPoker(contador)
    tiene_quintilla = ChecarQuintilla(contador)
    tiene_tercia=ChecarTercia(contador)
    tiene_fullhouse=False
    if tiene_tercia==True:
        tiene_fullhouse=ChecarFullHouse(contador)
        if tiene_fullhouse==True:
            tiene_tercia=False
    if tiene_quintilla:
        valor_quintilla = ValorQuintilla(contador)
        print("El cubilete tiene una quintilla con el valor ",  ConvertirDadoACarta(valor_quintilla))
    elif tiene_poker:
        valor_poker = ValorPoker(contador)
        print("El cubilete tiene un poker con el valor ", ConvertirDadoACarta(valor_poker))
    elif tiene_fullhouse:
        valor_fullhouseTercia=ValorFullHouseTercia(contador) 
        valor_fullhousePar=ValorFullHousePar(contador)
        print("El cubilete tiene un fullhouse con el valor de la tercia de  ", ConvertirDadoACarta(valor_fullhouseTercia), " y el valor del par de: ", ConvertirDadoACarta(valor_fullhousePar))
    elif tiene_tercia:
        valor_tercia=ValorTercia(contador)
        print("El cubilete tiene una tercia de ", ConvertirDadoACarta(valor_tercia))
    else:  
        print("La función todavia no esta definida")
    return None

def ChecarPoker(contador):
    for valor, cantidad in contador.items():
        if cantidad == 4:
            return True
    return False

def ValorPoker(contador):
    for valor, cantidad in contador.items():
        if cantidad == 4:
            return valor
    return None

def ChecarQuintilla(contador):
    for valor, cantidad in contador.items():
        if cantidad == 5:
            return True
    return False

def ValorQuintilla(contador):
    for valor, cantidad in contador.items():
        if cantidad == 5:
            return valor
    return None

def ChecarTercia(contador):
    for valor, cantidad in contador.items():
        if cantidad == 3:
            return True
    return False

def ValorTercia(contador):
    for valor, cantidad in contador.items():
        if cantidad == 3:
            return valor
    return None

def ChecarFullHouse(contador):
    tercia = False
    par = False
    for valor, cantidad in contador.items():
        if cantidad == 3:
            tercia = True
        if cantidad == 2:
            par = True
    if tercia==True and par==True:
        return True
    return False

def ValorFullHouseTercia(contador):
    for valor, cantidad in contador.items():
        if cantidad == 3:
            return valor
    return None  

def ValorFullHousePar(contador):
    for valor, cantidad in contador.items():
        if cantidad == 2:
            return valor
    return None  

#Programa principal
cubilete1=[]
#cubilete1=GenerarCubilete();
cubilete_ejemplo = ['9', '9', '9', '9', '9']
cubilete_ejemplo2 = ['J', 'J', 'K', 'J', 'J']
cubilete_ejemplo3 = ['J', 'K', 'K', 'J', 'J']
cubilete_ejemplo4 = ['J', 'K', 'Q', 'Q', 'Q']
cubilete_ejemplo5 = ['J', 'K', 'Q', 'J', 'K']
VerificarFrecuencia(cubilete_ejemplo)
VerificarFrecuencia(cubilete_ejemplo2)
VerificarFrecuencia(cubilete_ejemplo3)
VerificarFrecuencia(cubilete_ejemplo4)
VerificarFrecuencia(cubilete_ejemplo5)

jugadores = 0
jugar = True
while jugar == True:
    while jugadores <= 0:
        quierenJugar = int(input("no hay jugadores actualmente, quieren jugar? (1/0): "))
        if quierenJugar == 0:
            exit()
        else:
            jugadores = int(input("cuantos jugadores seran?: "))
            listaJugadores = CrearJugadores(jugadores)
            break
    cubilete = GenerarCubilete()
    ChecarValorApuesta(listaJugadores)