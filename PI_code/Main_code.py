import soil1
import dhhht
import ultrasonic_distance
import time
import moto
from firebase import firebase

firebase=firebase.FirebaseApplication('https://farming-48619.firebaseio.com/')
while True:
	b=firebase.get('/iot','motor')
	print(b)
	moto.mot(17)
        
	a1=soil1.soil(2)
	print(a1)
	firebase.put('iot','soil moisture',a1)
	#firebase.get('/iot','soil moisture')
	a2,a3=dhhht.dh(3)
	firebase.put('iot','temp',a2)
	firebase.put('iot','humidity',a3)
	a=ultrasonic_distance.distance(18,24)
	print(a)
	firebase.put('iot','distance',a)
	a4=soil1.soil(4)
	print(a4)
	firebase.put('iot','light',a4)
	
       
##        else:
##                pass
	time.sleep(1)
