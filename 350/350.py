class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        tmp_dict = dict()
        ret = []
        for i in nums1:
            tmp_dict[i] = tmp_dict[i] + 1 if tmp_dict.get(i) else 1
        for n in nums2:
            if tmp_dict.get(n) > 0:
                ret.append(n)
                tmp_dict[n] -= 1
        return ret
