#FUNZIONE CHE DISEGNA IL VOLANTE DI UNA LAMBORGHINI

from pyplasm import *

domain2 = POWER([INTERVALS(1)(10),INTERVALS(1)(10)])

l = 0.30
distl = 1.6

####################################################################################################

p1 = BEZIER(S1)([[6.32, 2.39, 0], [6.35, 2.26, 0], [6.37, 2.11, 0], [6.33, 1.95, 0]])
p2 = BEZIER(S1)([[6.06, 2.44, 0], [6.08, 2.25, 0.2], [6.09, 2.11, 0.2], [6.1, 1.95, 0]])
p3 = BEZIER(S1)([[5.91, 2.46, 0], [5.93, 2.3, 0.2], [5.95, 2.12, 0.2], [5.96, 1.95, 0]])
p4 = BEZIER(S1)([[5.7, 2.53, 0], [5.77, 2.33, 0], [5.78, 2.11, 0], [5.74, 1.92, 0]])

punder1 = BEZIER(S1)([[6.32, 2.39, 0],[6.06, 2.44, 0],[5.91, 2.46, 0],[5.7, 2.53, 0]])
punder1s = BEZIER(S1)([[6.32, 2.39, -l],[6.06, 2.44, -l],[5.91, 2.46, -l],[5.7, 2.53, -l]])
punder2 = BEZIER(S1)([[6.33, 1.95, 0],[6.1, 1.95, 0],[5.96, 1.95, 0],[5.74, 1.92, 0]])
punder2s = BEZIER(S1)([[6.33, 1.95, -l],[6.1, 1.95, -l],[5.96, 1.95, -l],[5.74, 1.92, -l]])

p1s = BEZIER(S1)([[6.32, 2.39, -l], [6.35, 2.26, -l], [6.37, 2.11, -l], [6.33, 1.95, -l]])
p2s = BEZIER(S1)([[6.06, 2.44, -l], [6.08, 2.25, -0.2-l], [6.09, 2.11, -0.2-l], [6.1, 1.95, -l]])
p3s = BEZIER(S1)([[5.91, 2.46, -l], [5.93, 2.3, -0.2-l], [5.95, 2.12, -0.2-l], [5.96, 1.95, -l]])
p4s = BEZIER(S1)([[5.7, 2.53, -l], [5.77, 2.33, -l], [5.78, 2.11, -l], [5.74, 1.92, -l]])

out1 = MAP(BEZIER(S2)([p1,p2,p3,p4]))(POWER([INTERVALS(1)(50),INTERVALS(1)(50)]))
out1s = MAP(BEZIER(S2)([p1s,p2s,p3s,p4s]))(POWER([INTERVALS(1)(50),INTERVALS(1)(50)]))

unione1 = MAP(BEZIER(S2)([p1,p1s]))(domain2)
unione4 = MAP(BEZIER(S2)([p4,p4s]))(domain2)
unioneunder1 = MAP(BEZIER(S2)([punder1,punder1s]))(domain2)
unioneunder2 = MAP(BEZIER(S2)([punder2,punder2s]))(domain2)
volante1 = STRUCT([unione1, unione4,unioneunder1,unioneunder2, out1, out1s])

####################################################################################################

p5 = BEZIER(S1)([[3.6, 2.37,0], [3.58, 2.22,0], [3.58, 2.07,0], [3.63, 1.94,0]])
p6 = BEZIER(S1)([[3.77, 2.39,0], [3.74, 2.23,0.2], [3.75, 2.09,0.2], [3.76, 1.94,0]])
p7 = BEZIER(S1)([[4.01, 2.48,0], [4, 2.3,0.2], [3.99, 2.11,0.2], [4, 1.92,0]])
p8 = BEZIER(S1)([[4.17, 2.52,0], [4.13, 2.33,0], [4.13, 2.11,0], [4.15, 1.9,0]])

punder3 = BEZIER(S1)([[3.6, 2.37,0],[3.77, 2.39,0],[4.01, 2.48,0],[4.17, 2.52,0]])
punder3s = BEZIER(S1)([[3.63, 1.94,-l],[3.76, 1.94,-l],[4, 1.92,-l],[4.15, 1.9,-l]])
punder4 = BEZIER(S1)([[3.63, 1.94,0],[3.76, 1.94,0],[4, 1.92,0],[4.15, 1.9,0]])
punder4s = BEZIER(S1)([[3.63, 1.94,-l],[3.76, 1.94,-l],[4, 1.92,-l],[4.15, 1.9,-l]])

