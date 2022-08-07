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
                
    # 最长无重复字串
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
    
    # 求和两个 listnode， 并写成新的 listnode
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def readNode(listnode):
            num = 0
            index = 0
            while listnode:
                num +=  listnode.val * (10 ** index) 
                index += 1
                listnode = listnode.next
            return num
        def writeNode(num):
            nums = str(num)
            this_listnode = None
            previous_listnode = None
            for n in nums:
                this_listnode = ListNode(val=int(n),next=previous_listnode)
                previous_listnode = this_listnode
            return this_listnode
        num_1 = readNode(l1)
        num_2 = readNode(l2)
        num_sum = num_1 + num_2
        return writeNode(num_sum)
    
    # 两个有序数组合并求中位数， 这是 m+n 复杂度的版本
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # method 1
        current_pops = 0
        flag = True if (len(nums1) + len(nums2)) % 2 == 0 else False
        target_pops = int((len(nums1) + len(nums2)) / 2)
        while nums1 and nums2 and current_pops < target_pops:
            if nums1[0] <= nums2[0]:
                num_to_pop = nums1[0]
                nums1.pop(0)
            else:
                num_to_pop = nums2[0]
                nums2.pop(0)
            current_pops += 1
        rest_to_pop = target_pops - current_pops
        if not flag:
            if nums1 and nums2:
                return min(nums1[0],nums2[0])
            elif nums1:
                return nums1[rest_to_pop]
            else:
                return nums2[rest_to_pop]
        else:
            if nums1 and nums2:
                return (num_to_pop + min(nums1[0],nums2[0])) / 2
            elif nums1:
                if rest_to_pop > 0:
                    return (nums1[rest_to_pop - 1] + nums1[rest_to_pop]) / 2
                else:
                    return (nums1[rest_to_pop] + num_to_pop) / 2
            else:
                if rest_to_pop > 0:
                    return (nums2[rest_to_pop - 1] + nums2[rest_to_pop]) / 2
                else:
                    return (nums2[rest_to_pop] + num_to_pop) / 2
     # 最长回文子串
     def longestPalindrome(self, s: str) -> str:
        max_length = 0
        flag = False
        if len(s) < 2:
            return s
        for i in range(len(s) - 1):
            j = i 
            while j < len(s) - 1:
                if s[j + 1] == s[i]:
                    j += 1
                else:
                    break
            for k in range(1, min(i, len(s) - 1 - j) + 1):
                flag = True
                index_left = i - k
                index_right = j + k
                if s[index_left] == s[index_right]:
                    continue
                else:
                    index_left += 1
                    index_right -= 1
                    break
            if flag:
                this_length = index_right - index_left + 1
                if this_length > max_length:
                    max_length = this_length
                    max_left = index_left
                    max_right = index_right
            else:
                this_length = j - i + 1
                if this_length > max_length:
                    max_length = this_length
                    max_right = j
                    max_left = i
        return s[max_left:max_right + 1]
