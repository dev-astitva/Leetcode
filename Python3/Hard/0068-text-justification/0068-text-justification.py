class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def full_justified(words):
            m,n=len(''.join(words)),len(words)
            if n==1:
                return words[0]+" "*(maxWidth-len(words[0]))
            else:
                r=""

                rem_space=maxWidth-m
                extra=rem_space%(n-1)

                equals=rem_space//(n-1)
                space=[equals]*(n-1)

                if extra!=0:
                    ptr=0
                    while extra:
                        space[ptr]+=1
                        ptr+=1
                        extra-=1

                for i in range(n):
                    r+=words[i]
                    if i<(n-1):
                        r+=" "*space[i]
                
                return r

        def left_justified(line):
            words=[]
            prev=""
            count=0
            for c in line:
                if c==" ":
                    if prev:
                        words+=[prev]
                        prev=""
                    continue
                else:
                    prev+=c
                    count+=1
            if prev:
                words+=[prev]
                
            return " ".join(words)+" "*(maxWidth-count-(len(words)-1))

                    
                

        ptr=0
        m=len(words)
        res=[]
        while True:
            if ptr>=m:
                break
            temp=[]
            count=0
            for i in range(ptr,m):
                el=words[i]
                m_=len(el)
                if count+m_>maxWidth:
                    break
                count+=m_+1
                temp+=[el]
                ptr+=1
            res+=[full_justified(temp)]


        res[-1]=left_justified(res[-1])

        return res