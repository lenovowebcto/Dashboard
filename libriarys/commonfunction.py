#/usr/bin/env python
#coding = utf8

from random import Random
import hashlib

def random_str(randomlength=8):
    '''
    produce a random string.
    '''
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

def md5(str):
    m = hashlib.md5()
    m.update(str.encode("gb2312"))
    return m.hexdigest()