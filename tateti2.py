import random

tablero = [" "] * 9\

def mostrartablero():
    print(tablero[0],"|",tablero[1],"|",tablero[2])
    print("--------")
    print(tablero[3],"|",tablero[4],"|",tablero[5])
    print("--------")
    print(tablero[6],"|",tablero[7],"|",tablero[8])

def ganador(J):
    return(
    (tablero[0]==tablero[1]==tablero[2]==J) or
    (tablero[3]==tablero[4]==tablero[5]==J) or
    (tablero[6]==tablero[7]==tablero[8]==J) or
    (tablero[0]==tablero[3]==tablero[6]==J) or
    (tablero[1]==tablero[4]==tablero[7]==J) or
    (tablero[2]==tablero[7]==tablero[8]==J) or
    (tablero[0]==tablero[4]==tablero[8]==J) or
    (tablero[2]==tablero[4]==tablero[6]==J) 
    )

while True: 
    
    mostrartablero()
    jugada = int(input("Dime un numero del 1 al 9:")) - 1
    if tablero[jugada] != " ":
        print("Lugar ocupado")
        continue

    tablero[jugada] = "X"

    if ganador("X"):
       mostrartablero()
       print("Ganaste")
       break
   
    if " " not in tablero:
        print("Empate")
    
    while True:
        compu = random.randint(0,8)
        if tablero[compu] == " ":
           tablero[compu] = "O"
           break
    
    if ganador("O"):
       mostrartablero()
       print("Perdiste")
       break
        