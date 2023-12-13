import serial

device = '/dev/tty.usbmodemRNG11'

out = bytearray()
with serial.Serial(device,rtscts=True) as ser:
    fromZero = False
   
    while True:
        sof = 'sofr'
        pos=0
        head = bytearray()
        while pos < 4:
            b = ser.read()
            if b == sof[pos].encode():
                pos += 1
                head += b
            else:
                print("%d 0x%02x"%(pos,int.from_bytes(b,byteorder='little')))
                pos = 0
                head = bytearray()
        addr = int.from_bytes(ser.read(4),byteorder='little')
        dat = ser.read(16)
        checksum = int.from_bytes(ser.read(4),byteorder='little')
        c = addr
        for b in dat:
            c += b
        print("0x%08x: "%addr,end="")
        i = int.from_bytes(dat,byteorder='little')
        print("%032x"%i)
        if c != checksum:
            print("checksum mismatch")
            print("computed: 0x%08x"%c)
            print("received: 0x%08x"%checksum)
            print("header: 0x%08x"%(int.from_bytes(head,byteorder='little')))
            fromZero = False
        else:
            if addr == 0x20001fe0:
                fromZero = True
                out = bytearray()
            if fromZero:
                out +=dat
                if addr == 0x20001ff0:
                    break

if 0:
    with open("ram.bin","wb") as f:
        f.write(out)