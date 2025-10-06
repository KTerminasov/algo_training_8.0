import pytest
from io import StringIO
import sys
from c import main


@pytest.mark.parametrize('input_data, answer', [
    # Пример из условия
    ('5 3\n1 1 1 2 2', '15'),
    ('10 4\n8 8 8 8 8 8 8 8 8 2 1', '1'),

        
])
def test_h(input_data, answer):
    sys.stdin = StringIO(input_data)
    
    result = main()
    assert result == answer