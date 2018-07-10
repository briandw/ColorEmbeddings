
def colorValueToRGB(colorValue, bit_depth):
    bit_mask = 2**bit_depth - 1
    b = (colorValue & bit_mask)
    g = ((colorValue >> bit_depth) & bit_mask)
    r = ((colorValue >> bit_depth * 2)  & bit_mask)
    return (r,g,b)

def RGBToColorValue(r, g, b, bit_depth):
    color_value = r
    color_value = color_value << bit_depth
    color_value += g
    color_value = color_value << bit_depth
    color_value += b
    return color_value

def compressColor(colorValue, start_bit_depth, end_bit_depth):
    start_max_val = int(2**start_bit_depth)
    end_max_val = int(2**end_bit_depth)
    devisor = int(start_max_val // end_max_val)
    
    bit_mask = start_max_val - 1
    b = (colorValue & bit_mask) // devisor
    g = ((colorValue >> start_bit_depth) & bit_mask) // devisor
    r = ((colorValue >> start_bit_depth * 2)  & bit_mask) // devisor
    return (r,g,b)

def expandColor(colorValue, start_bit_depth, end_bit_depth):
    start_max_val = int(2**start_bit_depth)
    end_max_val = int(2**end_bit_depth)
    factor = int(end_max_val // start_max_val)
    
    bit_mask = start_max_val - 1
    b = (colorValue & bit_mask) * factor + factor/2
    g = ((colorValue >> start_bit_depth) & bit_mask) * factor + factor/2
    r = ((colorValue >> start_bit_depth * 2)  & bit_mask) * factor + factor/2
    return (int(r), int(g), int(b))