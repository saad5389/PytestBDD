class TestConfig:
    def __init__(self, env):
        self.base_url = {
            'qa': 'https://one-sites-qa.avizia.com/#/login',
            'staging': 'https://one-sites-stg.avizia.com/#/login',
            'preprod': 'https://one-sites-pre-prod.avizia.com/#/login'
        }[env]

        self.app_port = {
            'qa': '80',
            'staging': '8080',
        }[env]
