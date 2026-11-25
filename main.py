opcion = 0
while opcion != 7:
    print("\n--- MENÙ DEL RESTAURANTE ---")
    print("1. Hamburguesa Doble Carne")
    print("2. Perro Caliente Especial")
    print("3. Salchipapa De La Casa")
    print("4. Limonada Cerezada")
    print("5. Jugo Natural")
    print("6. Gaseosa 600ml")
    print("7. salir")

    opcion = int(input("por favor, indique que desea pedir? "))
    if opcion ==1:
        print("¡Has pedido la Hamburguesa Doble Carne! Tu producto estara listo en 20 minutos. ¡Gracias!")
    elif opcion ==2:
        print("¡Has pedido el Perro Caliente Especial! Tu producto estara listo en 15 minutos. ¡Gracias!")
    elif opcion ==3:
        print("¡Has pedido la Salchipapa De la Casa! Tu producto estara listo en 25 minutos. ¡Gracias!")
    elif opcion ==4:
        print("¡Has pedido La Limonada Cerezada! Tu producto estara listo en 5 minutos. ¡Gracias!")
    elif opcion ==5:
        print("¡Has pedido El jugo natural! Tu producto estara listo en 6 minutos. ¡Gracias!")
    elif opcion ==6:
        print("¡Has pedido la Gaseosa de 600ml! Tu producto estara listo en 3 minutos. ¡Graciaas!")
    elif opcion ==7:
        print("saliendo del sistema...¡Gracias por tu visita!")
    else:
        print("Opcion no valida. por favor, elige un numero del 1 al 7.")