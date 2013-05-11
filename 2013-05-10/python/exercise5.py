#FUNZIONE CHE DISEGNA LA CARROZZERIA DI UNA LAMBORGHINI

from pyplasm import *

domain2 = POWER([INTERVALS(1)(50),INTERVALS(1)(50)])
l = 2.73
points0 = BEZIER(S1)([[4.09, 0.97, -0.2], [4.03, 1.08,-0.2], [3.98, 1.18,-0.2], [3.91, 1.26,-0.2]])
points1 = BEZIER(S1)([[4.15, 0.97,0], [4.15, 1.11,0], [4.15, 1.28,0], [4.16, 1.44,0]])
points2 = BEZIER(S1)([[4.26, 0.97,0], [4.24, 1.14,0], [4.23, 1.29,0], [4.22, 1.47,0]])
points3 = BEZIER(S1)([[4.37, 0.97,0], [4.35, 1.12,0], [4.34, 1.33,0], [4.33, 1.52,0]])
points4 = BEZIER(S1)([[4.46, 0.97,0], [4.43, 1.16,0], [4.41, 1.37,0], [4.41, 1.56,0]])
points5 = BEZIER(S1)([[4.54, 0.97,0], [4.52, 1.16,0], [4.5, 1.37,0], [4.5, 1.6,0]])
points6 = BEZIER(S1)([[4.64, 0.97,0], [4.65, 1.17,0], [4.65, 1.4,0], [4.64, 1.66,0]])
points7 = BEZIER(S1)([[4.65, 0.97,0], [4.64, 1.27,0], [4.69, 1.5,0], [4.76, 1.72,0]])
points8 = BEZIER(S1)([[4.67, 0.97,0], [4.5, 1.19,0], [4.69, 1.45,0], [4.73, 1.71,0]])
points9 = BEZIER(S1)([[4.67, 0.97,0], [4.47, 1.91,0], [5.92, 1.88,0], [5.69, 0.97,0]])
points10 = BEZIER(S1)([[4.3, 1.5,0], [4.85, 1.87,0], [5.44, 1.82,0], [5.96, 1.8,0]])
points11 = BEZIER(S1)([[5.69, 0.97,0], [5.76, 1.26,0], [5.82, 1.55,0], [5.96, 1.8,0]])
points12 = BEZIER(S1)([[6.64, 0.97,0], [6.59, 1.2,0], [6.54, 1.52,0], [6.47, 1.83,0]])
points13 = BEZIER(S1)([[7.15, 0.97,0], [7.1, 1.23,0], [7.07, 1.56,0], [7.03, 1.87,0]])
points14 = BEZIER(S1)([[7.96, 0.97,0], [7.96, 1.32,0], [7.97, 1.63,0], [8, 1.97,0]])
points15 = BEZIER(S1)([[8.4, 0.97,0], [8.36, 1.41,0], [8.37, 1.72,0], [8.33, 2,0]])
points16 = BEZIER(S1)([[8.4, 0.97,0], [8.23, 1.91,0], [9.68, 1.88,0], [9.45, 0.97,0]])
points17 = BEZIER(S1)([[8.33, 2,0], [8.78, 2.02,0], [9.1, 2,0], [9.48, 1.89,0]])
points18 = BEZIER(S1)([[9.45, 0.97,0], [9.52, 1.26,0], [9.39, 1.57,0], [9.38, 1.9,0]])
points19 = BEZIER(S1)([[9.77, 0.96,0], [9.74, 1.24,0], [9.72, 1.6,0], [9.68, 1.89,0]])
points20 = BEZIER(S1)([[9.93, 1.01,-0.2], [9.89, 1.33,-0.2], [9.82, 1.56,-0.2], [9.68, 1.89,-0.2]])
points21 = BEZIER(S1)([[5.19, 1.79,0], [6.1, 2.38,-0.3], [7.1, 2.49,-0.3], [9.48, 1.89,0]])
points22 = BEZIER(S1)([[5.19, 1.79,0], [6.1, 2.28,-0.2], [7.12, 2.39,-0.2], [9.48, 1.89,0]])
points23 = BEZIER(S1)([[5.19, 1.79,0], [6.14, 2.1,-0.1], [6.9, 2.34,-0.1], [9.48, 1.89,0]])
points24 = BEZIER(S1)([[5.19, 1.79,0], [6.02, 1.9,0], [7.18, 2.16,0], [9.48, 1.89,0]])
points25 = BEZIER(S1)([[5.19, 1.79,0], [6.54, 1.66,0], [7.21, 2.11,0], [9.48, 1.89,0]])

