import os
def main():
    os.system("clear")
    angulo = int(input("Tamaño del Ángulo: "))
    if angulo < 90:
        print("El angulo es Agudo")
    elif angulo == 90:
        print("El angulo es Recto")
    elif angulo > 90 and angulo < 180:
        print("El angulo es Obtuso")
    elif angulo == 180:
        print("El angulo es Llano")
    elif angulo>180 and angulo<360:
        print("El angulo es Cóncavo")
        
if __name__=='__main__':
    main()
