#Vilina Prenko

import unittest 
import liststuff

nums = [1, 2, 3, 4, 5]

class ListStaffTest(unittest.TestCase):
    def testmax(self) -> None:
        #test 1
        self.assertEqual(liststuff.maximum([1, 2, 3, 6, 5]), 6)
        #test 2
        self.assertEqual(liststuff.maximum([]), None)
        #test 3 
        self.assertEqual(liststuff.maximum([100, 55, 99, -50, 0]), 100)
        #test 4
        self.assertEqual(liststuff.maximum([9999999, 65, 879, 648, -898956, 0]), 9999999)
        #test 5
        self.assertEqual(liststuff.maximum([8, 8, 8]), 8)

    def testequal(self) -> None:
        #test 1
        self.assertEqual(liststuff.equivalent(nums, [2,3,4,5,1]), True)
        #test 2
        self.assertEqual(liststuff.equivalent(nums, []), False)
        #test 3 
        self.assertEqual(liststuff.equivalent([100, 55, 99, -50, 0], nums), False)
        #test 4
        self.assertEqual(liststuff.equivalent([1, 1, 1, 1], nums), False)
        #test 5
        self.assertEqual(liststuff.equivalent([1, 2, 3, 4], nums), False)        

    def testassending(self) -> None:
        #test 1
        self.assertEqual(liststuff.is_ascending(nums), True)
        #test 2
        self.assertEqual(liststuff.is_ascending([5,2,1,4,3]), False)
        #test 3 
        self.assertEqual(liststuff.is_ascending([-5, 5, 6, 7]), True)
        #test 4
        self.assertEqual(liststuff.is_ascending([1, 1, 1, 1]), False)
        #test 5
        self.assertEqual(liststuff.is_ascending([1, 2, 2, 3, 4]), False)

    def testrotate(self) -> None:
        #test 1
        liststuff.rotate(nums, 0)
        self.assertEqual([1, 2, 3, 4, 5], nums)
        #test 2
        nums1 = [5,2,1,4,3]
        liststuff.rotate(nums1, 1)
        self.assertEqual([3, 5, 2, 1, 4], nums1)
        #test 3 
        nums2 = [-5, 5, 6, 7]
        liststuff.rotate(nums2, -1)
        self.assertEqual([5, 6, 7, -5], nums2)
        #test 4
        nums3 = [1, 1, 1, 1, 0]
        liststuff.rotate([1, 1, 1, 1, 0], 5)
        self.assertEqual([1, 1, 1, 1, 0], nums3)
        #test 5
        nums4 = [1, 2, 2, 3, 4]
        liststuff.rotate([1, 2, 2, 3, 4], -5)
        self.assertEqual([1, 2, 2, 3, 4], nums4)

unittest.main()