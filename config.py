class Config:
    def __int__(self, env):
        self.baseURL = {
            'devtp15': 'https://one-sites-devtp15.avizia.com/#',
            'qa': 'https://one-sites-qa.avizia.com/#',
            'staging': 'https://one-sites-stg.avizia.com/#',
            'preprod': 'https://one-sites-pre-prod.avizia.com/#'
        }[env]
