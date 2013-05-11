#FUNZIONE CHE DISEGNA LE RUOTE DI UNA LAMBORGHINI

from pyplasm import *

def drawRuota(rCerchione,distanzaSemigomme,nraggi,spessoreraggio) :
	
	rInternoGomma = rCerchione+rCerchione/2
	rGomma = rCerchione + rInternoGomma
	rRuota = rCerchione + 2*rInternoGomma
	metarcerchione = rCerchione/2
	lasse = distanzaSemigomme
	traslazioneasseruota = distanzaSemigomme/2
	GRID = COMP([INSR(PROD),AA(QUOTE)]) 
	
	e = 0.05
	rosso = [1,0,0,1]
	coloregomma = [47/255,51/255,53/255,1]
	nero = [0,0,0,1]
	grigio = [0.5,0.5,0.5,1]

	#FUNZIONE PER DISEGNARE UNA STRISCIA CIRCOLARE
	def fcircle(r) :
		def function(v):
			return [r*COS(v[0]), r*SIN(v[0])]
		return function

	
	#FUNZIONE PER DISEGNARE UNA GOMMA
	def fgomma(radius):
		r1, r2, interval1, interval2 = radius
		def fgomma0(subds):
			N , M = subds
			a=0.5*(r2-r1)
			c=0.5*(r1+r2)
			domain=Plasm.power(INTERVALS(interval1)(N),INTERVALS(interval2)(M))
			fx = lambda p: (c+a*math.cos(p[1])) * math.cos(p[0])
			fy = lambda p: (c+a*math.cos(p[1])) * math.sin (p[0])
			fz = lambda p: a*math.sin(p[1])
			return MAP(([fx,fy,fz]))(domain)
		return fgomma0

	#FUNZIONE PER DISEGNARE I RAGGI DI UN CERCHIONE
	def fraggi(raggio, nraggi) :
		raggi = [raggio]
		for count in range(0,nraggi-1):
			raggi.append(R([1,2])(2/nraggi*PI)(raggio))
			raggio = raggi[count+1]
			
		if nraggi==0:
			return none
		return STRUCT(raggi)
	
	#GOMMA
	domainstriscia = INTERVALS(2*PI)(50)
	semigomma1 = fgomma([rCerchione,rInternoGomma,2*PI,PI])([50,50])
	semigomma2 = T(3)(-distanzaSemigomme)(R([2,3])(PI)(fgomma([rCerchione,rInternoGomma,2*PI,PI])([50,50])))
	mappingsstriscia1 = fcircle(rInternoGomma)
	circlestriscia1 = COLOR(BLACK)(MAP(mappingsstriscia1)(domainstriscia))
	striscia = T(3)(-distanzaSemigomme)(EXTRUDE([None,circlestriscia1,distanzaSemigomme]))
	gomma = COLOR(BLACK)(STRUCT([semigomma1,semigomma2,striscia]))
	domainCircle = INTERVALS(2*PI)(50)
	mappingsstriscia2 = fcircle(rCerchione)
	circlestriscia2 = COLOR(BLACK)(MAP(mappingsstriscia2)(domainstriscia))
	cerchione = T(3)(-distanzaSemigomme)(EXTRUDE([None, circlestriscia2, distanzaSemigomme]))

	#ASSE
	asseruota1 = COLOR(GRAY)(T(3)(-lasse)(TUBE([0,rCerchione/3,lasse])(50)))
	asseruota2 = COLOR(GRAY)(T(3)(-lasse-0.2)(TUBE([0,rCerchione/6,lasse+0.4])(50)))

	#CERCHIONE
	c1=COLOR(GRAY)(T(3)(-distanzaSemigomme-0.4)(TUBE([rCerchione-0.2, rCerchione, distanzaSemigomme+0.8])(50)))
	c2=COLOR(GRAY)(T(3)(-distanzaSemigomme-0.2)(TUBE([rCerchione-0.8, rCerchione, distanzaSemigomme+0.4])(50)))
	c3=COLOR(GRAY)(T(3)(-distanzaSemigomme+0.1)(TUBE([rCerchione-1.4, rCerchione, distanzaSemigomme-0.2])(50)))
	cerchione = COLOR(BLACK)(STRUCT([c1,c2,c3]))

	#RAGGI
	raggioa = COLOR(GRAY)(T(3)(-distanzaSemigomme-0.2)(GRID([[0.3],[rCerchione-0.8],[distanzaSemigomme+0.4]])))
	raggiob = R([1,2])(PI/6)(raggioa)
	raggio1 = STRUCT([raggioa, raggiob])
	
	raggioc = R([1,2])(PI/3)(raggiob)
	raggiod = R([1,2])(PI/6)(raggioc)
	raggio2 = STRUCT([raggioc, raggiod])
	
	raggioe = R([1,2])(PI/3)(raggiod)
	raggiof = R([1,2])(PI/6)(raggioe)
	raggio3 = STRUCT([raggioe, raggiof])
	
	raggiog = R([1,2])(PI/3)(raggiof)
	raggioh = R([1,2])(PI/6)(raggiog)
	raggio4 = STRUCT([raggiog, raggioh])
	
	
	return STRUCT([gomma,cerchione,asseruota1,asseruota2,cerchione,raggio1,raggio2,raggio3,raggio4])

#PARAMETRI RUOTA
rCerchione = 8
distanzaSemigomme = 5
nraggi = 5
spessoreraggio = 2
distanzaRuote = 80
ruotamoment = drawRuota(rCerchione,distanzaSemigomme,nraggi,spessoreraggio)

ruotaant1 = S(3)(0.0375)(S(2)(0.0375)(S(1)(0.0375)(ruotamoment)))
ruotaant2 = T([3])(-2.35)(ruotaant1)
ruoteant = STRUCT([ruotaant1, ruotaant2])
ruotepost = T([1])(3.76)(ruoteant)

ruote = STRUCT([ruoteant,ruotepost])

VIEW(ruote)