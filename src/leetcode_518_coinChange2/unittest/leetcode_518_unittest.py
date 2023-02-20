import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_518_top_down_memoisation import Solution as Solution1
from solutions.leetcode_518_bottom_up_tabulation import Solution as Solution2
from solutions.leetcode_518_bottom_up_optimized import Solution as Solution3

class Test(unittest.TestCase):
    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()
        self.solution3 = Solution3()
    
    def test_example_1(self):
        params = (
            [1,2,5],
            5
        )
        expected_output = 4

        actual_output = self.solution1.change(*params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.change(*params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.change(*params)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        params = (
            [2],
            3
        )
        expected_output = 0

        actual_output = self.solution1.change(*params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.change(*params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.change(*params)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        params = (
            [10],
            10
        )
        expected_output = 1

        actual_output = self.solution1.change(*params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.change(*params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.change(*params)
        self.assertEqual(actual_output, expected_output)

    def test_large_input_large_output(self):
        params = (
            [2930,691,4415,4872,2761,3841,3610,337,2598,3441,94,1780,926,4396,4810,1788,2159,4805,2984,4014,3826,2213,1083,2154,2187,341,2546,337,1653,4219,860,3451,654,4478,2594,376,1691,3956,4460,4294,762,1880,1007,2937,1766,1490,4407,3412,3458,1926,1426,4540,2714,1236,3745,4414,4999,845,1087,1220,846,2318,4297,3775,1012,4128,3803,2871,2896,2311,2003,129,3112,4552,1831,383,2792,1322,1268,3065,4753,1673,1476,1794,4991,76,1991,3979,2661,1343,2818,363,2574,2203,1329,450,2536,259,3269,4295,1022,1832,1655,2876,4909,2104,635,1408,4727,2333,3644,2657,4729,4614,2308,1466,326,599,27,1061,2975,86,3834,4690,4499,3982,1440,4654,1514,3735,413,2392,1323,759,47,1462,465,2030,4207,374,1295,4171,2237,1801,4541,4645,1643,1117,4842,2841,2775,6,4911,91,4029,24,3215,978,1007,1452,2484,1739,4875,2653,4676,1138,2621,2691,1416,4972,2183,3558,4620,4077,138,4823,590,1789,277,1112,331,2558,166,3129,145,4174,3813,2459,4070,4664,4908,2865,1068,1307,2344,2355,2363,3509,2902,1213,1538,4205,1148,2481,2583,3466,911,1028,1511,4237,920,1154,3354,1934,41,725,1504,3298,4292,4685,1183,4655,4371,3707,835,4497,246,3703,2468,647,4270,3595,2214,1925,194,1727,3035,3728,320,220,1997,2019,4475,3250,4492,3464,3930,3078,1183,2223,2783,1801,3040,2883,2901,4378,3337,2950,3074,1046,294,4440,1883,1875,3036,3928,3843,1493,3480,2424,2134,1535,4275,3210,952,2262,4222,2404,908,1690,1576,4859,395,1829,1675,4949,3525,2750,3577,1008,2294,267,2815,3638,1403,4446,4231,80,4355,422],
            1431
        )
        expected_output = 408220554

        actual_output = self.solution1.change(*params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.change(*params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.change(*params)
        self.assertEqual(actual_output, expected_output)

    def test_large_input_small_output(self):
        params = (
            [2930,691,4415,4872,2761,3841,3610,337,2598,3441,94,1780,926,4396,4810,1788,2159,4805,2984,4014,3826,2213,1083,2154,2187,341,2546,337,1653,4219,860,3451,654,4478,2594,376,1691,3956,4460,4294,762,1880,1007,2937,1766,1490,4407,3412,3458,1926,1426,4540,2714,1236,3745,4414,4999,845,1087,1220,846,2318,4297,3775,1012,4128,3803,2871,2896,2311,2003,129,3112,4552,1831,383,2792,1322,1268,3065,4753,1673,1476,1794,4991,76,1991,3979,2661,1343,2818,363,2574,2203,1329,450,2536,259,3269,4295],
            1022
        )
        expected_output = 8

        actual_output = self.solution1.change(*params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.change(*params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.change(*params)
        self.assertEqual(actual_output, expected_output)
        
#######################################
if __name__ == '__main__':
    unittest.main()