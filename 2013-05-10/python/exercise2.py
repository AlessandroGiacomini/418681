from pyplasm import *

domain1 = INTERVALS(1)(50)
domain2 = PROD([domain1,domain1])

def BEZIERS1(points):
	return BEZIER(S1)(points)

def MAPBEZIER1D(points):
	return MAP(BEZIERS1(points))(domain1)

#BASE
p0b = [[3.91+0.2, 5.24], [4.54, 5.77], [7.02, 5.43], [9.53, 5.52]]
curve0b = MAPBEZIER1D(p0b)

p1b = [[3.91+0.2, 3.08], [4.26, 2.61], [6.11, 2.82], [9.53, 2.8]]
curve1b = MAPBEZIER1D(p1b)

p2b = [[3.91+0.2, 5.21], [3.75+0.2, 4.72], [3.71+0.2, 3.78], [3.91+0.2, 3.08]]
curve2b = MAPBEZIER1D(p2b)

p3b = [[9.88, 3.1], [9.78, 3.02], [9.65, 2.92], [9.53, 2.8]]
curve3b = MAPBEZIER1D(p3b)

p4b = [[9.88, 3.1], [10.05, 3.89], [10.03, 4.6], [9.85, 5.28]]
curve4b = MAPBEZIER1D(p4b)

p5b = [[9.85, 5.28], [9.78, 5.33], [9.66, 5.43], [9.53, 5.52]]
curve5b = MAPBEZIER1D(p5b)


BASE = STRUCT([curve0b,curve1b,curve2b,curve3b,curve4b,curve5b])

BASEFINAL = T(1)(13.9)(R([1,2])(PI)(T(2)(-4.2)(BASE)))




#LATERAL
p0l = [[5.27, 1.83], [6.89, 2.87], [9.13, 1.84], [9.8, 1.91]]
curve0l = MAPBEZIER1D(p0l)

p1l = [[3.89, 1.26], [4.36, 1.62], [4.62, 1.69], [5.27, 1.83]]
curve1l = MAPBEZIER1D(p1l)

p2l = [[4.1, 0.95], [4.04, 1.07], [3.99, 1.19], [3.89, 1.26]]
curve2l = MAPBEZIER1D(p2l)

p3l = [[4.1, 0.95], [4.25, 0.95], [4.44, 0.95], [4.65, 0.95]]
curve3l = MAPBEZIER1D(p3l)

p4l = [[5.72, 0.86], [5.7, 2.01], [4.53, 1.74], [4.65, 0.95]]
curve4l = MAPBEZIER1D(p4l)

p5l = [[5.72, 0.86], [6.27, 0.86], [7.72, 0.86], [8.41, 0.86]]
curve5l = MAPBEZIER1D(p5l)

p6l = [[9.45, 0.88], [9.73, 1.99], [8.11, 1.9], [8.41, 0.86]]
curve6l = MAPBEZIER1D(p6l)

p7l = [[9.45, 0.88], [9.63, 0.91], [9.77, 0.97], [9.91, 1.04]]
curve7l = MAPBEZIER1D(p7l)

p8l = [[9.8, 1.91], [9.97, 1.68], [10, 1.38], [9.91, 1.04]]
curve8l = MAPBEZIER1D(p8l)

LATERAL = STRUCT([curve0l,curve1l,curve2l,curve3l,curve4l,curve5l,curve6l,curve7l,curve8l])

LATERALFINAL = T(3)(-1.5)(R([2,3])(PI/2)(LATERAL))


#FRONT
p0f = [[2.99, 1.83], [2.77, 2.35], [2.59, 2.37], [1.83, 2.35]]
curve0f = MAPBEZIER1D(p0f)

p1f = [[2.99, 1.83],[3.14, 1.71]]
curve1f = MAPBEZIER1D(p1f)

p2f = [[3.06, 0.85], [3.2, 1.04], [3.14, 1.5], [3.14, 1.72]]
curve2f = MAPBEZIER1D(p2f)

p3f = [[3.06, 0.85], [2.17, 0.85], [1.32, 0.85], [0.5, 0.85]]
curve3f = MAPBEZIER1D(p3f)

p4f = [[0.41, 1.71], [0.42, 1.35], [0.4, 1.02], [0.5, 0.85]]
curve4f = MAPBEZIER1D(p4f)

p5f = [[0.41, 1.71],[0.57, 1.83]]
curve5f = MAPBEZIER1D(p5f)

p6f = [[0.57, 1.83], [0.74, 2.02], [0.53, 2.41], [1.83, 2.35]]
curve6f = MAPBEZIER1D(p6f)

FRONT = STRUCT([curve0f,curve1f,curve2f,curve3f,curve4f,curve5f,curve6f])

FRONTFINAL = T([1,2,3])([5,-1.8,-1.5])(R([1,2])(PI/2)(R([2,3])(PI/2)(FRONT)))

VIEW(STRUCT([LATERALFINAL, BASEFINAL, FRONTFINAL]))