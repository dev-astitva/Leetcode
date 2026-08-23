class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num)
        p1,p2=num[:n//2],num[n//2:] #parts
        t1,q1=0,0 #total and remaining ones
        t2,q2=0,0
        for i in p1:
            if i=="?":
                q1+=1
            else:
                t1+=int(i)
        for j in p2:
            if j=="?":
                q2+=1
            else:
                t2+=int(j)

        #contains digits only
        if q1==q2==0:
            return t1!=t2
        #odd number of ?
        if (q1+q2)%2:
            return True
        #even number of ?
        if q1==q2:
            return t1!=t2
        
        return 2*(t1-t2)!=9*(q2-q1)
        