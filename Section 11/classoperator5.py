class Leapx_org():
	def __init__(self,first,last,pay):
		self.f_name = first
		self.l_name = last
		self.pay_amt = pay 
		self.full_name = first+" "+last
	def make_email(self):
		return self.f_name+ "."+self.l_name+"@xyz.com"
	def __str__(self):
		str1 = "instance belongs to "+self.full_name
		return str1
	def __len__(self):
		return len(self.f_name+self.l_name)
	
L_obj1 = Leapx_org('mohit', 'RAJ',60000)
print L_obj1
print "\n"
print "Lenght is ",len(L_obj1)