ciudades= ["santiago","temuco", "osorno","punta arenas"]
ica=[124,99,246,50]

minimo= ica.index (min[ica])
print (f"la ciudad con el indice mas bajo es{ciudades[ica]} con un indice de {min[ica]}")

maximo= max.index (max[ica])
print (f"la ciudad con el indice mas alto es{ciudades[ica]} con un indice de {max[ica]}")

for i in range (len(ciudades)):
    if ica [i] <= 0 and ica [i] <= 50:
       print (f"{ciudades[i]} tiene un indice de calidad del aire bueno") 
    elif ica [i] >= 100 and ica [i] <= 100:
       print (f"{ciudades[i]} tiene un indice de calidad del aire moderado")   





