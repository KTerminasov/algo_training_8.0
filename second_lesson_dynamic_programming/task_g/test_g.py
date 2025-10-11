import pytest
from io import StringIO
import sys
from g import main


@pytest.mark.parametrize('input_data, answer', [
    
])
def test_h(input_data, answer):
    sys.stdin = StringIO(input_data)

    result = main()
    assert result == answer
