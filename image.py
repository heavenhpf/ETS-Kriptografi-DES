import base64
import des

# Membuka image yang akan dienkripsi
with open("images/test2.jpg", "rb") as imageFile:
    img_byte = base64.b64encode(imageFile.read())

    img_str = img_byte.decode("utf-8")


# Mengubah image ke dalam bentuk biner
len_img_str = len(img_str)    
img_bin=''.join(format(ord(x), '07b') for x in img_str)

len_img_bin= len(img_bin)
img_bin_temp = img_bin
pad_len = 64 - len_img_bin%64
for i in range(pad_len):
    img_bin+='0'
pad_export = str(pad_len)
# Mengubah biner ke hex
img_hex = '%0*X' % ((len(img_bin) + 3) // 4, int(img_bin, 2))

img_enc=""
# Memasukkan key
K = '133457799BBCDFF1'
# Mengenkripsi image dengan bantuan des.py
for i in range(0,len(img_hex),16):
    img_enc=img_enc + des.encrypt(img_hex[i:i+16],K)
