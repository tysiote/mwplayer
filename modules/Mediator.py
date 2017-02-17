import urllib.parse
import urllib.request
import urllib
import hashlib


class Mediator(object):
    def __init__(self, owner):
        self.owner = owner
        self.url = 'http://www.martinusmaco.sk/mwp/post.php'

    def send_data(self, values):
        data = urllib.parse.urlencode(values)
        binary_data = data.encode('utf-8')
        req = urllib.request.Request(self.url, binary_data)
        return urllib.request.urlopen(req).read()

    @staticmethod
    def hash_password(password):
        return hashlib.md5(password.encode('utf-8')).hexdigest()

    def register_new_user(self, username, password):
        values = dict()
        values["order"] = "register"
        values["username"] = username
        values["password"] = password
        return self.send_data(values)

    def login(self, username, password):
        values = dict()
        values["order"] = "login"
        values["username"] = username
        values["password"] = password
        return self.send_data(values)

    @staticmethod
    def validate_username(text):
        if len(text) < 4 or len(text) > 16:
            return False
        permitted_symbols = ('.', '_')
        temporary_text = text
        for symbol in permitted_symbols:
            temporary_text = temporary_text.replace(symbol, '')
        if not temporary_text.isalnum():
            return False
        return True

    @staticmethod
    def validate_password(text):
        return len(text) in [i for i in range(4, 17)]
        # return len(text) > 3 and len(text) < 17
