//GLUON poltroncina - Marc Newson
//********************************************************************************************************
//Base sofa

var domainbase = DOMAIN([[0,1],[0,2*PI]])([40,40]);
colormetal = [0.5,0.5,0.5,1]
colorpillow = [1,1,0,1]

var profilecurvebase = BEZIER(S0)([[3.73-3.73+0.12, 0, 1.68],[3.73-3.73+0.12, 0, 1.81], [3.72-3.73+0.12, 0, 2.02], [3.8-3.73+0.12, 0, 2.38], [4.08-3.73+0.12, 0, 2.46]]);
var mappingcurvebase = ROTATIONAL_SURFACE(profilecurvebase);
var surfacecurvebase = COLOR(colormetal)(MAP(mappingcurvebase)(domainbase));
closebase1 = COLOR(colormetal)(T([2])([2.46])(DISK(0.47)(50)));

var profilebase = BEZIER(S0)([[3.86-3.86+0.2, 0, 1.79], [4.37-3.86+0.2, 0, 1.76], [4.69-3.86+0.2, 0, 1.72], [4.7-3.86+0.2, 0, 1.59]]);
var mappingbase = ROTATIONAL_SURFACE(profilebase);
var surfacebase = COLOR(colormetal)(MAP(mappingbase)(domainbase));
closebase2 = COLOR([0,0,0,1])(T([2])([1.59])(DISK(1.04)(50)));

base = T([0,1,2])([3.55,0.022,-1.43])(R([1,2])([-PI/2,-PI/2])(STRUCT([closebase1, closebase2, surfacecurvebase, surfacebase])));

//********************************************************************************************************
//Sofa vine
var domainv = DOMAIN([[0,1],[0,2*PI]])([30,30]);
var lvine = 2.86;

var profilev = BEZIER(S0)([[0-1.73, 0, 0], [0.27-1.73, 0,  0.36], [0.6-1.73, 0, 0.69], [1.73-1.73, 0, 0.67]]);
var mappingv = ROTATIONAL_SURFACE(profilev);

var vined = S([0,1,2])([0.05,0.05,0.05])(MAP(mappingv)(domainv));
var vinel = R([1,2])([PI,PI])(vined);

var vined1 = T([0,1,2])([1.76,4.99,0])(vined);
var vined2 = T([0,1,2])([2.22,3.53,0])(vined);
var vined3 = T([0,1,2])([3.03,2.99,0])(vined);
var vined4 = T([0,1,2])([4.59,3.20,0])(vined);
var vinel5 = T([0,1,2])([1.76,4.99,-lvine])(vinel);
var vinel6 = T([0,1,2])([2.22,3.53,-lvine])(vinel);
var vinel7 = T([0,1,2])([3.03,2.99,-lvine])(vinel);
var vinel8 = T([0,1,2])([4.59,3.20,-lvine])(vinel);

var vine = STRUCT([vined1,vined2,vined3,vined4,vinel5,vinel6,vinel7,vinel8]);

//********************************************************************************************************
//Sofa side

var domain = PROD1x1([INTERVALS(1)(30),INTERVALS(1)(30)]);
var domain2 = DOMAIN([[0,1],[0,1]])([30,30]);
var lsideext = 2.86
var lsideint = 2.46
var lsideintext = 0.20

//***
//side d

var c0d = BEZIER(S0)([[2.42, 2.9, 0], [1.3, 3.59, 0], [1.24, 5.18, 0], [1.68, 5.22, 0]]);
var c1d = BEZIER(S0)([[1.68, 5.22, 0],[2.17, 5.41, 0],[2.62, 4.37, 0],[2.57, 3.81, 0]]);
var c2d = BEZIER(S0)([[2.57, 3.81, 0], [2.58, 3.66, 0], [2.53, 3.45, 0], [2.7, 3.36, 0]]);
var c3d = BEZIER(S0)([[2.42, 2.9, 0],[2.7, 3.36, 0]]);

var c4d = BEZIER(S0)([[2.15, 3.69, 0], [1.82, 3.6, 0], [1.51, 4.66, 0], [1.81, 4.75, 0]]);
var c5d = BEZIER(S0)([[1.81, 4.75, 0],[2.17, 4.89, 0],[2.5, 3.85, 0],[2.15, 3.69, 0]]);
var c6d = [2.15, 3.69, 0]

