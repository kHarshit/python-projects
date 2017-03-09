img = input("Enter a binary no: ")  # for example: 111111100001001100
# try to generate a hollow rectangle: 111111100001111111
# or a triangle or any other figure you like :)

img_out = ""
position = 0

for i in img:
    if i != '1' and i != '0':
        raise ValueError("You need to enter no in binary only!\n Check " + i + " at " + str(position + 1) + "th position")
    if i == '1':
        img_out += "*"
    else:
        img_out += " "
    position += 1
    if position % 6 == 0:
        img_out += "\n"

print(img_out)