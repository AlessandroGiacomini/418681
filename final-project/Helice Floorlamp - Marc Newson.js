//Helice Floorlamp - Marc Newson
//********************************************************************************************************
//Base lamp

colorlamp = [0.75,0.75,0.75,1]
colorbase = [0.25,0.25,0.25,1]
var domainbase = DOMAIN([[0,1],[0,2*PI]])([60,60]);
hlamp = 12;
var rhole = 0.3;

var profilebase1 = BEZIER(S0)([[3.86-3.86+rhole, 0, 1.79-1.59], [4.37-3.86+rhole, 0, 1.76-1.59], [4.69-3.86+rhole, 0, 1.72-1.59], [4.7-3.86+rhole, 0, 1.59-1.59]]);
var mappingbase1 = ROTATIONAL_SURFACE(profilebase1);
var surfacebase1 = MAP(mappingbase1)(domainbase);

var profilebase2 = BEZIER(S0)([[3.86-4.16+rhole, 0, 1.79-1.59], [4.37-3.86+rhole, 0, 1.76-1.59], [4.69-3.86+rhole, 0, 1.72-1.59], [4.7-3.86+rhole, 0, 1.59-1.59]]);
var mappingbase2 = ROTATIONAL_SURFACE(profilebase2);
var surfacebase2 = R([1,2])([PI,PI])(MAP(mappingbase2)(domainbase));

var baselamp = STRUCT([surfacebase1, COLOR(colorbase)(surfacebase2)]);
var toplamp = COLOR(colorlamp)(T([2])([hlamp])(R([1,2])([PI,PI])(STRUCT([surfacebase1, surfacebase2]))));

var topbase = STRUCT([baselamp, toplamp]);

//********************************************************************************************************
//Body lamp

var profilecurvebase = BEZIER(S0)([[3.98-3.98+0.03, 0, 3.74-3.74], [3.98-3.98+0.03, 0, 4.31-3.74], [3.98-3.98+0.03, 0, 5.01-3.74], [4.08-3.98+0.03, 0, 5.53-3.74]]);
var mappingcurvebase = ROTATIONAL_SURFACE(profilecurvebase);
var surfacecurvebase1 = S([0,1,2])([1.5,1.5,1.5])(T([2])([6.2])(MAP(mappingcurvebase)(domainbase)));
var surfacecurvebase2 = S([0,1,2])([1.5,1.5,1.5])(T([2])([1.79])(R([1,2])([PI,PI])(MAP(mappingcurvebase)(domainbase))));
var middlelamp = EXTRUDE([12])(DISK(0.06)(20));
var bodylamp = COLOR(colorlamp)(STRUCT([surfacecurvebase1,surfacecurvebase2, middlelamp]));

//********************************************************************************************************
//Wire

var wire1 = EXTRUDE([0.2])(DISK(0.125)(50))
var wire2 = EXTRUDE([8])(DISK(0.1)(50))
var cube = T([0,1,2])([-0.75,-0.25,4.5])(CUBOID([1.5,0.5,1.5]));
var wire = T([1])([-1.13])(S([0,1,2])([0.3,0.3,0.3])(R([1,2])([PI/2,PI/2])(STRUCT([wire1,wire2,cube]))));
var wirelamp = COLOR([0,0,0,1])(wire);

//********************************************************************************************************
//Model

var model = STRUCT([topbase, bodylamp, wirelamp]);
DRAW(model);