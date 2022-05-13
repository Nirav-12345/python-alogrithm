def anagram(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()




    if(len(str1)==len(str2)):
        sorted_str1=sorted(str1)
        sorted_str2=sorted(str2)

        if (sorted_str1==sorted_str2):
            print(str1+"and"+str2+"are anagram")

        else:
            print("not anagram")



if __name__=="__main__":
    str1="earth"
str2="heart"

print(anagram(str1,str2))



