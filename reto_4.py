print ("Escriba los nombres de sus pacientes")

#paciente

paciente1= (input("ingrese el nombre del primer paciente:"))
paciente2= (input("ingrese el nombre del segundo paciente:"))
paciente3= (input("igrese nombre de su tercer paciente:"))


#peso

peso1= (input("ingrese el peso del primer paciente"))
peso2= (input("ingrese peso del segundo paciente"))
peso3= (input("ingrese peso del tercer paciente"))



#estatura

estatura1= int(input("ingrese la estatura del primer paciente"))
estatura2= int(input("ingrese la estatura del segundo paciente"))
estatura3= int(input("ingrese la estatura del tercer paciente"))




#edad
edad1= int(input("ingrese edad del primer paciente"))
edad2= int(input("ingrese edad del segundo paciente"))
edad3= int(input("ingrese edad del tercer paciente"))

while  edad1 < 0: 
    print ("la edad ingresada no es valida ")
    edad1 =int (input("ingrese edad valida"))


while edad2 <0:
    print ("la edad ingresada no es valida ")
    edad2= int (input("ingrese edad valida"))

    
while edad3 <0:
    print ("ingrese edad valida")
    edad3=int (input("ingrese edad valida"))




t_paciente1= paciente1,peso1,estatura1,edad1
t_paciente2= paciente2,peso2,estatura2,edad2
t_paciente3= paciente3,peso3,estatura3,edad3


t_pacientes= t_paciente1,t_paciente2,t_paciente3
print (t_pacientes)






