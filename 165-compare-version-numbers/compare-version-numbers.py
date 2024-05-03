class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1,v2 = version1.split('.'),version2.split('.')
        n = max(len(v1),len(v2))
        v1+=[0]*(n-len(v1))
        v2+=[0]*(n-len(v2))
        i=0

        while i<n:
            if int(v1[i])>int(v2[i]):
                return 1
            elif int(v1[i])<int(v2[i]):
                return -1
            else:
                i+=1

        return 0