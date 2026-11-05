
def parse_config_line(line):
    """Разбирает строку конфига вида key=value в пару (key, value)."""
    if not "=" in line:
        raise ValueError("missing '='")
        
    new = line.split("=", 1)
    
    key = new[0].strip()

    if len(key) == 0:
        raise ValueError("empty key")
        
    value = new[1].strip()
    
    return key, value