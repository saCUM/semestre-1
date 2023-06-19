
#datos de tipos de numero
estatura= 1.71
peso= 70
complejo= 1 +4j

print ("impresion del numero complejo", complejo)

#operacion aritmetica basica 
imc= peso/estatura**2
print ("mi IMC es de ",imc,"\n")

#datos de tipo de cadena de caracteres
asignatura= "programacion"
carrera= "ingenieria civil informatica"

print("la asignatura de", asignatura ,"corresponde a la carrera de", carrera)


#valores booleanos
ampolleta= False
interruptor= True

#con type sabemos el tipo de datos que estamos tratando 
print(type(ampolleta))
print (type(interruptor))
print (type(imc))
print (type(carrera))
print (type(peso))


#Dato tipo array (objetos de tipo coleccion)
estudiantes= ["matias", "marco", "cristobal", "sebastian"]
num= [1,2,3,4,5,6]
lenguaje=["python"]
print (estudiantes)
print (num)
print (estudiantes.count("marco"))

print ("posicion (3)", estudiantes(3))
print ("posicion(-2)", estudiantes (-2))

#Declarando e inicializando una lite
nueva_lista= []
print("esta es una lista vacia",nueva_lista)

otra_lista= []
print ("esta es otra lista vacia",otra_lista)
print (type(otra_lista))

#lista de datos compuestos
lista_compuesta= list()
print ("esta es la lista compuesta", lista_compuesta)
num=[1,2,3,4,5,6,7]
lenguaje= ["javascript"]
print ("nuevo valor de arreglo del elemento",lenguaje)

#le dimos un valor de forma rapida
data_asig=[]
cod, ramo, estado, peso, nombre2,=data_asig



print (list("python"))
print (list(range(10)))
print ("\n")


#tuplas
grupo1= ("daniel", "cristian", 10, False, 300)
print (type(grupo1))

print (list("phyton"))
print (list(range(18)))
print("\n")

#tuplas o tupla
grupo1=("daniel","cristian",10, False, 300)
print(type(grupo1))

print ("daniel se repite", grupo1.count("daniel"))
print ("daniel esta en la posicion",grupo1.index("daniel"))
#obteniendo trozo de tuple

print (grupo1)

#como modifico una tupla?
list(grupo1)
print(type(grupo1))

#sets, formas de inicializar
conjuntovacio= set()
conjuntovacio={}
print(type(conjuntovacio))
conjunto_colores=set({"azul", "rojo","verde"})
conjunto_animales={"gato","perro","loro"}
print (type(conjunto_animales))
print ("el segundo set contiene los siguientes animales", conjunto_animales)


conjunto_vacio= set()
conjunto_vacio ={}
print (type(conjunto_vacio))


conjunto_de_colores= {set("azul, rojo, verde")}
conjunto_animales = {"gato","perro","loro"}
print (type(conjunto_de_colores))
print (type(conjunto_animales))



datos_personales={
    "nombre":"victor",
    "institucion": "ulagos",
    "edad": 29,
    "asignatura":{"estructura de datos" , "programacion"},
}
 



print ("diccionario inicial",datos_personales)

print ()
print(datos_personales("institucion"))



datos_personales

















