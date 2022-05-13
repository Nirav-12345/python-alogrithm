import cmath
def  line(x1,y1,x2,y2):
        l = cmath.sqrt(x2**2 - x1**2) + cmath.sqrt(y2**2 -y1**2)
        return l





if __name__=="__main__":
    x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
print(line(x1,y1,x2,y2))





