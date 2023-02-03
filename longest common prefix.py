'''
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        
        temp = []
        for i in range(len(strs)):
            size = len(strs[i])
            temp.append(size)
        minsize = min(temp)
        
        flag = True
        for i in range(minsize):
            j = 1 
            if flag == True:   
                while j<len(strs):
                    if strs[0][i] == strs[j][i]:
                        if j==len(strs)-1:
                            ans = ans + strs[0][i]
                    else:
                        flag = False
                        break
                    j = j+1
        
        if len(strs)==1:
            return strs[0]
        elif len(strs)==0:
            return ''
        else:
            return ans
            

     

                

                
                



            