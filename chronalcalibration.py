#!env python3
import sys

def readme(filename):
    ans=[]
    with open(filename,"r") as fh:
        for x in fh:
            ans.append(int(x))
    return ans        

def firstFreqAtTwice(deviations):
    counter={}
    counter[0]=1
    cursum=0
    curidx=0
    while counter[cursum]<2:
        cursum+=deviations[curidx]
        if cursum in counter:
            counter[cursum]=counter[cursum]+1
        else:
            counter[cursum]=1
        curidx = (curidx+1)%len(deviations)    
    return cursum

def main():
    print("reading in "+sys.argv[1])
    kk = readme(sys.argv[1])    
    print("File has {} lines with a deviation of {}".format(len(kk),sum(kk)))
    print("First repeated frequency is {}".format(firstFreqAtTwice(kk)))

if __name__=="__main__":
    main()
    



