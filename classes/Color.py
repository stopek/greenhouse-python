def hex_to_rgb(hex_string):
    r_hex = None
    g_hex = None
    b_hex = None

    str_len = len(hex_string)
    if hex_string.startswith("#"):
        if str_len == 7:
            r_hex = hex_string[1:3]
            g_hex = hex_string[3:5]
            b_hex = hex_string[5:7]
        elif str_len == 4:
            r_hex = hex_string[1:2] * 2
            g_hex = hex_string[2:3] * 2
            b_hex = hex_string[3:4] * 2
    elif str_len == 3:
        r_hex = hex_string[0:1] * 2
        g_hex = hex_string[1:2] * 2
        b_hex = hex_string[2:3] * 2
    else:
        r_hex = hex_string[0:2]
        g_hex = hex_string[2:4]
        b_hex = hex_string[4:6]

    return int(r_hex, 16), int(g_hex, 16), int(b_hex, 16)
