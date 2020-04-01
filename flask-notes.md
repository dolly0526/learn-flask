# Learning Flask

## 学前准备

```bash
# version: python3.7.3
python3 -m venv learning-flask/venv
pip install flask
```

## 认识Web

### URL详解

![](https://tva1.sinaimg.cn/large/00831rSTly1gd344no3kqj30lo0cq7dj.jpg)

### Web服务器/应用服务器/Web应用框架

![](https://tva1.sinaimg.cn/large/00831rSTly1gd34ymuoaoj30sc0bsgs7.jpg)

## URL与视图函数

### Flask简介

![](https://tva1.sinaimg.cn/large/00831rSTly1gdb4w11df9j30qw0b6k3d.jpg)

### 第一个Flask程序

![](https://tva1.sinaimg.cn/large/00831rSTly1gd5g42wwh6j30nm0hsk21.jpg)

### debug模式

![](https://tva1.sinaimg.cn/large/00831rSTly1gd5gcr3xxhj30mo0bgjzs.jpg)

### 配置文件

![](https://tva1.sinaimg.cn/large/00831rSTly1gdb6athy9zj30n009gtfa.jpg)

### URL与视图函数的映射

![](https://tva1.sinaimg.cn/large/00831rSTly1gdb6eop4x7j30lg0g4thl.jpg)

![](https://tva1.sinaimg.cn/large/00831rSTly1gdb7osai58j30ng09uqat.jpg)

### url_for( )

![](https://tva1.sinaimg.cn/large/00831rSTly1gdb7qeld82j30mo0a2wl4.jpg)

![](https://tva1.sinaimg.cn/large/00831rSTly1gdb7reb9o8j30me07sdl2.jpg)

### 自定义URL转换器

![](https://tva1.sinaimg.cn/large/00831rSTly1gddfm7mgnoj30k80acgro.jpg)

```python
from flask import Flask, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)

class TelephoneConverter(BaseConverter):
    regex = r'1[85734]\d{9}'

class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split('+')

    def to_url(self, value):
        print(value)
        return 'hello'

app.url_map.converters['tel'] = TelephoneConverter
app.url_map.converters['list'] = ListConverter

@app.route('/')
def hello_world():
    print(url_for('posts', boards=['a', 'b']))
    return 'Hello World!'

@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return '您输入的user_id为: %s' % user_id

@app.route('/telephone/<tel:my_tel>/')
def my_tel(my_tel):
    return '您的手机号是: %s' % my_tel

@app.route('/posts/<list:boards>/')
def posts(boards):
    print(boards)
    return '您提交的板块是: %s' % boards

if __name__ == '__main__':
    app.run()
```

### 必会的小细节

![](https://tva1.sinaimg.cn/large/00831rSTly1gddfoea2vaj30mq0a410k.jpg)

![](https://tva1.sinaimg.cn/large/00831rSTly1gddfq2s1g7j30my0dywqy.jpg)

### 重定向

![](https://tva1.sinaimg.cn/large/00831rSTly1gddfu82cxaj30mw0bkdrr.jpg)

```python
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login/')
def login():
    return '这是登录页面'

@app.route('/profile/')
def profile():
    # http://127.0.0.1:5000/profile/?name=dolly
    if request.args.get('name'):
        return '个人中心页面'
    # http://127.0.0.1:5000/profile
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()
```

### Response

![](https://tva1.sinaimg.cn/large/00831rSTly1gde7pa91oqj30m40ae10u.jpg)

## 模版

### 模版简介

![](https://tva1.sinaimg.cn/large/00831rSTly1gde8endml8j30qo0cutks.jpg)

### 使用模版

![](https://tva1.sinaimg.cn/large/00831rSTly1gde8g4zqfsj30mq02g0vm.jpg)

### 模版传参

