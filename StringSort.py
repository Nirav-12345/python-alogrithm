def my_func():
    g=['nirav', 'anshu', 'prof', 'do', 'dont', 'as']

    for i in range(1,len(g)):
        u=g[i]

        # move elements of list [0..i-1], that are
        # greater than val, to one position ahead
        # of the current position
        j=i-1
        while j>0 and u<g[j]:
            g[j+1]=g[j]
            j=j-1
            g[j+1]=u
            print(g)


if __name__=="__main__":
    my_func()









