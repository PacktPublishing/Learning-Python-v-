class Leapx_org():
	def __init__(self,first,last,pay):
		self.f_name = first
		self.l_name = last
		self.pay_amt = pay 
		self.full_name = first+" "+last
	
	def make_email(self):
		return self.f_name+ "."+self.l_name+"@xyz.com"
		
	def incrementpay(self):
		self.pay_amt = int(self.pay_amt*1.20)
		return self.pay_amt
	
L_obj1 = Leapx_org('mohit', 'RAJ', 60000)
L_obj2 = Leapx_org('Ravender', 'Dahiya',70000) 

print L_obj1.pay_amt
print L_obj1.incrementpay()