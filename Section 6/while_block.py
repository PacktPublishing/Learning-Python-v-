#while <condition>:
#	<statements>

checking_acc = 5678143
num = int(raw_input("Enter the account number\t"))
while checking_acc != num:
	print "Wrong number "
	num = int(raw_input("Enter the right account number\t"))
print "\n*********"
print "Your account number is" , num