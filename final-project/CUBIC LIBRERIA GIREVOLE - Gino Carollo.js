//Helice Floorlamp - Marc Newson
//********************************************************************************************************
//Bookcase

var dplain = 0.025
var dtablet = 0.08
var hbigplain = 0.95
var hlittleplain = 0.74
var lfloor = 0.89 + dtablet + dtablet
var bookcasecolor = [0.2, 0.2, 0.2, 1]

var p = 0.27
var sg = 0.62

var m = 0.42
var sm = 0.47

var g = 0.70
var sp = 0.19 

var facade1 = T([2])([0])(STRUCT([SIMPLEX_GRID([[-dtablet, -sp, g, dtablet], [-dplain, -hbigplain, -dplain, hlittleplain, -dplain, -hbigplain, -dplain, hlittleplain], [dtablet]]),
		      SIMPLEX_GRID([[dtablet, m,-sm,dtablet], [-dplain, hbigplain, -dplain, -hlittleplain, -dplain, -hbigplain, -dplain, -hlittleplain, -dplain, hbigplain, -dplain], [dtablet]])]));

var facade2 = T([0,2])([dtablet,dtablet])(R([0,2])([-PI/2,-PI/2])(T([0])([-lfloor])(STRUCT([SIMPLEX_GRID([[dtablet, p,-sg,dtablet], [dplain, hbigplain, dplain, -hlittleplain, dplain, -hbigplain, dplain, -hlittleplain, dplain, hbigplain, dplain], [dtablet]]),
                      SIMPLEX_GRID([[dtablet, sm], [-dplain, -hbigplain, -dplain, -hlittleplain, dplain, hbigplain], [dtablet]])]))));

var facade3 = T([0,2])([lfloor-dtablet, dtablet])(R([0,2])([PI/2, PI/2])(STRUCT([SIMPLEX_GRID([[dtablet, p,-sg, dtablet], [dplain, hbigplain], [dtablet]]),		      
		      SIMPLEX_GRID([[-dtablet, -sg, p, dtablet], [-dplain, -hbigplain, -dplain, hlittleplain], [dtablet]]),
		      SIMPLEX_GRID([[dtablet, -sg, p, dtablet], [-dplain, -hbigplain, -dplain, -hlittleplain, dplain, -hbigplain, -dplain, hlittleplain], [dtablet]]),
		      SIMPLEX_GRID([[dtablet, m, -sm, dtablet], [-dplain, -hbigplain, -dplain, -hlittleplain, dplain, -hbigplain, -dplain, -hlittleplain, -dplain, hbigplain], [dtablet]])])));	

var facade4 = T([0,2])([lfloor, -lfloor+dtablet+dtablet])(R([0,2])([PI,PI])(SIMPLEX_GRID([[dtablet, m,-sm,dtablet], [dplain, hbigplain, dplain, -hlittleplain, dplain, hbigplain, dplain, -hlittleplain, dplain, hbigplain, dplain], [dtablet]])));

var floors = T([2])([-lfloor+dtablet])(SIMPLEX_GRID([[lfloor], [dplain, -hbigplain, dplain, -hlittleplain, dplain, -hbigplain, dplain, -hlittleplain, dplain, -hbigplain, dplain], [lfloor]]));

var bookcasemodel = COLOR(bookcasecolor)(STRUCT([facade1, facade2,facade3,facade4, floors]));

//********************************************************************************************************
//Bookcase base

var bookcasebase = T([0,2])([lfloor/2,-lfloor/2+dtablet])(R([1,2])([PI/2, PI/2])( EXTRUDE([0.04])(DISK(lfloor/2-dtablet)(50))));

//********************************************************************************************************
//Model

var bookcaseL = R([0,2])([PI/2,PI/2])(STRUCT([bookcasemodel, bookcasebase]));
var bookcaseR = T([0,2])([lfloor-3-2*p,-lfloor])(R([0,2])([-PI/2,-PI/2])(STRUCT([bookcasemodel, bookcasebase])));

var model = T([0])([4])(S([1])([1.3])(STRUCT([bookcaseL, bookcaseR])));
DRAW(model);