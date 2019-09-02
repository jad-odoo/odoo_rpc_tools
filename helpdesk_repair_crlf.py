from prefix import *
from files import *
import os

"""
Some lines of the Helpdesk Tickets import file are endend by 0x0D instead of 0x0D 0x0A.
This script creates a new import file by adding 0x0A after each 0x0D not followed by 0x0A.
"""

src_file = dest_helpdesk_ticket_2
dst_file = src_file+'.newcrlf'

with open(src_file, 'rb') as rf, open(dst_file, "w") as wf:
    while True:
        byte_s = rf.read(1)
        if not byte_s:
            break

        wf.write(byte_s)

        if ord(byte_s) == 13:
            byte_next = rf.read(1)
            if not byte_next:
                break
            if ord(byte_next) != 10:
                wf.write(chr(10))
                print ('Repair new line')
            # wf.write(byte_next)
            rf.seek(-1,1)
                
os.rename(dst_file, src_file)