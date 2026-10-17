class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # total = len(nums1) + len(nums2)  |   half = total // 2
        # from half, we need to get check how many ele we need from nums1 and nums2
        # to do this we will do BS on one of the arr
        # based on len, take other ele from other arr
        # check if BS is done correctly and take eles to cal median acc odd & even case
        # edge case: it is possible that we may need to take all ele from one of the arr
        
        # n1 = [1, 2, 3, 4, 5, 6, 7, 8] | n2 = [1, 2, 3, 4]  res = (3 + 4) / 2
        total = len(nums1) + len(nums2)
        half = total // 2
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2    # idx for A
            j = half - i - 2    # idx for B     IMP: -2

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if (i + 1) < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if (j + 1) < len(B) else float('inf')

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:        # A is too big
                r = i - 1
            else:                       # A is too small
                l = i + 1
                          

