class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    #两数之和
        dict_record = defaultdict(list)
        for index, num in enumerate(nums):
            dict_record[num].append(index)
        for key in dict_record.keys():
            diff = target - key
            if diff == key:
                if len(dict_record[key])>1:
                    return dict_record[key]
                else: pass
            elif diff in dict_record.keys():
                return [dict_record[key][0],dict_record[diff][0]]
            else:
                continue
                
    # 最长回文子串
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_in_window = defaultdict(int)
        window_length = 0
        current_max_length = 0
        right_index = 0
        left_index = 0
        while(right_index < len(s)):
            letter = s[right_index]
            if letter not in letter_in_window:
                letter_in_window[letter] = right_index
            else:
                current_max_length = max(right_index - left_index,current_max_length)
                for k in range(left_index,right_index):
                    if s[k] != letter:
                        print(s[k],letter)
                        letter_in_window.pop(s[k])
                    else:
                        letter_in_window[letter] = right_index
                        left_index = k + 1
                        break
            right_index += 1
        current_max_length = max(right_index - left_index,current_max_length)
        
        return current_max_length
