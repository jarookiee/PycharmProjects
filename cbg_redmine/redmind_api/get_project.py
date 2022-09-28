
import requests,codecs

TOKEN = '29e73d2ab2ef5957bd8fa17b3820b7ee'  # 填写自己的token
HOST = 'cbg.pm.netease.com'

def escape(text):
    r1 = codecs.getdecoder('unicode_escape')(text)[0]
    print(r1)


def get_project():
    param = {
        'token' : TOKEN,
        'host' : HOST
    }

    url = 'http://redmineapi.nie.netease.com/api/project'
    r = requests.get(url,params=param)
    if r.status_code == 200:
        escape(r.text)
    else:
        print('wrong')

if __name__ == '__main__':
    get_project()