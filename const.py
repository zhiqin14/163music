class Const:
    def __init__(self):
        self.is_login = False
        self.cookie = open('cookie').read()
        self.api_url = 'https://cloudmusic.api.zhiqin.eu.org'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                        'cookie': self.cookie}
        self.login_status = '/login/status'
        self.logout = '/logout'
        self.key_generate = '/login/qr/key'
        self.qr_generate = '/login/ar/create'
        self.qr_scan_status = '/login/qr/check'
        self.send_sms_code = '/captcha/sent'
        self.verify_sms_code = '/captcha/verify'
        self.get_user_detail = '/user/detail'
        self.get_user_level = 'user/level'
        