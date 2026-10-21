class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        n=len(s)
        result=[]
        if n<4 or n>12:
            return result
        for i in range(1,4):
            for j in range(i+1,i+4):
                for k in range(j+1,j+4):
                    if k >=n :
                        continue
                    a=s[:i]
                    b=s[i:j]
                    c=s[j:k]
                    d=s[k:]
                    if not (1<=len(d)<=3):
                        continue
                    parts=[a,b,c,d]
                    valid=True
                    for part in parts:
                        if (len(part)>1 and part[0]=="0"):
                            valid=False
                            break
                        if int(part) > 255:
                            valid=False
                            break
                    if valid:
                        result.append(".".join(parts))
        return result