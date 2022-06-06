import time
def timeit(func):
	def timed(*args,**kw):
		print("Before the timeit decorator")
		ts=time.time()
		result=func(*args,**kw)
		te=time.time()
		minutes,seconds=divmod((te-ts),60)
		print(minutes,seconds)
		print("After the timeit decorator")
		print("time taken %8.2F"% ((te-ts)*10**6))
		return result
	return timed
@timeit
def fib():
	a,b=0,1
	while True:
		yield a
		a,b=b,a+b
while True:
	num=int(input("Enter the range of the fibonacci series"))
	if num<0 :
		print("Enter any positive integer")
		print("Try Again")
	else:
		fibo=fib()
		for x in range(num):
			print(next(fibo))
		break
