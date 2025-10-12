import pytest
from io import StringIO
import sys
from i import main


@pytest.mark.parametrize('input_data, answer', [  
    ('3 3\n1 2 3\n6 5 4\n7 8 9', 9),
    ('3 2\n3 2\n2 2\n3 2', 2),
    ('1 1\n42', 1),
    ('1 3\n1 2 3', 3),
    ('1 3\n1 3 5', 1),
    ('2 2\n1 4\n2 3', 4),
    ('2 1\n1\n2', 2),
    ('2 1\n1\n3', 1),
    ('2 2\n1 1\n2 2', 2),
    ('2 2\n5 5\n5 5', 1),
    ('3 3\n1 2 3\n4 5 6\n7 8 9', 3),
    ('3 3\n9 8 7\n6 5 4\n3 2 1', 3),
    ('4 4\n1 2 4 5\n3 6 7 8\n9 10 11 12\n13 14 15 16', 4),
    ('3 3\n1 8 2\n7 9 3\n6 5 4', 6),
    ('4 1\n4\n3\n2\n1', 4),
    ('2 2\n1 4\n7 10', 1),
    ('3 3\n2 3 4\n1 5 6\n2 3 4', 4)
])
def test_h(input_data, answer):
    sys.stdin = StringIO(input_data)
    
    result = main()
    assert result == answer

