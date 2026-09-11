class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n=len(digits)

        def zeroPad(x):
            return "0"*(n-len(x))+x

        def rotateDigs(y):
            lst=[
                (y[0],y[1],y[2]),(y[2],y[0],y[1]),
                (y[0],y[2],y[1]),(y[2],y[1],y[0]),
                (y[1],y[0],y[2]),(y[1],y[2],y[0])
            ]
            return list(set(lst))

        def bitCalc(n):
            count=0

            unique_nums=set()


            for i in range(7,2**n):

                highs=abs(i).bit_count()
                if highs!=3:
                    continue

                b=zeroPad(bin(i)[2:])

                temp_num=[]
                for k in range(n):
                    if b[k]=="1":
                        temp_num+=[digits[k]]
                
                digs=rotateDigs(temp_num)
                for dig in digs:
                    unique_nums.add(dig)
            
            for r in unique_nums:
                if int(r[0])!=0 and int(r[-1])%2==0:
                    count+=1
            
            return count

        return bitCalc(n)