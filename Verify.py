from psutil import net_if_addrs, cpu_count
import requests
import time
import pyDes
from binascii import b2a_hex, a2b_hex


def current_time():
    response = requests.get("http://www.baidu.com")
    if response.status_code == 200:
        ts = response.headers['Date']
        ltime = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")  # 格林尼治时间
        # print(time.mktime(ltime))
        # ttime = time.localtime(time.mktime(ltime) + 8 * 60 * 60)  # 北京时间
        # print(time.mktime(ttime))
        # now_time = ttime
        # print(now_time)
        now_time = time.mktime(ltime)
        return int(now_time)


def get_mac():
    for k, v in net_if_addrs().items():
        for item in v:
            address = item[1]
            if "-" in address and len(address) == 17:
                return address


def machine_code():
    try:
        mac_addr = get_mac()
        mac_addr = mac_addr.replace('-', '')
        mec_code = my_encryption(mac_addr)
        return mec_code
    except:
        return '无法获取机器码，请联系卖家'


def creat_activation(code='5262050699d0c9eae23bd4b758eacc51', day=3000):
    delayed = day * 24 * 60 * 60
    # delayed=150
    cur_time = current_time()
    mec_text = my_decrypt(code)
    text = mec_text + '-' + str(cur_time + delayed)
    activate = my_encryption(text)
    print(activate)
    return activate


def check_activation(code='5262050699d0c9eae23bd4b758eacc51'):
    text = my_decrypt(code)
    data = text.split('-')
    mac_addr = data[0]
    end_stamp = int(data[1])
    date = time.localtime(end_stamp)
    print(date)


key = 'zzz123aa'
iv = 'aaa12311'


def my_encryption(text=''):  # 加
    # mac_addr = get_mac()
    # mac_addr = mac_addr.replace('-', '')
    # hex_nums = mac_addr.split('-')
    # dec_nums = []
    # codes = []
    # for num in hex_nums:
    #     dec_nums.append(int(num, 16))
    # for dec_num in dec_nums:
    #     if 0 <= dec_num < 80:
    #         y = -3 * dec_num + 498
    #         codes.append(str(y))
    #     elif 80 <= dec_num < 200:
    #         y = 4 * dec_num + 182
    #         codes.append(str(y))
    #     else:
    #         y = 2 * dec_num - 296
    #         codes.append(str(y))
    # codes.append(str(cpu_count()*100))
    # code='-'.join(codes)
    k = pyDes.des(key, pyDes.CBC, iv, pad=None, padmode=pyDes.PAD_PKCS5)  # 密钥 加密模式 偏移量 xx 填充
    code_2 = k.encrypt(text)  # 加密,结果为2进制
    code_16 = b2a_hex(code_2)  # 转16进制
    code = bytes.decode(code_16)  # byte转str
    # print(code_2)
    # print(code_16)
    # print(code)
    return code


def my_decrypt(code='b63d7a7e2d8d1aca'):  # 解
    code_16 = str.encode(code)  # str转byte
    code_2 = a2b_hex(code)
    k = pyDes.des(key, pyDes.CBC, iv, pad=None, padmode=pyDes.PAD_PKCS5)
    text = k.decrypt(code_2)
    text = bytes.decode(text)
    # print(code_16)
    # print(code_2)
    # print(text)
    return text

if __name__=='__main__':
# print(my_decrypt('5262050699d0c9ea68549f891d8dfa0d3eac8dc4302f6a2c'))
# machine_code()
    creat_activation('5262050699d0c9eae23bd4b758eacc51')
# check_activation('5262050699d0c9ea68549f891d8dfa0d309bf07ba6c6790b')
# my_encryption()
# my_decrypt()
