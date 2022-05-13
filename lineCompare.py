import math
def line_compare(x1,y1,x2,y2,a1,b1,a2,b2):
    length1=math.sqrt(x2**2-x1**2)-math.sqrt(y2**2-y1**2)
    length2=math.sqrt((a2**2-a1**2))-math.sqrt(b2**2-b1**2)
    if length2==length1:
        print("Both are equal")

    else:
        print("Both are not equal")








if __name__=="__main__":
    line_compare(4,6,7,8,3,4,5,7)