#def pass_ref(list1):
#	list1.extend([23,89])
#	print "list inside the function: ",list1
#list1 = [12,67,90]
#print "list before pass", list1
#pass_ref(list1)
#print "list outside the function", list1

def func(a):
	a=a+4
	print "Inside the function", a
a= 10
func(a)
print "Outside the function", a