var lateral0d = BEZIER(S1)([c0d,c4d]);
var lateral1d = BEZIER(S1)([c1d,c5d]);
var lateral2d = BEZIER(S1)([c2d,c6d]);
var lateral3d = BEZIER(S1)([c3d,c6d]);

var fuse0d = MAP(lateral0d)(domain2);
var fuse1d = MAP(lateral1d)(domain2);
var fuse2d = MAP(lateral2d)(domain2);
var fuse3d = MAP(lateral3d)(domain2);

var c7d = BEZIER(S0)([[2.42, 2.9, 0], [3.39, 2.26, 0], [4.95, 2.67, 0], [4.82, 3.2, 0]]);
var c8d = BEZIER(S0)([[3.03, 3.34, 0], [3.57, 3.68, 0], [4.69, 3.65, 0], [4.82, 3.2, 0]]);
var c9d = BEZIER(S0)([[2.7, 3.36, 0], [2.79, 3.29, 0], [2.89, 3.29, 0], [3.03, 3.34, 0]]);

var c10d = BEZIER(S0)([[3.26, 2.98, 0], [3.39, 2.63, 0], [4.4, 2.84, 0], [4.34, 3.11, 0]]);
var c11d = BEZIER(S0)([[3.26, 2.98, 0], [3.26, 3.3, 0], [4.24, 3.48, 0], [4.34, 3.11, 0]]);
var c12d = [3.26, 2.98, 0]

var lateral4d = BEZIER(S1)([c7d,c10d]);
var lateral5d = BEZIER(S1)([c8d,c11d]);
var lateral6d = BEZIER(S1)([c9d,c12d]);
var lateral7d = BEZIER(S1)([c3d,c12d]);

var fuse4d = MAP(lateral4d)(domain2);
var fuse5d = MAP(lateral5d)(domain2);
var fuse6d = MAP(lateral6d)(domain2);
var fuse7d = MAP(lateral7d)(domain2);

//***
//side dint

var c0dint = BEZIER(S0)([[2.42, 2.88, -lsideintext], [1.42, 3.42, -lsideintext], [1.13, 5.08, -lsideintext], [1.63, 5.24, -lsideintext]]);
var c1dint = BEZIER(S0)([[1.63, 5.24, -lsideintext], [2.21, 5.46, -lsideintext], [2.66, 4.3, -lsideintext], [2.6, 3.84, -lsideintext]]);
var c2dint = BEZIER(S0)([[2.6, 3.84, -lsideintext], [2.59, 3.66, -lsideintext], [2.58, 3.46, -lsideintext], [2.71, 3.38, -lsideintext]]);
var c3dint = BEZIER(S0)([[2.42, 2.88, -lsideintext],[2.71, 3.38, -lsideintext]]);

var c4dint = BEZIER(S0)([[2.15, 3.69, -lsideintext], [1.82, 3.6, -lsideintext], [1.51, 4.66, -lsideintext], [1.81, 4.75, -lsideintext]]);
var c5dint = BEZIER(S0)([[1.81, 4.75, -lsideintext],[2.17, 4.89, -lsideintext], [2.5, 3.85, -lsideintext], [2.15, 3.69, -lsideintext]]);
var c6dint = [2.15, 3.69, -lsideintext]

var lateral0dint = BEZIER(S1)([c0dint,c4dint]);
var lateral1dint = BEZIER(S1)([c1dint,c5dint]);
var lateral2dint = BEZIER(S1)([c2dint,c6dint]);
var lateral3dint = BEZIER(S1)([c3dint,c6dint]);

var fuse0dint = MAP(lateral0dint)(domain2);
var fuse1dint = MAP(lateral1dint)(domain2);
var fuse2dint = MAP(lateral2dint)(domain2);
var fuse3dint = MAP(lateral3dint)(domain2);

var c7dint = BEZIER(S0)([[2.42, 2.88, -lsideintext], [3.36, 2.2, -lsideintext], [4.95, 2.65, -lsideintext], [4.87, 3.17, -lsideintext]]);
var c8dint = BEZIER(S0)([[3.03, 3.36, -lsideintext],[3.29, 3.61, -lsideintext],[4.77, 3.84, -lsideintext],[4.87, 3.17, -lsideintext]]);
var c9dint = BEZIER(S0)([[2.71, 3.38, -lsideintext], [2.79, 3.31, -lsideintext], [2.9, 3.28, -lsideintext], [3.03, 3.36, -lsideintext]]);

