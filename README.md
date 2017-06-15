# captcha-python-demo
易盾验证码python演示

# 运行演示
* `pip install Flask`
* 修改index.html
```
initNECaptcha({
  captchaId: 'YOUR_CAPTCHA_ID', // <-- 这里填入在易盾官网申请的验证码id
  element: '#captcha_div',
  mode: 'float',
  width: '320px',
  onVerify: function(err, ret){
    if(!err){
        // ret['validate'] 获取二次校验数据
    }
  }
}, function (instance) {
  // 初始化成功后得到验证实例instance，可以调用实例的方法
}, function (err) {
  // 初始化失败后触发该函数，err对象描述当前错误信息
})
```

* 修改index.py

```
    captcha_id = "YOUR_CAPTCHA_ID" # 验证码id
    secret_id = "YOUR_SECRET_ID"   # 验证码密钥对id
    secret_key = "YOUR_SECRET_KEY" # 验证码密钥对key
```

* `python index.py`
* 访问 http://127.0.0.1:5000/