import pytest
from io import StringIO
import sys
from c import main


@pytest.mark.parametrize('input_data, answer', [    
    # Single rectangle fitting exactly
    ('1 10 10\n5 5', '2.0000000000'),
    # Multiple rectangles, same height, fits with stacking
    ('3 10 10\n2 5\n3 5\n4 5', '2.0000000000'),
    # Multiple rectangles, different heights, fits with stacking
    ('4 10 10\n2 3\n3 4\n2 3\n3 4', '2.5000000000'),
    # Rectangle exceeds width, should scale down
    ('2 10 10\n6 5\n6 5', '1.6666666667'),
    # Rectangle exceeds height, should scale down
    ('2 10 10\n5 6\n5 6', '1.6666666667'),
    # Maximum possible k with min(w, h)
    ('1 5 5\n5 5', '1.0000000000'),
    # Zero width or height rectangle
    ('2 10 10\n0 5\n5 5', '2.0000000000'),
    # Large numbers
    ('2 100000 100000\n50000 50000\n50000 50000', '2.0000000000'),
    # Very small k
    ('2 10 10\n1 1\n1 1', '10.0000000000'),
])
def test_h(input_data, answer):
    sys.stdin = StringIO(input_data)
    
    result = main()
    assert result == answer