var c10dint = BEZIER(S0)([[3.26, 2.98, -lsideintext], [3.39, 2.63, -lsideintext], [4.4, 2.84, -lsideintext], [4.34, 3.11, -lsideintext]]);
var c11dint = BEZIER(S0)([[3.26, 2.98, -lsideintext], [3.26, 3.3, -lsideintext], [4.24, 3.48, -lsideintext], [4.34, 3.11, -lsideintext]]);
var c12dint = [3.26, 2.98, -lsideintext]

var lateral4dint = BEZIER(S1)([c7dint,c10dint]);
var lateral5dint = BEZIER(S1)([c8dint,c11dint]);
var lateral6dint = BEZIER(S1)([c9dint,c12dint]);
var lateral7dint = BEZIER(S1)([c3dint,c12dint]);

var fuse4dint = MAP(lateral4dint)(domain2);
var fuse5dint = MAP(lateral5dint)(domain2);
var fuse6dint = MAP(lateral6dint)(domain2);
var fuse7dint = MAP(lateral7dint)(domain2);

//***
//side l

var c0l = BEZIER(S0)([[2.42, 2.9, -lsideext], [1.3, 3.59, -lsideext], [1.24, 5.18, -lsideext], [1.68, 5.22, -lsideext]]);
var c1l = BEZIER(S0)([[1.68, 5.22, -lsideext],[2.17, 5.41, -lsideext], [2.62, 4.37, -lsideext],[2.57, 3.81, -lsideext]]);
var c2l = BEZIER(S0)([[2.57, 3.81, -lsideext], [2.58, 3.66, -lsideext], [2.53, 3.45, -lsideext], [2.7, 3.36, -lsideext]]);
var c3l = BEZIER(S0)([[2.42, 2.9, -lsideext],[2.7, 3.36, -lsideext]]);

var c4l = BEZIER(S0)([[2.15, 3.69, -lsideext], [1.82, 3.6, -lsideext], [1.51, 4.66, -lsideext], [1.81, 4.75, -lsideext]]);
var c5l = BEZIER(S0)([[1.81, 4.75, -lsideext],[2.17, 4.89, -lsideext], [2.5, 3.85, -lsideext], [2.15, 3.69, -lsideext]]);
var c6l = [2.15, 3.69, -lsideext]

var lateral0l = BEZIER(S1)([c0l,c4l]);
var lateral1l = BEZIER(S1)([c1l,c5l]);
var lateral2l = BEZIER(S1)([c2l,c6l]);
var lateral3l = BEZIER(S1)([c3l,c6l]);

var fuse0l = MAP(lateral0l)(domain2);
var fuse1l = MAP(lateral1l)(domain2);
var fuse2l = MAP(lateral2l)(domain2);
var fuse3l = MAP(lateral3l)(domain2);

var c7l = BEZIER(S0)([[2.42, 2.9, -lsideext], [3.39, 2.26, -lsideext], [4.95, 2.67, -lsideext], [4.82, 3.2, -lsideext]]);
var c8l = BEZIER(S0)([[3.03, 3.34, -lsideext], [3.57, 3.68, -lsideext], [4.69, 3.65, -lsideext], [4.82, 3.2, -lsideext]]);
var c9l = BEZIER(S0)([[2.7, 3.36, -lsideext], [2.79, 3.29, -lsideext], [2.89, 3.29, -lsideext], [3.03, 3.34, -lsideext]]);

var c10l = BEZIER(S0)([[3.26, 2.98, -lsideext], [3.39, 2.63, -lsideext], [4.4, 2.84, -lsideext], [4.34, 3.11, -lsideext]]);
var c11l = BEZIER(S0)([[3.26, 2.98, -lsideext], [3.26, 3.3, -lsideext], [4.24, 3.48, -lsideext], [4.34, 3.11, -lsideext]]);
var c12l = [3.26, 2.98, -lsideext]

var lateral4l = BEZIER(S1)([c7l,c10l]);
var lateral5l = BEZIER(S1)([c8l,c11l]);
var lateral6l = BEZIER(S1)([c9l,c12l]);
var lateral7l = BEZIER(S1)([c3l,c12l]);

var fuse4l = MAP(lateral4l)(domain2);
var fuse5l = MAP(lateral5l)(domain2);
var fuse6l = MAP(lateral6l)(domain2);
var fuse7l = MAP(lateral7l)(domain2);

