import time
class vendor:
	def __init__(self,vN,vGST,vMobile,vCode='V001'):
		self.vName = vN
		self.vGST = vGST
		self.vMobile = vMobile
		self.vCode = vCode
		print('Registration is done!!!')
	def billing(self,pN,pQ=0,pCost=0.0):
		self.pName = pN
		self.pQty  = pQ
		self.pCost = pCost
		self.total = self.pQty * self.pCost
		self.tax   = self.total * 0.12
		self.GS	   = self.tax + self.total
		self.WriteOperation() # object based nestedCall
	def WriteOperation(self):
		wobj = open('E:\\products.csv','a')
		s1=f'{self.vName},{self.vCode},{self.vGST},{self.vMobile},'
		s2=f'{self.pName},{self.pCost},{self.pQty},{self.total},'
		s3=f'{self.tax},{self.GS} (including Tax),'
		s4=f'{time.ctime()}'
		wobj.write(s1+s2+s3+s4+'\n')
		wobj.close()

vobj1 = vendor('IBM','GST1234',99393939,'V-123')
vobj2 = vendor('KLabs','GST4323',433523,'V-452')

vobj2.billing('prodX',3,1500)
vobj1.billing('prodD',14,569.32)
time.sleep(5)
vobj2.billing('prodY',2,500)


