import pytest
from io import StringIO
import sys
from h import main


@pytest.mark.parametrize('input_data, answer', [
    # Пример из условия
    ('12 3\ncabacaqwerty\nerty\ncaba\ncaqw', '2 3 1'),

    # Уже правильный порядок
    ('6 2\nabcdef\nabc\ndef', '1 2'),

    # Обратный порядок
    ('6 2\nabcdef\ndef\nabc', '2 1'),

    # Все куски одинаковые
    ('6 3\naaaaaa\naa\naa\naa', '1 2 3'),

    # Минимальный случай
    ('1 1\na\na', '1'),

    # Два одинаковых куска, но используются оба
    ('4 2\nabab\nab\nab', '1 2'),

    # Перепутанный порядок
    ('9 3\nxyzabc123\nabc\n123\nxyz', '3 1 2'),    

    # Случай, где ответ любой (дублирующиеся куски, но порядок не важен)
    ('4 2\naabb\naa\nbb', '1 2'),

    # Чередующиеся блоки (однозначное восстановление)
    ('8 4\nabababab\nab\nab\nab\nab', '1 2 3 4'),

    # Повторяющиеся, но вперемешку
    ('12 4\nxyzxyzxyzxyz\nxyz\nxyz\nxyz\nxyz', '1 2 3 4'),

    # Кирасирский тест (перемешка повторяющихся групп)
    ('16 4\nqwerqwerasdfasdf\nqwer\nasdf\nqwer\nasdf', '1 3 2 4'),
    
])
def test_h(input_data, answer):
    sys.stdin = StringIO(input_data)
    
    result = main()
    assert result == answer
