# captcha-python-demo
易盾验证码python演示

# 运行演示
* `pip install Flask`
* 修改index.html
```
var opts = {
    "element": "captcha_div",
    "captchaId": "YOUR_CAPTCHA_ID", // <-- 验证码id
    "width": 320
  }
```

* 修改index.py

```
    captcha_id = "YOUR_CAPTCHA_ID" # 验证码id
    secret_id = "YOUR_SECRET_ID"   # 验证码密钥对id
    secret_key = "YOUR_SECRET_KEY" # 验证码密钥对key
```

* `python index.py`
* 访问 http://127.0.0.1:5000/