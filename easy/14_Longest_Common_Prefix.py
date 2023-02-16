class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # cur_prefix = strs[0]

        # for i in range(1, len(strs)):
        #     if not cur_prefix:
        #         return ""

        #     min_length = min(len(cur_prefix), len(strs[i]))

        #     slice_num = 0
        #     for j in range(min_length):
        #         if cur_prefix[j] != strs[i][j]:
        #             break
        #         slice_num += 1
            
        #     cur_prefix = cur_prefix[:slice_num]
        
        # return cur_prefix
        output = ""
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                if i >= len(strs[j+1]) or strs[j][i] != strs[j+1][i]:
                    return output
            
            output += strs[0][i]
        
        return output
                 

            