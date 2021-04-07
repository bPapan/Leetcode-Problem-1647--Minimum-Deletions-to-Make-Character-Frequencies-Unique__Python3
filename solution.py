class Solution:
    def minDeletions(self, s: str) -> int:
        
        cnt_dict = {}
        
        for c in s:
            if c in cnt_dict:
                cnt_dict[c]+=1
            else:
                cnt_dict[c]=1                                   #Store the frequency of each character in a dictionary
                
        cnt_dict = {k: v for k, v in sorted(cnt_dict.items(), reverse=True, key=lambda item: item[1])}  #Sort the dictionary in a non-increasing order of the frequencies
             
        freq_found = []                                         #Store which frequencies have been found till now
        res = 0                                                 #Store how many characters to remove to make frequencies unique
        for c in cnt_dict.keys():
            while cnt_dict[c]>0 and cnt_dict[c] in freq_found:  #Don't reduce the frequency if the frequency is already 0
                cnt_dict[c]-=1
                res+=1
            freq_found.append(cnt_dict[c])                      #Found a unique frequency, append to the list
            
            
        return res
