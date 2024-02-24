const newObject={}
body=document.querySelector('body')

function recursiveScroll(obj,i,ms, Rs){
	//console.log('rS started\n',
				//`counter=${obj.counter}\n`,)
	//console.time()
	if (obj.counter>0){
		window.setTimeout(()=>{
			obj.counter-=1
			if(obj.downScroll){body.scrollTop+=obj.scrollPowerArray[i]}
			else 			  {body.scrollTop-=obj.scrollPowerArray[i]}
			i+=1
			//console.timeEnd()
			recursiveScroll(obj,i,ms,Rs)
			},ms)
	}
	else if(obj.counter===0){enableManualScroll()
		if (obj.callOptionalFunction!==false){
			obj.callOptionalFunction()}}
	//console.log('rS finished')
}



function scrollSmooth(distance, timeInMs, finalOnees, optionalFunction=false){
	disableManualScroll()
	console.log('started')
	let time=timeInMs
	let finalOnes=finalOnees
	let negativeDistance=false
	if (distance<0){negativeDistance=true}
	const absDistance=Math.abs(distance)
	let Tscrolls=0		//Total
	let scrollPower=0
	let ms=5		//minimum is 4 and 5, 10 for stability
	if (time<ms){time=ms}

	if (absDistance<=time/ms){
		scrollPower=1
		Tscrolls=absDistance
		ms=time/absDistance
		RemainingScrolls=0
	}

	else if(absDistance>time/ms){
		scrollPower=Math.floor(absDistance/(time/ms))
		Tscrolls=Math.floor(time/ms)
		ms=5
		RemainingScrolls=absDistance%(Math.floor(time/ms))
	}

	//if(finalOnes>Tscrolls){finaOnes=Math.floor(Tscrolls/2)}
/*
	for(let i=0;i!==Tscrolls;i++){
		window.setTimeout(()=>{
		body.scrollTop-=scrollPower
		//needs a type of recursion
		//all of them are being executed at the same time
		//let the other be executed only when the first finished
		}, ms)
	}
*/
	newObject.counter=Tscrolls
	//console.log(RemainingScrolls)
	newObject.scrollPowerArray=easeInOutArray(scrollPower,Tscrolls, RemainingScrolls, finalOnes)
	newObject.callOptionalFunction=optionalFunction
	newObject.downScroll=negativeDistance
	let i =0
	recursiveScroll(newObject,i,ms, RemainingScrolls)

	console.log(`absDistance=${absDistance}\n`,
		`Tscrolls=${Tscrolls}\n`,
		`scrollPower=${scrollPower}\n`,
		`ms=${ms}\n`)
		
}
	


//THINGS TO DO/Problems to solve
//1. Its possible to scroll during the "animation" (DONE)
//2. Its possible to trigger the "animation" multiple time. Disable stacking. (may not be needed)
//3. Smooth edges, speed middle (EaseInOutArray.js done)

//////////////////////////////////////////////////////////////////////////////////
//DISABLING SCROLL
//(as possible)

const moveKeys=[32,33,34,35,36,38,40]
//keys for movement:
//up: 38, down: 40,
//spacebar: 32, pageup: 33, pagedown: 34, end: 35, home: 36

function checkMK(e){
	if(moveKeys.includes(e.keyCode)){
		e.preventDefault()
		console.log('stopped')
	}
}

//test for the third option of aEL
let objectNotation=false

try{
	//from here on, idk exactly what is going on
	const options={
		get passive(){
			objectNotation=true
			return false
		}
	} 

	window.addEventListener('test', null, options)
	window.removeEventListener('test', null, options)
}catch(e){}

setPassiveToFalse= objectNotation? {passive:false}: false

function pD(e){e.preventDefault()}

function disableManualScroll(){
	console.log('DISABLED')
	window.addEventListener('touchmove', pD, setPassiveToFalse)
	window.addEventListener('wheel', pD, setPassiveToFalse)
	window.addEventListener('keydown', checkMK)

}

function enableManualScroll(){
	console.log('ENABLED')
	window.removeEventListener('touchmove', pD, setPassiveToFalse)
	window.removeEventListener('wheel', pD, setPassiveToFalse)
	window.removeEventListener('keydown', checkMK)

}
