"""LZ-String decompressFromBase64 port (pieroxy/lz-string), decode side only."""
from __future__ import annotations

_B64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
_REV = {c: i for i, c in enumerate(_B64)}


def decompress_from_base64(s: str) -> str:
    s = "".join(s.split())
    if not s:
        return ""
    return _decompress(len(s), 32, lambda i: _REV[s[i]])


def _decompress(length: int, reset_value: int, get_next) -> str:
    dictionary: dict[int, str] = {}
    enlarge_in = 4
    dict_size = 4
    num_bits = 3
    entry = ""
    result: list[str] = []
    val = get_next(0)
    position = reset_value
    index = 1

    def read_bits(n: int) -> int:
        nonlocal val, position, index
        bits = 0
        maxpower = 1 << n
        power = 1
        while power != maxpower:
            resb = val & position
            position >>= 1
            if position == 0:
                position = reset_value
                val = get_next(index)
                index += 1
            bits |= (1 if resb > 0 else 0) * power
            power <<= 1
        return bits

    nxt = read_bits(2)
    if nxt == 0:
        c = chr(read_bits(8))
    elif nxt == 1:
        c = chr(read_bits(16))
    else:
        return ""
    dictionary[3] = c
    w = c
    result.append(c)
    while True:
        if index > length:
            return ""
        c = read_bits(num_bits)
        if c == 0:
            dictionary[dict_size] = chr(read_bits(8))
            c = dict_size
            dict_size += 1
            enlarge_in -= 1
        elif c == 1:
            dictionary[dict_size] = chr(read_bits(16))
            c = dict_size
            dict_size += 1
            enlarge_in -= 1
        elif c == 2:
            return "".join(result)
        if enlarge_in == 0:
            enlarge_in = 1 << num_bits
            num_bits += 1
        if c in dictionary:
            entry = dictionary[c]
        elif c == dict_size:
            entry = w + w[0]
        else:
            return ""
        result.append(entry)
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
        enlarge_in -= 1
        w = entry
        if enlarge_in == 0:
            enlarge_in = 1 << num_bits
            num_bits += 1
