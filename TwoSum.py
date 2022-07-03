class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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