//***
//side lint

var domain2 = DOMAIN([[0,1],[0,1]])([50,50]);
var c0lint = BEZIER(S0)([[2.42, 2.88, -lsideintext-lsideint], [1.42, 3.42, -lsideintext-lsideint], [1.13, 5.08, -lsideintext-lsideint], [1.63, 5.24, -lsideintext-lsideint]]);
var c1lint = BEZIER(S0)([[1.63, 5.24, -lsideintext-lsideint], [2.21, 5.46, -lsideintext-lsideint], [2.66, 4.3, -lsideintext-lsideint], [2.6, 3.84, -lsideintext-lsideint]]);
var c2lint = BEZIER(S0)([[2.6, 3.84, -lsideintext-lsideint], [2.59, 3.66, -lsideintext-lsideint], [2.58, 3.46, -lsideintext-lsideint], [2.71, 3.38, -lsideintext-lsideint]]);
var c3lint = BEZIER(S0)([[2.42, 2.88, -lsideintext-lsideint],[2.71, 3.38, -lsideintext-lsideint]]);

var c4lint = BEZIER(S0)([[2.15, 3.69, -lsideintext-lsideint], [1.82, 3.6, -lsideintext-lsideint], [1.51, 4.66, -lsideintext-lsideint], [1.81, 4.75, -lsideintext-lsideint]]);
var c5lint = BEZIER(S0)([[1.81, 4.75, -lsideintext-lsideint],[2.17, 4.89, -lsideintext-lsideint], [2.5, 3.85, -lsideintext-lsideint], [2.15, 3.69, -lsideintext-lsideint]]);
var c6lint = [2.15, 3.69, -lsideintext-lsideint]

var lateral0lint = BEZIER(S1)([c0lint,c4lint]);
var lateral1lint = BEZIER(S1)([c1lint,c5lint]);
var lateral2lint = BEZIER(S1)([c2lint,c6lint]);
var lateral3lint = BEZIER(S1)([c3lint,c6lint]);

var fuse0lint = MAP(lateral0lint)(domain2);
var fuse1lint = MAP(lateral1lint)(domain2);
var fuse2lint = MAP(lateral2lint)(domain2);
var fuse3lint = MAP(lateral3lint)(domain2);

var c7lint = BEZIER(S0)([[2.42, 2.88, -lsideintext-lsideint], [3.36, 2.2, -lsideintext-lsideint], [4.95, 2.65, -lsideintext-lsideint], [4.87, 3.17, -lsideintext-lsideint]]);
var c8lint = BEZIER(S0)([[3.03, 3.36, -lsideintext-lsideint],[3.29, 3.61, -lsideintext-lsideint],[4.77, 3.84, -lsideintext-lsideint],[4.87, 3.17, -lsideintext-lsideint]]);
var c9lint = BEZIER(S0)([[2.71, 3.38, -lsideintext-lsideint], [2.79, 3.31, -lsideintext-lsideint], [2.9, 3.28, -lsideintext-lsideint], [3.03, 3.36, -lsideintext-lsideint]]);

var c10lint = BEZIER(S0)([[3.26, 2.98, -lsideintext-lsideint], [3.39, 2.63, -lsideintext-lsideint], [4.4, 2.84, -lsideintext-lsideint], [4.34, 3.11, -lsideintext-lsideint]]);
var c11lint = BEZIER(S0)([[3.26, 2.98, -lsideintext-lsideint], [3.26, 3.3, -lsideintext-lsideint], [4.24, 3.48, -lsideintext-lsideint], [4.34, 3.11, -lsideintext-lsideint]]);
var c12lint = [3.26, 2.98, -lsideintext-lsideint]

var lateral4lint = BEZIER(S1)([c7lint,c10lint]);
var lateral5lint = BEZIER(S1)([c8lint,c11lint]);
var lateral6lint = BEZIER(S1)([c9lint,c12lint]);
var lateral7lint = BEZIER(S1)([c3lint,c12lint]);

var fuse4lint = MAP(lateral4lint)(domain2);
var fuse5lint = MAP(lateral5lint)(domain2);
var fuse6lint = MAP(lateral6lint)(domain2);
var fuse7lint = MAP(lateral7lint)(domain2);

//***

