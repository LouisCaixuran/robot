import itchat
from itchat.content import TEXT, MAP, NOTE, CARD, SHARING
from itchat.content import PICTURE, RECORDING, ATTACHMENT
from itchat.content import VIDEO, FRIENDS


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    msg.user.send('%s:%s' % (msg.type, msg.text))


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
    if msg.isAt:
        if ('hi' in msg.text):
            msg.user.send('hehe')
        else:
            msg.user.send(u'@%s,%s' % (
                msg.actualNickName, msg.text))


itchat.auto_login(True)
itchat.run(True)
