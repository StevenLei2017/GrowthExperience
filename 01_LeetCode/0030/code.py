class Solution(object):
    def findSubstring(self, s, word_list):
        if not s or not word_list:
            return []
        from collections import Counter
        word_counter = Counter(word_list)
        len_word = len(word_list[0])
        len_str = len(s)
        len_subStr = len_word * len(word_list)
        if len_str < len_subStr:
            return []
        result_list = []
        for i in range(min(len_word, len_str-len_subStr+1)):
            local_dict = {}
            windowStart_index = i
            wordStart_index = i
            while wordStart_index + len_word <= len_str:
                wordEnd_index = wordStart_index + len_word
                word = s[wordStart_index: wordEnd_index]
                wordStart_index = wordEnd_index
                if word not in word_counter:
                    windowStart_index = wordEnd_index
                    local_dict.clear()
                else:
                    if word in local_dict:
                        local_dict[word] += 1
                    else:
                        local_dict[word] = 1
                    while local_dict[word] > word_counter[word]:
                        window_firstWord = s[windowStart_index: windowStart_index+len_word]
                        local_dict[window_firstWord] -= 1
                        windowStart_index += len_word
                    if wordStart_index - windowStart_index == len_subStr:
                        result_list.append(windowStart_index)
        return result_list    
            

if __name__ == '__main__':
    solution = Solution()
    s = "wordgoodgoodgoodbestword"
    word_list = ["word","good","best","word"]
    result_list = solution.findSubstring(s, word_list)
    print(result_list)
    s = "barfoothefoobarman"
    word_list = ["foo","bar"]
    result_list = solution.findSubstring(s, word_list)
    print(result_list)
    