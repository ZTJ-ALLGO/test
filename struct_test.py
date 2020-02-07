import struct
# native byteorder
a = 12
buffer = struct.pack("ihb", 1, 2, a)
print(repr(buffer))
print(struct.unpack("ihb", buffer))
# data from a sequence, network byteorder
data = [1, 2]
data.append(a)
buffer = struct.pack("!ihb", *data)
# print(repr(buffer))
# print(struct.unpack("!ihb", buffer))
