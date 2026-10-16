def parse_command(text: str):
    tokens = text.split()
    if not tokens:
        return None

    first_token = tokens[0]

    if not first_token.startswith('/') or first_token.startswith('//'):
        return None

    command_part = first_token.split('@')[0]
    
    command_name = command_part[1:].lower()

    if not command_name:
        return None

    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789_"
    
    for char in command_name:
        if char not in allowed_chars:
            return None

    arguments = tokens[1:]

    return (command_name, arguments)
