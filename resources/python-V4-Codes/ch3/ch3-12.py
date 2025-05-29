def rect(width = 5, length = 15):
    perim = (width + length) * 2
    area = width * length
    return perim, area
#-------------------------------------
perim , area = rect()
print("default: perim = ", perim, ", area = ", area)
perim , area = rect(8)
print("length is default: perim = ", perim, ", area = ", area)
perim, area = rect(5, 12)
print("no default: perim = ", perim, ", area = ", area)
