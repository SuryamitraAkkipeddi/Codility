class bintree:
    x = 0
    l = None
    r = None

    def __init__(self,x,l,r):
        self.x = x
        self.l = l
        self.r = r



tree = bintree(5,
               bintree(8,
                       bintree(12,
                               bintree(1,
                                       None,
                                       None),
                               None),
                       bintree(6,
                               None,
                               None),
                       ),
               bintree(9,
                       bintree(7,
                               bintree(2,
                                       None,
                                       None),
                               None),
                       bintree(4,
                               None,
                               bintree(3,
                                       None,
                                       None)

                       )
               )
            )


def maxdiff(maxN,minN, node):

    if node == None:
        return (maxN, minN)

    maxN1 = maxN if maxN != None and maxN >= node.x  else node.x # node.x is max if maxN is less than it
    minN1 = minN if minN != None and minN <= node.x  else node.x # node.x is min if minN is > than it

    maxN2 = maxN1
    minN2 = minN1
    # split paths here
    (maxN1,minN1) = maxdiff(maxN1,minN1,node.l)

    (maxN2,minN2) = maxdiff(maxN2,minN2,node.r)

    if abs(maxN1-minN1) > abs(maxN2 - minN2):
        return (maxN1,minN1)

    return (maxN2,minN2)


if __name__=="__main__":

    max,min = maxdiff(None,None,tree)
    print ( "max,min (%d,%d)" % (max,min))
    print ("Solution is %d" % abs(max-min))