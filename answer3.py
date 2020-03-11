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
        ''' 获取签名信息 '''

        # 1. 字典升序排序 (按 key 升序排列)
        params = dict(sorted(params.items(), key=lambda x: x[0]))

        # 2. 生成签名信息
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
        向请求参数中添加签名信息和 question，并返回请求参数
        :param question: 聊天发起的问话或回答
        :return: 返回请求参数
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

    def doPost(self, question='你好，你叫什么名字？'):
        '''
        发起聊天请求
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
    # 1】获取回复内容
    ac = AIChatCls()
    # reply = ac.doPost()
    # reply = ac.doPost('你多大了')
    reply = ac.doPost(question='你工作了吗？')
    print(reply)

    # 2】模拟聊天
    # ac = AIChatCls()
    # reply = ac.doPost(question='你工作了吗？')
    # while 1:
    #     print('机器人：',reply,'\n')
    #     print('我：')
    #     question = input()
    #     reply = ac.doPost(question=question)

