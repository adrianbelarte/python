import random

# Función para crear un mazo de cartas
def crear_mazo():
    mazo = []
    valores = [2,3,4,5,6,7,8,9,10,10,10,11]
    for _ in range(4): # cuatro palos
        for valor in valores:
            mazo.append(valor)
    
    random.shuffle(mazo) #Baraja el mazo
    return mazo

# Función para calcular el puntaje de una mano
def calcular_puntaje(mano):
    total = sum(mano)
    #Ajustar el As
    for carta in mano:
        if total > 21 and carta == 11:
            total -= 10
    return total

#Función para repartir cartas
def repartir_cartas(mazo):
    jugador = [mazo.pop(), mazo.pop()]
    casa = [mazo.pop(), mazo.pop()]
    return jugador, casa

def iniciar_partida():
    mazo = crear_mazo()
    jugador, casa = repartir_cartas(mazo)

    # Mostrar cartas
    print(f"Cartas del jugador: {jugador}, Puntaje: {calcular_puntaje(jugador)}")
    print(f"Cartas de la casa: {casa[0]}, [Carta oculta]")

    # Turno jugador
    while calcular_puntaje(jugador) < 21:
        accion = input("¿Quieres pedir carta(p) o plantarse(s)?").lower()
        if accion == "p":
            jugador.append(mazo.pop())
            print(f"Cartas del jugador: {jugador}, Puntaje: {calcular_puntaje(jugador)}")
        elif accion == "s":
            break
    
    # Turno de la casa
    while calcular_puntaje(casa) < 17:
        casa.append(mazo.pop())
    
    print(f"Cartas de la casa: {casa}, Puntaje: {calcular_puntaje(casa)}")

    # Determinar el ganador

    puntaje_jugador = calcular_puntaje(jugador)
    puntaje_casa = calcular_puntaje(casa)

    if puntaje_jugador > 21:
        print("¡Te has pasado de 21! La casa gana.")
    elif puntaje_casa > 21 or puntaje_jugador > puntaje_casa:
        print("¡El jugador gana!")
    else:
        print("¡La casa gana!")
    

# Iniciar el juego
iniciar_partida()
