function lar_to_obj(larModel){
	
	var s = "";
	
	var v = larModel[0];
	
	var fs= larModel[1];
	
	for (var i=0; i<v.length; i++){
	
		if (v[i][2]!=undefined)
			s = s + "V "+" "+v[i][0]+" "+v[i][1]+" "+v[i][2]+"\n";
		else
			s = s + "V "+" "+v[i][0]+" "+v[i][1]+" 0 \n";
	}

	for(var i=0; i<v.length; i++){
		
		for(var j=0; j<fv[i].length; j++){
			
			if(j===0) 
			
				s = s + "F "+fv[i][j]+" ";
				
			else if(j===k-1)
			
				s = s + fv[i][j]+"\n";
			
			else
				
				s = s + fv[i][j]+" ";
 		}
	}
	return s;
}

/* 
* Ex. dal link: https://github.com/cvdlab-cg/lessons/blob/master/lessons/2013-06-04/examples.py
*/

FV = [[5,6,7,8],
      [0,5,8],
      [0,4,5],
      [1,2,4,5],
      [2,3,5,6],
      [0,8,7], 
      [3,6,7], 
      [1,2,3], 
      [0,1,4]];
      
V = [[0,6],
     [0,0],
     [3,0],
     [6,0,4],
     [0,3,4],
     [3,3],
     [6,3],
     [6,6],
     [3,6]];

var larModel = [V,FV]
var object = lar_to_obj(larModel);