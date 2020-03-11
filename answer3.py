import hashlib
import json
import time
import urllib
import urllib.request


class AIChatCls():
    def __init__(self, app_id='2129956076', app_key='HZSbkoSOYR4rk4Ft',
                 url='https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat'):
        self.app_id = app_id
        self.app_key = app_key
        self.url = url

    def getReqSign(self, params):
        ''' ��ȡǩ����Ϣ '''

        # 1. �ֵ��������� (�� key ��������)
        params = dict(sorted(params.items(), key=lambda x: x[0]))

        # 2. ����ǩ����Ϣ
        url_str = ''
        for k, v in params.items():
            if k != 'app_key':
                pass
                #url_str += f "{k}={urllib.parse.quote(str(v), safe='')}&"
            else:
                url_str += f"app_key={urllib.parse.quote(str(params['app_key']), safe='')}"
                hash_md5 = hashlib.md5(url_str.encode("utf8"))
                sign = hash_md5.hexdigest().upper()
        return sign

    def getReqParams(self, question):
        '''
        ��������������ǩ����Ϣ�� question���������������
        :param question: ���췢����ʻ���ش�
        :return: �����������
        '''
        params = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'session': int(time.time() * 10000)
        }
        params['question'] = question
        params['sign'] = self.getReqSign(params)
        return params

    def doPost(self, question='��ã����ʲô���֣�'):
        '''
        ������������
        :param question:
        :return:
        '''
        params = self.getReqParams(question=question)
        req_data = urllib.parse.urlencode(params).encode(encoding='utf-8')
        req = urllib.request.Request(self.url, data=req_data)
        rsp = urllib.request.urlopen(req)
        rsp_str = rsp.read().decode('utf-8')
        rsp_dict = json.loads(rsp_str)
        if rsp_dict.get('ret', '') == 0:
            return rsp_dict['data']['answer']
        else:
            print(rsp_dict)
        return None


if __name__ == '__main__':
    # 1����ȡ�ظ�����
    ac = AIChatCls()
    # reply = ac.doPost()
    # reply = ac.doPost('������')
    reply = ac.doPost(question='�㹤������')
    print(reply)

    # 2��ģ������
    # ac = AIChatCls()
    # reply = ac.doPost(question='�㹤������')
    # while 1:
    #     print('�����ˣ�',reply,'\n')
    #     print('�ң�')
    #     question = input()
    #     reply = ac.doPost(question=question)

