import pytest
from io import StringIO
import sys
from c import main


@pytest.mark.parametrize('input_data, answer', [
    # Пример из условия
    ('abacaba\n', '15'),
    ('aaaaaa\n', '1'),

    # Минимальная длина
    ('a\n', '1'),

    # Два разных символа
    ('ab\n', '2'),

    # Два одинаковых символа
    ('aa\n', '1'),

    # Все символы разные
    ('abcd\n', '7'),

    # Частично повторяющиеся буквы
    ('aabb\n', '5'),

    # Смешанные повторения
    ('abcabc\n', '13'),

    # Все символы одинаковые, длина большая
    ('aaaaaaaaaa\n', '1'),

    # Все буквы разные, n=10
    ('abcdefghij\n', '46'),

    # Большой тест: все одинаковые
    ('a' * 100000 + '\n', '1'),    
])
def test_h(input_data, answer):
    sys.stdin = StringIO(input_data)
    
    result = main()
    assert result == answer