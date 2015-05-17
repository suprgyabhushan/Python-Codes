class Rational:
    def __init__(self,num,den):
        self.num=float(num)
        self.den=float(den)
    def add(self,n):
        return (self.num/self.den)+n
    def sub(self,n):
        return (self.num/self.den)-n
    def mul(self,n):
        return (self.num/self.den)*n
    def divide(self,n):
        return (self.num/self.den)/n
    def neg(self):
        return -self.num/self.den
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
if __name__=="__main__":
    p1=Rational(1,2)
    p2=1
    p3=p1.add(p2)
    p4=p1.neg()
    print p3
    print p4



