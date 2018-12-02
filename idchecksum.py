#!env python3

import sys

def countsID(idin):
    ans=[0]*len(idin)
    chash = {}
    for x in idin:
        if x not in chash:
            chash[x]=1
        else:
            chash[x]+=1
    for c,co in chash.items():
        ans[co]+=1
    return ans

def idchecksum(filename):
    count2=0
    count3=0
    with open(filename,"r") as fn:
        for line in fn:
            cc = countsID(line)
            if cc[2]>=1:
                count2+=1
            if cc[3]>=1:
                count3+=1
    return (count2,count3)

def findpair(filename):
    with open(filename,"r") as fn:
        ids = [qwerty.strip() for qwerty in fn.readlines()]
        for ii in range(len(ids)):
            for jj in range(ii+1,len(ids)):
                pans = matchme(ids[ii],ids[jj])
                if pans is not None:
                    return pans
    return None

def matchme(x,y):
    diffcount = 0
    diffs = None
    for i,xx in enumerate(x):
        if xx!=y[i]:
            diffcount+=1
            diffs = xx+y[i]
        if diffcount==2:
            return None
    if diffcount==1:
        print("***Found it: {} and {} differ with {}***".format(x,y,diffs))
        return diffs
    return None

def main():
    a = idchecksum(sys.argv[1])
    print("Checksum of id file: ({},{}) with product {}".format(a[0],a[1],a[0]*a[1]))
    print("Closepair differ at {}".format(findpair(sys.argv[1])))

if __name__=="__main__":
    main()
