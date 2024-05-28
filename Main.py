print("*******Bienvenido al Burguer King*****")
print("Ingrese los datos para su factura electronica")




nombre=float
cedula=float
correo=float
opcionc=float
opcionp=float

sen=float(1.50)
med=float(2.50)
gra=float(3.25)

pbp=float(1.00)
pbm=float(1.50)
pbg=float(2.00)


nombre =input("Ingrese su nombre: ")
cedula =input("Ingrese su cedula: ")
correo =input("Ingrese su correo: ")
numero =float(input("Ingrese su numero de hamburguesas a adquirir: "))

print(numero)

print("Ingrese uno de los siguientes tipos de hamburguesas")
print("1)Sencilla")
print("2)Doble")
print("3)Triple")
opcionc=int(input("Ingrese la opcion: "))
if (opcionc<1 or opcionc>3):
    print("Error producto no existente")
    print("Gracias por usar nuestro servicio")
    exit(1)
else:()
 




print ("Ingrese su forma de pago")
print("1)Tarjeta de credito")
print("2)Efectivo")
opcionp=float(input("Ingrese la opcion:"))
if (opcionp<1 or opcionp>2):
    print("Error metodo de pago no valido")
    print("Gracias por usar nuestro servicio")
    exit(1)

if (opcionc==1 and opcionp==1):
    t=(numero*sen)*0.05
    print(f"Su cuenta total es: {t}")
    print(f"La factura se enviara a{correo}")
elif(opcionc==1 and opcionp==2):
    sd=(numero*sen)
    print( f"Su cuenta total es: {sd}" )
    print(f"La factura se enviara a{correo}")

elif(opcionc==2 and opcionp==1):
    ys=(numero*med)*0.05
    print(f"Su cuenta total es: {ys}")
    print(f"La factura se enviara a{correo}")
elif(opcionc==2 and opcionp==2):
    yx=(numero*med)
    print(f"Su cuenta total es: {yx}")
    print(f"La factura se enviara a{correo}")
elif(opcionc==3 and opcionp==1):
    xx=(numero*gra)*0.05
    print(f"Su cuenta total es {xx}")
    print(f"La factura se enviara a{correo}")
elif(opcionc==3 and opcionp==2):
    ws=(numero*med)
    print(f"Su cuenta total es: {ws}")
    print(f"La factura se enviara a{correo}")
else:{
   
}

print("Desea expandir su orden con bebidas y papas")
print("Digite 1 para si y 2 para no")
extrad=int(input())
if(extrad==1):
 print("Digite el numero segun la opcion deseada")
 print("1)Papas y bebidas pequeñas: 1.00$")
 print("2)Papas y bebidas medianas: 1.50$")   
 print("3)Papas y bebidas grandes: 2.00$")     
 extra=int(input("Digite la opcion: ")) 
 if(extra==1):
    print(f"Se agregara un cargo adicional de:{pbp}")
 elif(extra==2):
    print(f"Se agregara un cargo adicional de:{pbm}")
 elif(extra==3):
    print(f"Se agregara un cargo adicional de:{pbg}")
else:()
print("Gracia por su compra")






  
