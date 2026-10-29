
def format_phone(digits):
    """Приводит строку из 11 цифр к виду +7 (XXX) XXX-XX-XX."""
    if len(digits)!=11 or not digits.isdigit():
        raise ValueError("expected 11 digits")
    code=digits[1:4]
    part1=digits[4:7]
    part2=digits[7:9]
    part3=digits[9:11]
    return (f"+7 ({code}) {part1}-{part2}-{part3}")