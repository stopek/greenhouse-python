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


def wavelength_to_rgb(wavelength, gamma=0.80, intensity_max=255):
    factor = None
    red = None
    green = None
    blue = None

    if 380 <= wavelength < 440:
        red = -(wavelength - 440) / (440 - 380)
        green = 0.0
        blue = 1.0
    elif 440 <= wavelength < 490:
        red = 0.0
        green = (wavelength - 440) / (490 - 440)
        blue = 1.0
    elif 490 <= wavelength < 510:
        red = 0.0
        green = 1.0
        blue = -(wavelength - 510) / (510 - 490)
    elif 510 <= wavelength < 580:
        red = (wavelength - 510) / (580 - 510)
        green = 1.0
        blue = 0.0
    elif 580 <= wavelength < 645:
        red = 1.0
        green = -(wavelength - 645) / (645 - 580)
        blue = 0.0
    elif 645 <= wavelength < 781:
        red = 1.0
        green = 0.0
        blue = 0.0
    else:
        red = 0.0
        green = 0.0
        blue = 0.0

    if 380 <= wavelength < 420:
        factor = 0.3 + 0.7 * (wavelength - 380) / (420 - 380)
    elif 420 <= wavelength < 701:
        factor = 1.0
    elif 701 <= wavelength < 781:
        factor = 0.3 + 0.7 * (780 - wavelength) / (780 - 700)
    else:
        factor = 0.0

    r = round(intensity_max * pow(red * factor, gamma)) if red != 0.00 else 0
    g = round(intensity_max * pow(green * factor, gamma)) if green != 0.00 else 0
    b = round(intensity_max * pow(blue * factor, gamma)) if blue != 0.00 else 0

    return r, g, b