p5s = BEZIER(S1)([[3.6, 2.37,-l], [3.58, 2.22,-l], [3.58, 2.07,-l], [3.63, 1.94,-l]])
p6s = BEZIER(S1)([[3.77, 2.39,-l], [3.74, 2.23,-0.2-l], [3.75, 2.09,-0.2-l], [3.76, 1.94,-l]])
p7s = BEZIER(S1)([[4.01, 2.48,-l], [4, 2.3,-0.2-l], [3.99, 2.11,-0.2-l], [4, 1.92,-l]])
p8s = BEZIER(S1)([[4.17, 2.52,-l], [4.13, 2.33,-l], [4.13, 2.11,-l], [4.15, 1.9,-l]])

out2 = MAP(BEZIER(S2)([p5,p6,p7,p8]))(POWER([INTERVALS(1)(50),INTERVALS(1)(50)]))
out2s = MAP(BEZIER(S2)([p5s,p6s,p7s,p8s]))(POWER([INTERVALS(1)(50),INTERVALS(1)(50)]))

unione5 = MAP(BEZIER(S2)([p5,p5s]))(domain2)
unione8 = MAP(BEZIER(S2)([p8,p8s]))(domain2)
unioneunder3 = MAP(BEZIER(S2)([punder3,punder3s]))(domain2)
unioneunder4 = MAP(BEZIER(S2)([punder4,punder4s]))(domain2)

volante2 = STRUCT([unione5, unione8, unioneunder3,unioneunder4, out2, out2s])

####################################################################################################

domain2 = POWER([INTERVALS(1)(10),INTERVALS(1)(10)])

l = 0.30
distl = 0.8

####################################################################################################

p1 = BEZIER(S1)([[6.32, 2.39, 0], [6.35, 2.26, 0], [6.37, 2.11, 0], [6.33, 1.95, 0]])
p2 = BEZIER(S1)([[6.06, 2.44, 0], [6.08, 2.25, 0.2], [6.09, 2.11, 0.2], [6.1, 1.95, 0]])
p3 = BEZIER(S1)([[5.91, 2.46, 0], [5.93, 2.3, 0.2], [5.95, 2.12, 0.2], [5.96, 1.95, 0]])
p4 = BEZIER(S1)([[5.7, 2.53, 0], [5.77, 2.33, 0], [5.78, 2.11, 0], [5.74, 1.92, 0]])

punder1 = BEZIER(S1)([[6.32, 2.39, 0],[6.06, 2.44, 0],[5.91, 2.46, 0],[5.7, 2.53, 0]])
punder1s = BEZIER(S1)([[6.32, 2.39, -l],[6.06, 2.44, -l],[5.91, 2.46, -l],[5.7, 2.53, -l]])
punder2 = BEZIER(S1)([[6.33, 1.95, 0],[6.1, 1.95, 0],[5.96, 1.95, 0],[5.74, 1.92, 0]])
punder2s = BEZIER(S1)([[6.33, 1.95, -l],[6.1, 1.95, -l],[5.96, 1.95, -l],[5.74, 1.92, -l]])

p1s = BEZIER(S1)([[6.32, 2.39, -l], [6.35, 2.26, -l], [6.37, 2.11, -l], [6.33, 1.95, -l]])
p2s = BEZIER(S1)([[6.06, 2.44, -l], [6.08, 2.25, -0.2-l], [6.09, 2.11, -0.2-l], [6.1, 1.95, -l]])
p3s = BEZIER(S1)([[5.91, 2.46, -l], [5.93, 2.3, -0.2-l], [5.95, 2.12, -0.2-l], [5.96, 1.95, -l]])
p4s = BEZIER(S1)([[5.7, 2.53, -l], [5.77, 2.33, -l], [5.78, 2.11, -l], [5.74, 1.92, -l]])

out1 = MAP(BEZIER(S2)([p1,p2,p3,p4]))(POWER([INTERVALS(1)(50),INTERVALS(1)(50)]))
out1s = MAP(BEZIER(S2)([p1s,p2s,p3s,p4s]))(POWER([INTERVALS(1)(50),INTERVALS(1)(50)]))

unione1 = MAP(BEZIER(S2)([p1,p1s]))(domain2)
unione4 = MAP(BEZIER(S2)([p4,p4s]))(domain2)
unioneunder1 = MAP(BEZIER(S2)([punder1,punder1s]))(domain2)
unioneunder2 = MAP(BEZIER(S2)([punder2,punder2s]))(domain2)
volante1 = STRUCT([unione1, unione4,unioneunder1,unioneunder2, out1, out1s])