points0s = BEZIER(S1)([[4.09, 0.97, -0.2-l+0.4], [4.03, 1.08,-0.2-l+0.4], [3.98, 1.18,-0.2-l+0.4], [3.91, 1.26,-0.2-l+0.4]])
points1s = BEZIER(S1)([[4.15, 0.97,-l], [4.15, 1.11,-l], [4.15, 1.28,-l], [4.16, 1.44,-l]])
points2s = BEZIER(S1)([[4.26, 0.97,-l], [4.24, 1.14,-l], [4.23, 1.29,-l], [4.22, 1.47,-l]])
points3s = BEZIER(S1)([[4.37, 0.97,-l], [4.35, 1.12,-l], [4.34, 1.33,-l], [4.33, 1.52,-l]])
points4s = BEZIER(S1)([[4.46, 0.97,-l], [4.43, 1.16,-l], [4.41, 1.37,-l], [4.41, 1.56,-l]])
points5s = BEZIER(S1)([[4.54, 0.97,-l], [4.52, 1.16,-l], [4.5, 1.37,-l], [4.5, 1.6,-l]])
points6s = BEZIER(S1)([[4.64, 0.97,-l], [4.65, 1.17,-l], [4.65, 1.4,-l], [4.64, 1.66,-l]])
points7s = BEZIER(S1)([[4.65, 0.97,-l], [4.64, 1.27,-l], [4.69, 1.5,-l], [4.76, 1.72,-l]])
points8s = BEZIER(S1)([[4.67, 0.97,-l], [4.5, 1.19,-l], [4.69, 1.45,-l], [4.73, 1.71,-l]])
points9s = BEZIER(S1)([[4.67, 0.97,-l], [4.47, 1.91,-l], [5.92, 1.88,-l], [5.69, 0.97,-l]])
points10s = BEZIER(S1)([[4.3, 1.5,-l], [4.85, 1.87,-l], [5.44, 1.82,-l], [5.96, 1.8,-l]])
points11s = BEZIER(S1)([[5.69, 0.97,-l], [5.76, 1.26,-l], [5.82, 1.55,-l], [5.96, 1.8,-l]])
points12s = BEZIER(S1)([[6.64, 0.97,-l], [6.59, 1.2,-l], [6.54, 1.52,-l], [6.47, 1.83,-l]])
points13s = BEZIER(S1)([[7.15, 0.97,-l], [7.1, 1.23,-l], [7.07, 1.56,-l], [7.03, 1.87,-l]])
points14s = BEZIER(S1)([[7.96, 0.97,-l], [7.96, 1.32,-l], [7.97, 1.63,-l], [8, 1.97,-l]])
points15s = BEZIER(S1)([[8.4, 0.97,-l], [8.36, 1.41,-l], [8.37, 1.72,-l], [8.33, 2,-l]])
points16s = BEZIER(S1)([[8.4, 0.97,-l], [8.23, 1.91,-l], [9.68, 1.88,-l], [9.45, 0.97,-l]])
points17s = BEZIER(S1)([[8.33, 2,-l], [8.78, 2.02,-l], [9.1, 2,-l], [9.48, 1.89,-l]])
points18s = BEZIER(S1)([[9.45, 0.97,-l], [9.52, 1.26,-l], [9.39, 1.57,-l], [9.38, 1.9,-l]])
points19s = BEZIER(S1)([[9.77, 0.96,-l], [9.74, 1.24,-l], [9.72, 1.6,-l], [9.68, 1.89,-l]])
points20s = BEZIER(S1)([[9.93, 1.01,-0.2-l+0.4], [9.89, 1.33,-0.2-l+0.4], [9.82, 1.56,-0.2-l+0.4], [9.68, 1.89,-0.2-l+0.4]])
points21s = BEZIER(S1)([[5.19, 1.79,-l], [6.1, 2.38,-0.3-l+0.6], [7.1, 2.49,-0.3-l+0.6], [9.48, 1.89,-l]])
points22s = BEZIER(S1)([[5.19, 1.79,-l], [6.1, 2.28,-0.2-l+0.4], [7.12, 2.39,-0.2-l+0.4], [9.48, 1.89,-l]])
points23s = BEZIER(S1)([[5.19, 1.79,-l], [6.14, 2.1,-0.1-l+0.2], [6.9, 2.34,-0.1-l+0.2], [9.48, 1.89,-l]])
points24s = BEZIER(S1)([[5.19, 1.79,-l], [6.02, 1.9,-l], [7.18, 2.16,-l], [9.48, 1.89,-l]])
points25s = BEZIER(S1)([[5.19, 1.79,-l], [6.54, 1.66,-l], [7.21, 2.11,-l], [9.48, 1.89,-l]])


