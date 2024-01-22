class ComplexNumber:
    def __init__(self,r=0,i=1):
        self.real=r;
        self.image=i;
def getData(self):
    print('{0}+{1}'.format(self.real,self.image))

c1=ComplexNumber(5,6)
c1.getData()