####################################################################################################
t = 0.6

p5 = BEZIER(S1)([[3.6+t, 2.37,0], [3.58+t, 2.22,0], [3.58+t, 2.07,0], [3.63+t, 1.94,0]])
p6 = BEZIER(S1)([[3.77+t, 2.39,0], [3.74+t, 2.23,0.2], [3.75+t, 2.09,0.2], [3.76+t, 1.94,0]])
p7 = BEZIER(S1)([[4.01+t, 2.48,0], [4+t, 2.3,0.2], [3.99+t, 2.11,0.2], [4+t, 1.92,0]])
p8 = BEZIER(S1)([[4.17+t, 2.52,0], [4.13+t, 2.33,0], [4.13+t, 2.11,0], [4.15+t, 1.9,0]])

punder3 = BEZIER(S1)([[3.6+t, 2.37,0],[3.77+t, 2.39,0],[4.01+t, 2.48,0],[4.17+t, 2.52,0]])
punder3s = BEZIER(S1)([[3.6+t, 2.37,-l],[3.77+t, 2.39,-l],[4.01+t, 2.48,-l],[4.17+t, 2.52,-l]])
punder4 = BEZIER(S1)([[3.63+t, 1.94,0],[3.76+t, 1.94,0],[4+t, 1.92,0],[4.15+t, 1.9,0]])
punder4s = BEZIER(S1)([[3.63+t, 1.94,-l],[3.76+t, 1.94,-l],[4+t, 1.92,-l],[4.15+t, 1.9,-l]])

p5s = BEZIER(S1)([[3.6+t, 2.37,-l], [3.58+t, 2.22,-l], [3.58+t, 2.07,-l], [3.63+t, 1.94,-l]])
p6s = BEZIER(S1)([[3.77+t, 2.39,-l], [3.74+t, 2.23,-0.2-l], [3.75+t, 2.09,-0.2-l], [3.76+t, 1.94,-l]])
p7s = BEZIER(S1)([[4.01+t, 2.48,-l], [4+t, 2.3,-0.2-l], [3.99+t, 2.11,-0.2-l], [4+t, 1.92,-l]])
p8s = BEZIER(S1)([[4.17+t, 2.52,-l], [4.13+t, 2.33,-l], [4.13+t, 2.11,-l], [4.15+t, 1.9,-l]])

out2 = MAP(BEZIER(S2)([p5,p6,p7,p8]))(POWER([INTERVALS(1)(50),INTERVALS(1)(50)]))
out2s = MAP(BEZIER(S2)([p5s,p6s,p7s,p8s]))(POWER([INTERVALS(1)(50),INTERVALS(1)(50)]))

unione5 = MAP(BEZIER(S2)([p5,p5s]))(domain2)
unione8 = MAP(BEZIER(S2)([p8,p8s]))(domain2)
unioneunder3 = MAP(BEZIER(S2)([punder3,punder3s]))(domain2)
unioneunder4 = MAP(BEZIER(S2)([punder4,punder4s]))(domain2)

volante2 = STRUCT([unione5, unione8, unioneunder3,unioneunder4,out2, out2s])

####################################################################################################

GRID = COMP([INSR(PROD),AA(QUOTE)])
volante3 =  T([1,2,3])([5,0.95,-0.3])(GRID([[0.5],[0.7],[0.3]]))

####################################################################################################

clacson = T([1,2,3])([5.25,2.2,-0.3])(TUBE([0, 0.6, 0.30])(50))

####################################################################################################

def TOR (radius):
	r1 , r2, interval1, interval2 = radius
	def TOR0 (subds):
		N , M = subds
		a=0.5*(r2-r1)
		c=0.5*(r1+r2)
		domain=Plasm.power(  INTERVALS(interval1)(N),  INTERVALS(interval2)(M)  )
		fx = lambda p: (c+a*COS(p[1])) * COS(p[0])
		fy = lambda p: (c+a*COS(p[1])) * SIN(p[0])
		fz = lambda p: a*SIN(p[1])
		return MAP(([fx,fy,fz]))(domain)
	return TOR0


manubrio = T([1,2,3])([5.25,2.2,-0.15])(TOR([1,1+0.4, 2*PI, 2*PI])([50,50]))

####################################################################################################

volante = COLOR(BLACK)(STRUCT([volante1, volante2,volante3, clacson, manubrio]))
VIEW(volante)