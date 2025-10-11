import pytest
from io import StringIO
import sys
from f import main


@pytest.mark.parametrize('input_data, answer', [
    ('5\nW.W\nC.C\n.W.\nCC.\nC.W', 3),
    ('4\n.W.\nCWC\n.W.\nC.W', 2),
    ('1\n...', 0),
    ('1\nCCC', 1),
    ('1\nWWW', 0),
    ('1\nWCW', 1),
    ('1\n.C.', 1),
    ('1\nW.W', 0),
    ('2\n...\nWWW', 0),
    ('2\nWWW\n...', 0),
    ('2\nCCC\nCCC', 2),
    ('2\n.W.\nW.W', 0),
    ('3\n..C\n.W.\nC.C', 2),
    ('3\nC..\n.W.\n..C', 1),
    ('2\nWW.\n.WW', 0),  # No way to reach bottom
    ('3\n...\nWWW\n...', 0),  # Blocking row in middle
    ('4\nC.C\n.C.\nC.C\n.C.', 4),  # Zigzagging to collect all possible
    ('1\n..W', 0),  # Only possible landings give 0 or invalid
    ('1\nC.W', 1),  # Max 1
    ('5\n...\n...\n...\n...\n...', 0),  # No coins
    ('5\nCCC\nCCC\nCCC\nCCC\nCCC', 5),  # Max in one column

    # 3 тест
    ('4\nWWW\nCWC\nW.W\nCWW', 0),
    # 8 тест
    ('6\nWW.\nCWW\nWW.\nCW.\nCWC\nWWC', 0),
    # 12 тест
    ('17\nWW.\n..C\n.C.\n.CC\n.WC\nWW.\n.WW\nCW.\n.CW\nCWC\n.WC\nCW.\nCWC\nCWC\n.W.\nCCW\nCWW\n', 4),
    # 24 тест
    ('30\n.C.\n.W.\nWW.\nWWC\n.WC\nWW.\n...\n.WC\n.WC\nCW.\nCWW\nCWC\n.WC\nCW.\n.WC\n'
     '.WC\n.WC\nWWC\n.WC\n.WC\nC.C\nCWC\n.WC\nCWC\nWW.\nC..\nCWC\nCWC\nCCW\nCWC\n', 7),
])
def test_h(input_data, answer):
    sys.stdin = StringIO(input_data)
    
    result = main()
    assert result == answer

