estudiante={
    "nombre": "",
    "asignatura":"",
    "nota lab 1":"",
    "nota lab 2":"",
}


estudiante["nombre del estudiante"]=input ("nombre del estudiante")
estudiante["nombre de la asignatura"]= input ("nombre de la asignatura")
estudiante["nota lab 1"]= input ("nota lab 1")
estudiante["nota lab 2"]= input ("nota lab 2")
nota_final= float(estudiante["nota laboratorio 1"]) *0.3 + float(estudiante["nota laboratio 2"]) *0.7

estudiante["promedio ponderado"]= f"{nota_final:.1f}"
print (estudiante)
