import binascii
import time

"Manju send-off gift - 16-Apr-2020"

fa = open("bb1.bmp","rb")
fa = fa.read()

fb = open("bb1a.bmp","rb")
fb = fb.read()

fc = open("bb2.bmp","rb")
fc = fc.read()

full_data = []
pix_range_x = 128
pix_range_y = 128
for xx in range(3):
    for f in [fa,fb,fc]:
        idd = f
        pix = binascii.hexlify(idd)[236:]
        pix = pix.replace(b"f",b")")
        pix = pix.replace(b"7",b" ")
        pix = pix.replace(b"8",b" ")
        pix = pix.replace(b"4",b" ")
        pix = pix.replace(b"0",b" ")
        pix = pix.replace(b"6",b" ")
        pix_s = 1
        data = ""
        for a in range(pix_range_y):
            print_data = pix[-pix_s:-pix_s+pix_range_x]
            print_data = print_data.decode("utf-8")
            data = data + "\n" + print_data
            pix_s = pix_s + pix_range_x

        full_data.append(data)

while True:
    for d in full_data:
        print(d)
        time.sleep(3)
    
