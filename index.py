# encoding: utf8

from flask import Flask, request, render_template
from necaptcha import SecretPair, NECaptchaVerifier

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def login():
    captcha_id = "YOUR_CAPTCHA_ID" # 验证码id
    secret_id = "YOUR_SECRET_ID"   # 验证码密钥对id
    secret_key = "YOUR_SECRET_KEY" # 验证码密钥对key

    verifier = NECaptchaVerifier(captcha_id, SecretPair(secret_id, secret_key))
    validate = request.form[verifier.REQ_VALIDATE]
    user = "{'user':123345}"
    result = verifier.verify(validate, user);

    print result
    msg = "<html><body><h1>验证成功 <a href='/'>返回首页</a></h1></body></html>" \
        if result else "<html><body><h1>验证失败 <a href='/'>返回首页</a></h1></body></html>"
    return msg

if __name__ == "__main__":
    app.run()