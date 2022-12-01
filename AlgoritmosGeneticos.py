import random

def inicializarPoblacion(n):
	poblacion = []
	for j in range (0, n):
		individuo = [0, 1, 0, 1, 0, 1] #Preparo plantilla base
		for i in range (0, len(individuo)):
			individuo[i] = random.choice([0,1]) #Hago aleatorio el individuo
		print(individuo)
		poblacion.append(individuo)
	return poblacion



def generarNuevoIndividuo(individuo1, individuo2):
	#Se define el cruce:
	# Del cand1 escogemos primeros 3 elementos. Del cand2 los últimos 3. Y luego Swipe. 
	nuevoIndividuo = [individuo2[-1], individuo2[-2], individuo2[-3], individuo1[0], individuo1[1], individuo1[2]]

	# Mutacion posible
	val = random.randint(1, 10 - 1)
	if(val >= 7): #Una alta probabilidad de mutar... 0.4p
		pos = random.randint(0, len(individuo1) - 1) #aleatoriamente cambiamos de estado en esa posición  haciendo la mutación en el individuo
		if(nuevoIndividuo[pos] == 0):
			nuevoIndividuo[pos] = 1
		else:
			nuevoIndividuo[pos] = 1
	return nuevoIndividuo

def fitness(individuo): # Depende del problema...
	return sum(individuo) #Inventamos que la suma mayor es el mejor candidato
	



mejorCandidato  = [0, 1, 0, 1, 0, 1]
maxGeneraciones = 5
gen = 0
while  not gen > maxGeneraciones:

	primeraGeneracion = inicializarPoblacion(10)
	#Cruzamos la mitad de la poblacion con la otra mitad...
	mitadPoblacion = primeraGeneracion[:int(len(primeraGeneracion)/2)]
	laOtraMitad = primeraGeneracion[int(len(primeraGeneracion)/2):]
	
	generacionNueva = []
	#Empieza el cruce...
	for individuo in mitadPoblacion: #Cada individuo cruza con una posición aleatoria de la otra mitad...
		
		pos = random.randint(0, len(laOtraMitad) -1)		
		candidato = laOtraMitad[pos]
		laOtraMitad.pop(pos) #Elimino al potencial individuo para no repetir

		nuevoIndividuo = generarNuevoIndividuo(individuo, candidato)
		generacionNueva.append(nuevoIndividuo)

	gen += 1
	print('Número de generación:',(gen), '. A continuación los individuos:')
	print(generacionNueva)


	aptitudVieja = fitness(mejorCandidato)
	for individuoNuevo in generacionNueva:
		aptitudNueva = fitness(individuoNuevo)
		if(aptitudNueva > aptitudVieja):
			mejorCandidato  =  individuoNuevo

	print('El mejor candidato es:', mejorCandidato)





