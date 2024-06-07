class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        s=[]
        dictionary.sort()
        sentence=sentence.split()
        for i in sentence:
            flag=0
            for x in dictionary:
                if i.startswith(x):
                    s.append(x)
                    flag=1
                    break
            if flag==0: s.append(i)
        return " ".join(s)