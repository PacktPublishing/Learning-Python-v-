#def func():
#	a =12
#	print '''Inside the function the value of a is acting as local variable''', a
#a= 10
#func()
#print '''Outside function the value of a is acting as global variable''',a

#def func():
#	a =12
#	print "a inside the function is the local variable",a
#func()
#print "Trying to access the local variable outside the function.",a

def func():
	global k
	k=k+7
	print "variable k is now global",k
k=10
func()
print "Accessing the value of k outside the function",k