var laterald1 = BEZIER(S1)([c0d,c0dint]);
var laterald2 = BEZIER(S1)([c1d,c1dint]);
var laterald3 = BEZIER(S1)([c2d,c2dint]);
var laterald4 = BEZIER(S1)([c7d,c7dint]);
var laterald5 = BEZIER(S1)([c8d,c8dint]);
var laterald6 = BEZIER(S1)([c9d,c9dint]);
var laterall1 = BEZIER(S1)([c0l,c0lint]);
var laterall2 = BEZIER(S1)([c1l,c1lint]);
var laterall3 = BEZIER(S1)([c2l,c2lint]);
var laterall4 = BEZIER(S1)([c7l,c7lint]);
var laterall5 = BEZIER(S1)([c8l,c8lint]);
var laterall6 = BEZIER(S1)([c9l,c9lint]);
var lateralint1 = BEZIER(S1)([c4d,c4dint]);
var lateralint2 = BEZIER(S1)([c5d,c5dint]);
var lateralint3 = BEZIER(S1)([c10d,c10dint]);
var lateralint4 = BEZIER(S1)([c11d,c11dint]);
var lateralint5 = BEZIER(S1)([c4l,c4lint]);
var lateralint6 = BEZIER(S1)([c5l,c5lint]);
var lateralint7 = BEZIER(S1)([c10l,c10lint]);
var lateralint8 = BEZIER(S1)([c11l,c11lint]);

var fuse1 = MAP(laterald1)(domain2);
var fuse2 = MAP(laterald2)(domain2);
var fuse3 = MAP(laterald3)(domain2);
var fuse4 = MAP(laterald4)(domain2);
var fuse5 = MAP(laterald5)(domain2);
var fuse6 = MAP(laterald6)(domain2);
var fuse7 = MAP(laterall1)(domain2);
var fuse8 = MAP(laterall2)(domain2);
var fuse9 = MAP(laterall3)(domain2);
var fuse10 = MAP(laterall4)(domain2);
var fuse11 = MAP(laterall5)(domain2);
var fuse12 = MAP(laterall6)(domain2);
var fuse13 = MAP(lateralint1)(domain2);
var fuse14 = MAP(lateralint2)(domain2);
var fuse15 = MAP(lateralint3)(domain2);
var fuse16 = MAP(lateralint4)(domain2);
var fuse17 = MAP(lateralint5)(domain2);
var fuse18 = MAP(lateralint6)(domain2);
var fuse19 = MAP(lateralint7)(domain2);
var fuse20 = MAP(lateralint8)(domain2);

var latside = STRUCT([fuse1,fuse2,fuse3,fuse4,fuse5,fuse6,fuse7,fuse8,fuse9,fuse10,
		fuse11,fuse12,fuse13,fuse14,fuse15,fuse16,fuse17,fuse18,fuse19,fuse20]);

//***
//side

var side = COLOR(colormetal)(STRUCT([fuse0d,fuse1d,fuse2d,fuse3d,fuse4d,fuse5d,fuse6d,fuse7d,
		    fuse0l,fuse1l,fuse2l,fuse3l,fuse4l,fuse5l,fuse6l,fuse7l,
		    fuse0dint,fuse1dint,fuse2dint,fuse3dint,fuse4dint,fuse5dint,fuse6dint,fuse7dint,
		    fuse0lint,fuse1lint,fuse2lint,fuse3lint,fuse4lint,fuse5lint,fuse6lint,fuse7lint,
		    latside,vine]));

//********************************************************************************************************
//Sofa pillowUP

var domainp = PROD1x1([INTERVALS(1)(40),INTERVALS(1)(40)]);
var domainp2 = DOMAIN([[0,1],[0,1]])([40,40]);
var lpillow = 2.46
var lhalfpillow = 1.23
colormetal = [0.5,0.5,0.5,1]
colorpillow = [1,1,0,1]

var c0lsof = BEZIER(S0)([[2.3, 3.19, -lsideintext-lsideint], [1.63, 2.95,  -lsideintext-lsideint], [1.13, 5.08, -lsideintext-lsideint], [1.63, 5.24, -lsideintext-lsideint]]);
var cmiddledsof0 = BEZIER(S0)([[2.34, 3.12,  -lsideintext-lhalfpillow],[1.6, 2.75,  -lsideintext-lhalfpillow],[0.92, 5.19,  -lsideintext-lhalfpillow],[1.63, 5.31,  -lsideintext-lhalfpillow]]);
var c0dsof = BEZIER(S0)([[2.3, 3.19, -lsideintext], [1.63, 2.95,  -lsideintext], [1.13, 5.08, -lsideintext], [1.63, 5.24, -lsideintext]]);

