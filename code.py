class Solution:
    def calPoints(self, operations: List[str]) -> int:
        n=len(operations)
        d=[]
        for i in range(n):
            if operations[i]=="+":
                d.append(int(d[-1])+int(d[-2]))
            elif operations[i]=="D":
                d.append(int(d[-1]*2))
            elif operations[i]=="C":
                d.pop()
            else:
                d.append (int(operations[i]))
        l=0
        for i in d:
            l+=i
        return l

            

        
