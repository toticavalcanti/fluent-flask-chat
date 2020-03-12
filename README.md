# Fluent Code Chat

*Chatroom for coders*

> Example application for *[DevOPs - Docker - Python Web Development with Flask](https://www.codigofluente.com.br/devops/docker/)*.

## Installation

clone:
```
$ git clone https://github.com/toti/fluentchat.git
$ cd fluentchat
```
create & activate virtual env then install dependency:

with venv/virtualenv + pip:
```
$ python -m venv env  # use `virtualenv env` for Python2, use `python3` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt  # use `pip3` for Python3 on Linux & macOS
```
or with Pipenv:
```
$ pipenv install --dev
$ pipenv shell
```
generate database:
```
$ flask initdb

```
run the app and generate fake users and data inside the chat:
```
$ flask run
* Running on http://127.0.0.1:5000/
```
Test account:
* email: `admin@hello.com`
* password: `hello`

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