var c1lsof = BEZIER(S0)([[1.63, 5.24, -lsideintext-lsideint], [2.35, 5.62, -lsideintext-lsideint], [2.99, 3.42, -lsideintext-lsideint], [2.3, 3.19, -lsideintext-lsideint]]);
var cmiddledsof1 = BEZIER(S0)([[1.63, 5.31, -lsideintext-lhalfpillow],[2.41, 5.67, -lsideintext-lhalfpillow],[3.13, 3.24, -lsideintext-lhalfpillow],[2.34, 3.12, -lsideintext-lhalfpillow]]);
var c1dsof = BEZIER(S0)([[1.63, 5.24, -lsideintext], [2.35, 5.62, -lsideintext], [2.99, 3.42, -lsideintext], [2.3, 3.19, -lsideintext]]);

var pillow0 = MAP(BEZIER(S1)([c0lsof,cmiddledsof0,c0dsof]))(domainp);
var pillow1 = MAP(BEZIER(S1)([c1lsof,cmiddledsof1,c1dsof]))(domainp);

var lateral2 = BEZIER(S1)([c0lsof,c1lsof]);
var lateral3 = BEZIER(S1)([c0dsof,c1dsof]);

var pillow2 = MAP(lateral2)(domainp2);
var pillow3 = MAP(lateral3)(domainp2);

var pillowup = T([0,1])([0.01,-0.025])(STRUCT([pillow0, pillow1, pillow2, pillow3]));

//********************************************************************************************************
//Sofa pillowDOWN

var c7lsof = BEZIER(S0)([[2.74, 2.95, -lsideintext-lsideint], [2.85, 2.24, -lsideintext-lsideint], [4.94, 2.54, -lsideintext-lsideint], [4.87, 3.17, -lsideintext-lsideint]]);
var cmiddledsof7 = BEZIER(S0)([[2.66, 2.99, -lsideintext-lhalfpillow], [2.55, 2.14, -lsideintext-lhalfpillow], [5.06, 2.41, -lsideintext-lhalfpillow], [4.93, 3.19, -lsideintext-lhalfpillow]]);
var c7dsof = BEZIER(S0)([[2.74, 2.95, -lsideintext], [2.85, 2.24, -lsideintext], [4.94, 2.54, -lsideintext], [4.87, 3.17, -lsideintext]]);

var c8lsof = BEZIER(S0)([[2.74, 2.95, -lsideintext-lsideint],[2.74, 3.7, -lsideintext-lsideint],[4.88, 3.86, -lsideintext-lsideint],[4.87, 3.17, -lsideintext-lsideint]]);
var cmiddledsof8 = BEZIER(S0)([[2.66, 2.99, -lsideintext-lhalfpillow], [2.64, 3.78, -lsideintext-lhalfpillow], [5, 3.94, -lsideintext-lhalfpillow], [4.93, 3.19, -lsideintext-lhalfpillow]]);
var c8dsof = BEZIER(S0)([[2.74, 2.95, -lsideintext],[2.74, 3.7, -lsideintext],[4.88, 3.86, -lsideintext],[4.87, 3.17, -lsideintext]]);

var pillow7 = MAP(BEZIER(S1)([c7lsof, cmiddledsof7, c7dsof]))(domainp);
var pillow8 = MAP(BEZIER(S1)([c8lsof, cmiddledsof8, c8dsof]))(domainp);

var lateral9 = BEZIER(S1)([c7lsof,c8lsof]);
var lateral10 = BEZIER(S1)([c7dsof,c8dsof]);

var pillow9 = MAP(lateral9)(domainp2);
var pillow10 = MAP(lateral10)(domainp2);

var pillowdown = T([0])([-0.012])(STRUCT([pillow7, pillow8, pillow9, pillow10]));

//********************************************************************************************************
//Pillow

var pillow = COLOR(colorpillow)(STRUCT([pillowup, pillowdown]));

//********************************************************************************************************
//Sofa

var unionsofa = STRUCT([side, pillow, vine]);

//********************************************************************************************************
//MODEL

var model = STRUCT([unionsofa, base]);
DRAW(model);