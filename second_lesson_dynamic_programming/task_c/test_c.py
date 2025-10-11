import pytest
from io import StringIO
import sys
from c import main


@pytest.mark.parametrize('input_data, answer', [  

    # Test 1: From the example
    ("3\n0 1 1\n0.5 1.5 1.5\n1 2 1\n", 2.0),
    
    # Test 2: N=0
    ("0\n", 0.0),
    
    # Test 3: N=1
    ("1\n0 1 10\n", 10.0),
    
    # Test 4: All overlapping, choose max weight
    ("3\n1 3 5\n1.5 2.5 10\n2 4 3\n", 10.0),
    
    # Test 5: No overlapping, sum all
    ("3\n1 2 1\n3 4 2\n5 6 3\n", 6.0),
    
    # Test 6: Identical ends, choose max single
    ("3\n0 2 1\n1 2 2\n1.5 2 3\n", 3.0),
    
    # Test 7: Identical intervals
    ("2\n1 2 1\n1 2 2\n", 2.0),
    
    # Test 8: Small weights, overlapping
    ("2\n1 3 0.1\n2 4 0.2\n", 0.2),
    
    # Test 9: Chain with small in middle beneficial
    ("4\n1 2 10\n2.1 3 1\n3.1 4 10\n1.5 5 15\n", 21.0),
    
    # Test 10: Multiple with same end, binary search picks rightmost
    ("4\n0 1 1\n0.5 1 2\n0.7 1 3\n1.1 2 4\n", 7.0),
    
    # Test 11: Touching intervals (non-overlapping if e_j == b_i allowed)
    ("2\n1 2 1\n2 3 2\n", 3.0),
    
    # Test 12: Overlapping with same start, different ends
    ("2\n1 3 5\n1 2 10\n", 10.0),
    
    # Test 13: One long low-weight overlapping many high-weight shorts
    ("5\n1 10 1\n2 3 100\n4 5 100\n6 7 100\n8 9 100\n", 400.0),
    
    # Test 14: Barely non-overlapping with floats
    ("3\n1 2 1\n2.0001 3 1\n3.0001 4 1\n", 3.0),
    
    # Test 15: Fractional values
    ("2\n0.5 1.5 1.5\n1.0 2.0 1.0\n", 1.5),
    
    # Test 16: Zero weights (edge, though problem says >0)
    ("2\n1 2 0\n3 4 0\n", 0.0),
    
    # Test 17: Negative weight (code should skip)
    ("2\n1 2 -1\n3 4 2\n", 2.0),
    
    # Test 18: Multiple same ends, different weights
    ("3\n1 5 10\n2 5 20\n3 5 15\n", 20.0),
    
    # Test 19: Long chain non-overlapping
    ("5\n1 2 5\n3 4 4\n5 6 3\n7 8 2\n9 10 1\n", 15.0),
    
    # Test 20: Skipping better than taking
    ("3\n1 10 10\n2 3 100\n4 5 100\n", 200.0),  # 100+100=200 >10
])
def test_h(input_data, answer):
    sys.stdin = StringIO(input_data)
    
    result = main()
    assert result == answer

