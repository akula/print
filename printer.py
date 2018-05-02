# -*-coding: UTF-8 -*-
import serial
import logging, logging.handlers
import time
from label1 import label1
cur_date = time.strftime("%Y/%m/%d")

log = logging.getLogger('')
log.setLevel(logging.INFO)
FORMAT = '%(asctime)-15s %(message)s'
formater = logging.Formatter(FORMAT)
handler = logging.handlers.TimedRotatingFileHandler("record.log","D",1,0)
handler.suffix="%Y%m%d"
handler.setFormatter(formater)
log.addHandler(handler)
def receive():
    t = serial.Serial('COM6', 115200, timeout=2)
    p = serial.Serial('COM3')
    if t.isOpen():
        print('opening commuicate port \r\n')
        while True :
            if t.in_waiting > 0:
                data = t.read(14).decode('GB2312')
                print(data)
                log.info('get data: ' + data)
                msg = label1.replace('serialmsg',data)
                sendmsg = msg.replace('TDATE',cur_date).encode('GB2312')
                p.write(sendmsg)
                log.info('print data: ' + data)               
                print("\n")
                 
    else:
        print("error on open port")

if __name__ == '__main__':
    receive()