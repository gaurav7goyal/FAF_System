import Adafruit_DHT as d 
def dh(a):
	h,t=d.read_retry(d.DHT11,a) 
	r1=str(t) 
	r2=str(h) 
	print(r1)
	print(r2)
	return r1,r2
	#return r2
#dh(4)
