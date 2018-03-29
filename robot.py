# _*_ coding:utf-

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import random
import itchat

match_dict = {
        'Hi':'Hi',
        'Hello':'Hello',
        'new year':'HAPPY NEW YEAR!',
        'xin nian hao':'XIN NIAN HAO!',
        'good morning':'good morning',
        '88':'Have a Good dream!'
    }

question = ' '

from itchat.content import TEXT, MAP, NOTE, CARD, SHARING
from itchat.content import PICTURE, RECORDING, ATTACHMENT
from itchat.content import VIDEO, FRIENDS


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    msg.user.send('%s' %(msg.text))


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid'}.get(msg.type, 'fil')
    return'@%s@%s' % (typeSymbol, msg.fileName)


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet u!')


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    global question
    if msg.isAt:
        if msg.text[8:12]=='ans:':
            match_dict[question]=msg.text[12:]
            msg.user.send('I have learned it')
            pass    

        elif msg.text[8:] in match_dict:
            reply = match_dict[msg.text[8:]]
            msg.user.send('@%s,%s' % (msg.actualNickName, reply))
        else:
            msg.user.send("I do not know this question, please tell me the answer.")
            question=msg.text[8:]
    else:
        randid = random.randint(0, 100) % 100
        reply = "great"
        if(randid == 0):
            reply = 'Happy new year!'
        elif(randid == 1):
            reply = "hello !"
        elif(randid == 2):
            reply = "ok"
        elif(randid == 3):
            reply = "nice to meet you "
        else:
            pass

        msg.user.send(reply)




itchat.auto_login()
itchat.run(True)
#init_rand_dict()

