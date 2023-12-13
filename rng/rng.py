import argparse
import logging
import serial
import sys
import time

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='sha256bit.cli')
    levels = ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
    parser.add_argument('--log-level', default='WARNING', choices=levels)
    parser.add_argument('--size', help='size of output', default=None, type=int)
    parser.add_argument('--block-size', help='read block size', default=1024*1024, type=int)
    parser.add_argument('--out', help='output file path', default=None, type=str)
    parser.add_argument('device', nargs=1, help='RNG device', type=str)
    args = parser.parse_args()
    logging.basicConfig(format='%(message)s', level=args.log_level)

device = args.device[0]
size = args.size 
out_path = args.out
block_size = args.block_size

if out_path is None:
    out = sys.stdout
else:
    out = open(out_path,'wb')

start = time.time()

with serial.Serial(device,exclusive=True) as ser:
    while size > block_size:
        dat = ser.read(block_size)
        out.write(dat)
        size -= block_size
    dat = ser.read(size)
    out.write(dat)

end = time.time()

ms = int((end-start)*1000)

data_rate = int(args.size / (end-start))
logging.info("time: %d ms"%ms)
logging.info("size: %d bytes"%args.size)
logging.info("data rate: %d bytes/s"%data_rate)