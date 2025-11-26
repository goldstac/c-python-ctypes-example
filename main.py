import ctypes
main = ctypes.CDLL("./main.dll")
print(main.add(7,7))
