import pytest
from io import StringIO
import sys
from e import main


@pytest.mark.parametrize('input_data, answer', [  
    # Test 1: Minimal case, single tower K=1
    ("1 1\n1", "1\n1"),
    
    # Test 2: N < K, no towers possible
    ("1 2\n1", "0"),
    
    # Test 3: K=1, two separate towers
    ("2 1\n1 2", "2\n1 2"),
    
    # Test 4: Choice of tower position, equal strength, code prefers earlier due to reconstruction
    ("3 2\n1 10 1", "1\n1"),
    
    # Test 5: From problem example, skipping low values
    ("8 3\n1 2 3 4 1 6 7 8", "2\n2 6"),
    
    # Test 6: Skipping a low pillar in the middle for better total
    ("7 3\n100 100 100 1 100 100 100", "2\n1 5"),
    
    # Test 7: Alternating low-high, take non-overlapping towers
    ("4 2\n1 100 1 100", "2\n1 3"),
    
    # Test 8: K=1, all positive, take all
    ("5 1\n5 4 3 2 1", "5\n1 2 3 4 5"),
    
    # Test 9: All zeros, no benefit to take any
    ("3 1\n0 0 0", "0"),
    
    # Test 10: Better to take later tower with higher min
    ("4 3\n10 20 30 40", "1\n2"),
    
    # Test 11: Multiple towers, increasing values, optimal non-greedy
    ("6 2\n1 2 3 4 5 6", "3\n1 3 5"),
    
    # Test 12: Low mins in between, take only one tower
    ("5 3\n10 1 10 1 10", "1\n1"),
    
    # Test 13: Full length tower
    ("3 3\n5 5 5", "1\n1"),
    
    # Test 14: Handle negatives and zeros with K=1 (skip negative/zero if strength <=0)
    ("4 1\n-1 0 1 2", "3\n1 3 4"),
])
def test_h(input_data, answer):
    sys.stdin = StringIO(input_data)
    
    result = main()
    assert result == answer

