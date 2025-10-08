import pytest
from io import StringIO
import sys
from d import main


@pytest.mark.parametrize('input_data, answer', [
    # Тест из условия
    ('whatcanido\n6\na\nan\ncan\ndo\ni\nwhat', 'what can i do '),

    # Пустая строка
    ('\n0', ''),

    # Строка из одного элемента
    ('ko\n1\nko', 'ko '),

    # Строка из одного элемента и одного слова
    ('ko\n1\nko', 'ko '),

    # Строка из одного элемента и двух слов
    ('ko\n2\nk\no', 'k o '),

    # Строка из повторяющихся символов, разбиение на одиночные буквы
    ('aaa\n1\na', 'a a a '),

    # Строка с несколькими возможными разбиениями (выберет одно)
    ('pineapple\n4\npine\napple\npin\neapple', 'pine apple '),  # Или 'pine apple ', но любое

    # Строка с пересекающимися словами
    ('abc\n3\na\nab\nbc', 'a bc '),  # Или 'ab c ', но любое

    # Строка длиной 1, словарь с тем же словом
    ('x\n1\nx', 'x '),

    # Строка с максимальной длиной 100, разбиение на одиночные буквы (N=1, но много повторений)
    ('a' * 100 + '\n1\na', ' '.join(['a'] * 100) + ' '),

    # Максимальный N=2000: симулируем большой словарь, но для теста возьмем небольшой, но концептуально - строка 'ab', словарь с 'a','b' и filler словами
    # Для pytest не нужно 2000, но тест на большую строку с разбиением
    ('ab' * 50 + '\n2\na\nb', ' '.join(['a b'] * 50) + ' '),  # Длина 100

    # Словарь с длинными словами (до 20 букв)
    ('longwordexamplehere\n2\nlongword\nexamplehere', 'longword examplehere '),

    # Строка с минимальными словами, но множеством коротких
    ('abcde\n5\na\nb\nc\nd\ne', 'a b c d e '),

    # Строка, где слово равно всей строке
    ('completeword\n1\ncompleteword', 'completeword '),

    # Строка с дубликатами в словаре (но set сделает уникальными)
    ('dup\n2\ndup\ndup', 'dup '),

    # Строка длиной 100, разбиение на слова по 20 символов (5 слов)
    ('a'*20 + 'b'*20 + 'c'*20 + 'd'*20 + 'e'*20 + '\n5\n' + 'a'*20 + '\n' + 'b'*20 + '\n' + 'c'*20 + '\n' + 'd'*20 + '\n' + 'e'*20, 'a'*20 + ' ' + 'b'*20 + ' ' + 'c'*20 + ' ' + 'd'*20 + ' ' + 'e'*20 + ' '),

    # Тест 4
    ('xyzpqrstq\n7\np\npqrstq\nrst\nstq\nxyz\nxyzpq\nzpq', 'xyz pqrstq ')
])
def test_h(input_data, answer):
    sys.stdin = StringIO(input_data)
    
    result = main()
    assert result == answer