result1 = MAP(BEZIER(S2)([points0,points1,points2,points3,points4,points5, points6, points7, points8]))(POWER([INTERVALS(1)(50),INTERVALS(1)(50)]))
result2 = MAP(BEZIER(S2)([points9, points10]))(POWER([INTERVALS(1)(50),INTERVALS(1)(50)]))
result3 = MAP(BEZIER(S2)([points11, points12, points13, points14, points15]))(POWER([INTERVALS(1)(50),INTERVALS(1)(50)]))
result4 = MAP(BEZIER(S2)([points16,points17]))(POWER([INTERVALS(1)(50),INTERVALS(1)(50)]))
result5 = MAP(BEZIER(S2)([points18,points19,points20]))(POWER([INTERVALS(1)(50),INTERVALS(1)(50)]))
result6 = MAP(BEZIER(S2)([points21,points22,points23,points24,points25]))(POWER([INTERVALS(1)(50),INTERVALS(1)(50)]))


result1s = MAP(BEZIER(S2)([points0s,points1s,points2s,points3s,points4s,points5s, points6s, points7s, points8s]))(POWER([INTERVALS(1)(50),INTERVALS(1)(50)]))
result2s = MAP(BEZIER(S2)([points9s, points10s]))(POWER([INTERVALS(1)(50),INTERVALS(1)(50)]))
result3s = MAP(BEZIER(S2)([points11s, points12s, points13s, points14s, points15s]))(POWER([INTERVALS(1)(50),INTERVALS(1)(50)]))
result4s = MAP(BEZIER(S2)([points16s,points17s]))(POWER([INTERVALS(1)(50),INTERVALS(1)(50)]))
result5s = MAP(BEZIER(S2)([points18s,points19s,points20s]))(POWER([INTERVALS(1)(50),INTERVALS(1)(50)]))
result6s = MAP(BEZIER(S2)([points21s,points22s,points23s,points24s,points25s]))(POWER([INTERVALS(1)(50),INTERVALS(1)(50)]))


lateralDX = STRUCT([result1,result2,result3,result4,result5,result6])
lateralSX = STRUCT([result1s,result2s,result3s,result4s,result5s,result6s])

