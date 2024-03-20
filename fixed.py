#!/usr/local/bin/python3.7
# encoding: utf-8

import datetime
import math

def fixedfloat(value, precision=32, base=16):
    format_spec = {2: 'b', 8: 'o', 10: 'd', 16: 'x'}[base]
    n, value = divmod(value, 1)
    int_part = '{:{base}}'.format(int(n), base=format_spec)
    float_part = ''
    while len(float_part) < precision//(base-1).bit_length():
        n, value = divmod(value * base, 1)
        float_part += '{:{base}}'.format(int(n), base=format_spec)
    return float_part, int_part

def main():
    now = datetime.datetime.now()
    epoch = int(now.timestamp())
    microsecond = now.microsecond / 1000000.0
    print(epoch)
    print('{:08x}'.format(epoch))
    print(microsecond)
    print(microsecond.hex())
    print(fixedfloat(microsecond, base=16))
    v = fixedfloat(1/8)
    print(v, len(v))
    print(fixedfloat(now.timestamp(), base=16), now.timestamp())
    print((16-1).bit_length())
    
if __name__ == '__main__':
    main()
