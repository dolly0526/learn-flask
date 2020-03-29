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
