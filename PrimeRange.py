def prime(lower,upper):

    flag=0
    for num in range(lower,upper+1):
        flag=0
        if num >1:


            for i in range(2,num):
                if (num%i)==0:
                    flag=1
        if flag==0:
            print("Odd",num)

        if num%11==0:
            print("Palindromes",num)



if __name__=="__main__":
    prime(0,1000)


























