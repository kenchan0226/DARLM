# coding=utf-8
import configparser
import json
class Config(object):

    def __init__(self):
        super(Config, self).__init__()
        self.cfg = configparser.ConfigParser()

        self.hparams = {}

    def load_config(self, file_path):
        self.cfg.read(file_path)

        for item in self.cfg.items('hparam'):
            key = item[0]
            value = item[1]
            if value == 'False' or value == 'True':
                value = (value == 'True')
            elif value.isdigit() == True:
                value = int(value)
            else:
                try:
                    value = float(value)
                except:
                    pass
            if key in self.hparams:
                print('*Warning, a redundant key hyper-paramter.')
            else:
                self.hparams[key] = value

    def set(self, hparam, value):
        if hparam in self.hparams:
            print('*Warning, a redundant key hyper-paramter.')
        else:
            self.hparams[hparam] = value

    def lists(self):
        return self.hparams

    def __getitem__(self, key):
        if key in self.hparams:
            return self.hparams[key]
        else:
            return None

    def save_config(self, file_path):
        for key in self.hparams:
            value = self.hparams[key]

            self.cfg.set('hparam', key, value)

        with open(file_path, 'w') as fd:
            cfg.write(fd)
