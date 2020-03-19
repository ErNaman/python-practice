def decorator(func): 
	def inner1(): 
		print("before function call") 
		func() 
		print("After function call") 
	return inner1 
def fun(): 
	print("inside the function !!") 
fun = decorator(fun) 
fun()
