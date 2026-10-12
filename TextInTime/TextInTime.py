import re


def parse_duration(duration_str: str) -> int:
  # Проверяем, что строка вообще не пустая
  if not duration_str:
    raise ValueError('invalid duration')

  # Паттерн строго проверяет порядок: h -> m -> s
  pattern = r'^(?:(?P<hours>\d+)h)?(?:(?P<minutes>\d+)m)?(?:(?P<seconds>\d+)s)?$'
  match = re.match(pattern, duration_str)

  if not match:
    raise ValueError('invalid duration')

  group_dict = match.groupdict()

  # Важнейшая проверка: в строке должна быть ХОТЯ БЫ ОДНА цифра.
  if all(v is None for v in group_dict.values()):
    raise ValueError('invalid duration')

  # Превращаем найденные строки в числа (если None, то 0)
  hours = int(group_dict['hours']) if group_dict['hours'] else 0
  minutes = int(group_dict['minutes']) if group_dict['minutes'] else 0
  seconds = int(group_dict['seconds']) if group_dict['seconds'] else 0

  return hours * 3600 + minutes * 60 + seconds