unione0 = MAP(BEZIER(S2)([points0,points0s]))(domain2)
unione9 = MAP(BEZIER(S2)([points9,points9s]))(domain2)
unione10 = MAP(BEZIER(S2)([points10,points10s]))(domain2)
unione16 = MAP(BEZIER(S2)([points16,points16s]))(domain2)
unione20 = MAP(BEZIER(S2)([points20,points20s]))(domain2)
unione21 = MAP(BEZIER(S2)([points21,points21s]))(domain2)

pointsclose1 = BEZIER(S1)([[3.91, 1.26,-0.2],[4.16, 1.44,0],[4.22, 1.47,0],[4.33, 1.52,0],[4.41, 1.56,0],[4.5, 1.6,0],[4.64, 1.66,0],[4.76, 1.72,0],[4.73, 1.71,0]])
pointsclose1s = BEZIER(S1)([[3.91, 1.26,-0.2-l+0.4],[4.16, 1.44,-l],[4.22, 1.47,-l],[4.33, 1.52,-l],[4.41, 1.56,-l],[4.5, 1.6,-l],[4.64, 1.66,-l],[4.76, 1.72,-l],[4.73, 1.71,-l]])

pointsclose2 = BEZIER(S1)([[9.38, 1.9,0],[9.68, 1.89,0],[9.68, 1.89,-0.2]])
pointsclose2s = BEZIER(S1)([[9.38, 1.9,-l],[9.68, 1.89,-l],[9.68, 1.89,-0.2-l+0.4]])

pointsclose3 = BEZIER(S1)([[4.09, 0.97, -0.2],[4.15, 0.97,0],[4.26, 0.97,0],[4.37, 0.97,0],[4.46, 0.97,0],[4.54, 0.97,0],[4.64, 0.97,0],[4.65, 0.97,0],[4.67, 0.97,0]])
pointsclose3s = BEZIER(S1)([[4.09, 0.97, -0.2-l+0.4],[4.15, 0.97,-l],[4.26, 0.97,-l],[4.37, 0.97,-l],[4.46, 0.97,-l],[4.54, 0.97,-l],[4.64, 0.97,-l],[4.65, 0.97,-l],[4.67, 0.97,-l]])

pointsclose4 = BEZIER(S1)([[5.69, 0.97,0],[6.64, 0.97,0],[7.15, 0.97,0],[7.96, 0.97,0],[8.4, 0.97,0]])
pointsclose4s = BEZIER(S1)([[5.69, 0.97,-l],[6.64, 0.97,-l],[7.15, 0.97,-l],[7.96, 0.97,-l],[8.4, 0.97,-l]])

pointsclose5 = BEZIER(S1)([[9.45, 0.97,0],[9.77, 0.96,0],[9.93, 1.01,-0.2]])
pointsclose5s = BEZIER(S1)([[9.45, 0.97,-l],[9.77, 0.96,-l],[9.93, 1.01,-0.2-l+0.4]])

unioneclose1 = MAP(BEZIER(S2)([pointsclose1,pointsclose1s]))(domain2)
unioneclose2 = MAP(BEZIER(S2)([pointsclose2,pointsclose2s]))(domain2)
unioneclose3 = MAP(BEZIER(S2)([pointsclose3,pointsclose3s]))(domain2)
unioneclose4 = MAP(BEZIER(S2)([pointsclose4,pointsclose4s]))(domain2)
unioneclose5 = MAP(BEZIER(S2)([pointsclose5,pointsclose5s]))(domain2)
unioneclose = STRUCT([unioneclose1,unioneclose2,unioneclose3,unioneclose4,unioneclose5])

car = COLOR(YELLOW)(STRUCT([lateralDX,lateralSX,unione0,unione9,unione10,unione16,unione20,unione21,unioneclose]))

########################################################################################################################################

#FUNZIONE CHE DISEGNA LE RUOTE DI UNA LAMBORGHINI

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

ruote = COLOR(GRAY)(T([1,2,3])([5.17,1.1,-0.1])(STRUCT([ruoteant,ruotepost])))

########################################################################################################################################

final = STRUCT([car, ruote])

VIEW(final)