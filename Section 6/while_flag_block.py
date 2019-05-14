sum = 0
flag = 1
while flag == 1:
	data = int(raw_input("Enter the number or press 0 to quit :"))
	if data == 0:
		flag =0
	sum = sum+data
print "Sum is ", sum