class Solution:
    def minOperations(self, s: str) -> int:
        
        count,count_mod = 0, 1
        i = 0
        slist =list(s) 
        s_list_mod = list(s)
        s_list_mod[0] = '0' if s_list_mod[0]=='1' else '1'

        while i < (len(slist)-1):
            
            if slist[i]==slist[i+1]:
                count+=1
                if slist[i] =='0':
                    slist[i+1] = '1' 
                else:
                    slist[i+1] = '0'
            # i+=1
            
            if s_list_mod[i]==s_list_mod[i+1]:
                count_mod+=1
                if s_list_mod[i] =='0':
                    s_list_mod[i+1] = '1' 
                else:
                    s_list_mod[i+1] = '0'
            i+=1   
        
        return min(count,count_mod)
                   