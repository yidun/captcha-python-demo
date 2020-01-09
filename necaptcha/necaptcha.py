#!coding:utf8
import random
import json
import time
from hashlib import md5
import urllib
import urllib.request

VERSION = "v2"

"""
验证码密钥对
"""
class SecretPair(object):
    def __init__(self, secret_id, secret_key):
        self.secret_id = secret_id
        self.secret_key = secret_key

"""
验证码二次校验
"""
class NECaptchaVerifier(object):
    REQ_VALIDATE = "NECaptchaValidate"
    API_URL = "http://c.dun.163yun.com/api/v2/verify"

    def __init__(self, captcha_id, secret_pair):
        self.captcha_id = captcha_id
        self.secret_pair = secret_pair

    def verify(self, validate, user):
        params = {}
        params["captchaId"] = self.captcha_id
        params["validate"] = validate
        params["user"] = user
        params["secretId"] = self.secret_pair.secret_id
        params["version"] = VERSION
        params["timestamp"] = int(time.time() * 1000)
        params["nonce"] = int(random.random()*100000000)
        params["signature"] = self.sign(params)

        print("debug: ", params)

        try:
            params = urllib.parse.urlencode(params)
            params = params.encode('utf-8')
            request = urllib.request.Request(self.API_URL, params)
            content = urllib.request.urlopen(request, timeout=5).read()
            ret = json.loads(content)
            print("debug: ", ret)
            return ret['result'] if 'result' in ret else False
        except Exception as  ex:
            print("调用API接口失败:", str(ex))

    def sign(self, params=None):
        buff = ""
        for k in sorted(params.keys()):
            buff += str(k)+ str(params[k])
        buff += self.secret_pair.secret_key
        buff = buff.encode('utf-8')
        return md5(buff).hexdigest()