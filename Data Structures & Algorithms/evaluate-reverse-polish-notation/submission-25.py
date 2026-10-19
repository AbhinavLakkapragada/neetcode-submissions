class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """while len(tokens)>1:
            for i in tokens:
                if i in ("+","-","*","/"):
                    a = tokens[i-2]
                    b = tokens[i-1]
                    if"""
        a=[]
        for x in tokens:
            if x=="+":
                a.append(a.pop()+a.pop())
            elif x=="-":
                n=a.pop()
                m=a.pop()
                a.append(m-n)

            elif x=="*":
                a.append(a.pop()*a.pop())
            elif x=="/":
                n=a.pop()
                m=a.pop()
                a.append(int(m/n))
            else:
                a.append(int(x))
        return a.pop()




            