def add_invisible_watermark(text, user_id):
    mapping = {'0': '\u200B', '1': '\u200C'}
    binary_id = ''.join(format(ord(c), '08b') for c in user_id)
    watermark = ''.join(mapping.get(b, b) for b in binary_id)
    return watermark + text
