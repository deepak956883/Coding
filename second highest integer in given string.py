class Solution:
    def secondHighest(self, s: str) -> int:
        li = []
        for i in s:
            if i.isdigit():
                if int(i) not in li:
                    li.append(int(i))
        if len(li)==0 or len(li)==1:
            return -1
        else:
            mf = max(li)
            li.remove(mf)
            ms = max(li)
            return ms 
