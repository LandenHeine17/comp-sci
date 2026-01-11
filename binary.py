data = [255]

buffer = bytes(data)
print(buffer)
f = open("binary.txt", "bw")

f.write(buffer)

f.close()

