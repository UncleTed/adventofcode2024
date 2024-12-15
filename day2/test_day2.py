import unittest
import numpy as np

class TestDay2(unittest.TestCase):
    def _remove_one_element(self, report, position):
        report = report.tolist()
        if position == 0:
            return report[1:]
        if position == len(report):
            return report[0:position-1]
        return report[0:position] + report[position+1:]

    
    def test_remove_from_front(self):
        a = np.array([1,2,3,4,5])
        b = self._remove_one_element(a, 0)
        np.testing.assert_array_equal(b, np.array([2,3,4,5]))

    def test_remove_from_middle(self):
        a = np.array([1,2,3,4,5])
        b = self._remove_one_element(a, 1)
        np.testing.assert_array_equal(b, np.array([1,3,4,5]))

    def test_remove_from_end(self):
        a = np.array([1,2,3,4,5])
        b = self._remove_one_element(a, 5)
        np.testing.assert_array_equal(b, np.array([1,2, 3,4]))
