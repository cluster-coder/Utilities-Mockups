function easeInOutArray(Averagenumber, Arraysize, Rnumbers, finalOnees=0){
//declarations
	//console.log('called easeInOutArray')
	let finalOnes=1
	if (Arraysize>2){finalOnes=finalOnees}
	let pure=Arraysize-finalOnes
	let Avnumber=Averagenumber
	let modified=total=finalOnes
	let remaining=Rnumbers+ (Avnumber-1)*modified

	let array=[]
	let rq=20 	//repeat quantity
	let bi=0 	//beggining index
	let ei=0 	//ending index
	let number=0

	const multiplier=Math.floor(Avnumber/3)+1


	function addToArray(position){
		if (position==='beggining'){
			array.splice(bi, 0, number)
			bi+=1
		}
		else if(position==='ending'){
			array.splice((array.length-1-ei), 0, number)
			ei+=1
		}
		modified+=1
		pure-=1
		total+=1
		remaining+=Avnumber-number
	}


	//console.log('starting ease')
	//making the eased array:

	while(total<Arraysize){
		if(number<Avnumber){
			if (Avnumber-number<=multiplier){number+=1} 	//to avoid overshooting
			else{number+=1*multiplier}
		/////////////BEGGINING///////////////////
			if (rq>1){
				for(let i=rq; i!==0; i--) {addToArray('beggining')}
				rq-=2
			}
			else{
				addToArray('beggining')
			}
		/////////////ENDING///////////////
			if (number>1 && pure>0){
				for(let i=2; i!==0; i--){addToArray('ending')}
			}
		}
		///////MIDDLE////////
		else{
			array.splice(bi, 0, number)
			bi+=1
			total+=1
		}
		if (remaining>=pure && pure>0){
			Avnumber+= Math.floor(remaining/pure)
			remaining-= Math.floor(remaining/pure)*pure
		}
	}

	//Distributing the remaining
	if (remaining>=array.length){
		evenDistribution=Math.floor(remaining/array.length)
		for(let i in array){array[i]+=evenDistribution}
		remaining-=array.length*evenDistribution
	}

	halfRemaining=Math.floor((remaining-1)/2)
	if(pure>0){middle= array.indexOf(Avnumber)+1+Math.ceil(pure/2)}
	else{middle=Math.floor(array.length/2)}
	FI=middle-halfRemaining 	//first index
	LI=middle+halfRemaining+1 	//last index

	if (remaining%2===0){
		if(pure%2===0){
			LI+=1
		}
		else{
			FI-=1
		}
	}/*
	console.log(`halfRemaining ${halfRemaining}`)
	console.log(`middle ${middle}`)
	console.log(`FI ${FI}`)
	console.log(`LI ${LI}`)*/

	for (let i=FI;i<LI;i++){
		array[i]+=1
		//console.log(array[i])
	}
	///wraping with the 1s
	for(let i=finalOnes;i!==0;i--){
		array.push(1)
	}/*
	console.log(`Averagenumber ${Averagenumber}`)
	console.log(`Arraysize ${Arraysize}`)
	console.log(`Rnumbers ${Rnumbers}`)
	console.log(`pure ${pure}`)
	console.log(`Avnumber ${Avnumber}`)
	console.log(`modified ${modified}`)
	console.log(`total ${total}`)
	console.log(`remaining ${remaining}`)
	console.log(`number ${number}`)
	console.log(`multiplier ${multiplier}`)
/*
	suma=0
	for(item of array){suma+=item}
	/*console.log(suma)
	console.log(array)*/
	return array
}