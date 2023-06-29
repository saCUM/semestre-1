

Algoritmo paqueteria
	
	Escribir "seleccione su tipo de envio"
	
	
	leer p
	Definir encargo Como Entero
	Definir documento Como Entero
	Leer documento
	Leer encargo

	Escribir "seleccione la ubicacion del envio"
	Segun encargo Hacer
		norteamerica:
			costo=40
			Escribir "ha seleccionado norteamerica"
		centroamerica:
			costo=30
			Escribir "ha seleccionado centroamerica"
		sudamerica:
			costo=20
			Escribir "ha seleccionado sudamerica"
		europa:	
			costo=60
			Escribir "ha seleccionado europa"
		Asia:
			costo=70
			Escribir "ha selecionado Asia"
		De Otro Modo:
			Escribir "ingrese ubicación valida"
	Fin Segun
	
	Segun documento Hacer
		norteamerica:
			costo=20
			escribir "ha seleccionado norteamerica"
		centroamerica:
			costo=15
			Escribir "ha seleccionado centroamerica"
		sudamerica:
			costo= 10
			Escribir "ha seleccionado sudamerica"
		europa:	
			costo=30
			Escribir "ha seleccionado europa"
		Asia:
			costo=35
			Escribir "ha seleccionado Asia"
		De Otro Modo:
			Escribir  "ingrese ubicacion valida"
	Fin Segun
	
	
	
	
	
	
	Para p<-costo Hasta p Con Paso p Hacer
		Escribir "tu encargo tendra un costo de: ", p 
	Fin Para
	
	
	
	
FinAlgoritmo
