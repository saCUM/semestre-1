a=20
b=10
c=5
d=16


print ("")
print ("")




t= ("tiempo")
g= ("g")


v= g*t


print ("la velocidad de bajada en caida libre es de: {v}m/s")
print ("la velocidad del objeto en caida es de: {:2f}", format [v], "m/s")
print ("la velocidad del objeto en caida libre es de:[v.2;]")









c1= 4+3
print (type(c1))

c2= complex(3-2)
print ("el numero complejo es: ")




print (c2.imag)



print ("hola"*5)


print ("hola"+28)






print ("hola" + ())

print ("comparando numeros")


print (a==b)
print (a<=b )
print (a>=b)
print ()





animal_domestico = "gato"
animal_salvaje= "leopardo"

print ("comprension cadenas de caracteres")
print (animal_domestico== animal_salvaje ) #igual a
print (animal_domestico != animal_salvaje) #desigual a
print (animal_domestico > animal_salvaje) #mayor que
print (animal_domestico < animal_salvaje) #menor que 
print (animal_domestico <= animal_salvaje) #mayor o igual       
print (animal_domestico >= animal_salvaje) #menor o igual
    


bencina= True
encendido= True
edad= 19

#utilizando el aprendizaje 
if bencina and encendido:
  print ("el vehiculo peued eavamzar")

else:
  print ("el vehiculo no puede avanzar")

#utilizamos el operador not junto or

if not bencina or encendido:
    print ("el vehiculo puede avanzar")
else:
    print ("el vehiculo no puede avanzar")
#utilizando el operador not junto and
if not bencina and encendido:   
    print ("el vehiculo puede avanzar") #es verdadero
else:
    print ("el vehiculo no puede avanzar")

#utilizando el operador not junto and y or
if not bencina or (encendido and edad>=18):
    print ("el vehiculo puede avanzar ")
else:
    print ("el vehiculo no puede avanzar ")

    