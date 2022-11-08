# -*- coding: utf-8 -*-
#Hanya sekedar SC copas By: ─╼╼࿋͜͡ᬼ͜͡⁜͜͡ʟ͜͡е͜͡α͜͡β͜͡ɵ͜͡τ͜͡ʂ͜͡⁜͜͡ѵ͜͡е͜͡ʀ͜͡ʂ͜͡і͜͡ɵ͜͡ɳ͜͡⁜ᬽ͜͡࿋╾╾─
from linepy import *
from linepy import Menu
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from threading import Thread, activeCount
from shutil import copyfile
from subprocess import check_output
from bs4 import BeautifulSoup
import time, random, signal, pytz, subprocess, atexit, ctypes, livejson, sys, shutil, json, codecs, ast, threading, glob, re, string, asyncio, os, traceback, requests, six, urllib, urllib.parse
rd = ["0","1","2","3","4","5","6","7","8","9"]
h1=random.choice(rd)
h2=random.choice(rd)
h3=random.choice(rd)
h4=random.choice(rd)
h5=random.choice(rd)
h6=random.choice(rd)
h7=random.choice(rd)
h8=random.choice(rd)
h9=random.choice(rd)
ha=random.choice(rd)
hb=random.choice(rd)
hc=random.choice(rd)
hd=random.choice(rd)
he=random.choice(rd)
hf=random.choice(rd)
hg=random.choice(rd)
hi=random.choice(rd)
hj=random.choice(rd)
hk=random.choice(rd)
head="CHANNELCP\t2."+h1+"."+h2+"\tAndroid OS\t10."+h3+"."+h4+'"'
head1="CHANNELCP\t2."+h5+"."+h6+"\tAndroid OS\t10."+h7+"."+h8+'"'
head2="CHANNELCP\t2."+h9+"."+ha+"\tAndroid OS\t10."+hb+"."+hc+'"'
head3="CHANNELCP\t2."+hd+"."+he+"\tAndroid OS\t10."+hf+"."+hg+'"'
head4="CHANNELCP\t2."+hi+"."+hj+"\tAndroid OS\t10."+hk+"."+h1+'"'
head5="CHANNELCP\t2."+h2+"."+h3+"\tAndroid OS\t10."+h4+"."+h5+'"'
head6="CHANNELCP\t2."+h6+"."+h7+"\tAndroid OS\t10."+h8+"."+h9+'"'
with open('tokenku.json', 'r') as bolo:
     pin = json.load(bolo)
cl = LINE(pin["token"],appName="{}".format(head))
pin['token'] = cl.authToken
ka = LINE(pin["token2"],appName="{}".format(head1))
pin['token2'] = ka.authToken
kb = LINE(pin["token3"],appName="{}".format(head2))
pin['token3'] = kb.authToken
kc = LINE(pin["token4"],appName="{}".format(head3))
pin['token4'] = kc.authToken
kd = LINE(pin["token5"],appName="{}".format(head4))
pin['token5'] = kd.authToken
ke = LINE(pin["token6"],appName="{}".format(head5))
pin['token6'] = ke.authToken
k1 = LINE(pin["token7"],appName="{}".format(head6))
pin['token7'] = k1.authToken
#==============[●●●●●●]==============#
print ("login succes")
call = cl
linePoll = OEPoll(cl)
Bismillah=[cl,ka,kb,kc,kd]
Amin=[ka,kb,kc,kd,ke]
Aakun=[kb,kc,kd,ke]
Bakun=[ka,kc,kd,ke]
Cakun=[ka,kb,kd,ke]
Dakun=[ka,kc,kb,ke]
Eakun=[ka,kb,kd,kc]
mid = cl.getProfile().mid
Amid = ka.getProfile().mid
Bmid = kb.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kd.getProfile().mid
Emid = ke.getProfile().mid
Smid = k1.getProfile().mid
Alfiah=[mid,Amid,Bmid,Cmid,Dmid,Emid,Smid]
Zie = ["u813371351618d02e65acf4c8f857ef30"]
Introvert = Alfiah+Zie
botlist=[cl,ka,kb,kc,kd,ke,k1]
msg_dict = {}
msg_dict1 = {}
#==============[ Main Json ]==============#
Leakiller = livejson.File('settingSB.json')
wait = {
    "blacklist":{}
}
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
mulai = time.time()
smuleaudio = {}
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])) > timedelta(1):
            del msg_dict1[msg_id]
def atend():
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
atexit.register(atend)
def atend1():
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4,separators=(',', ': '))
atexit.register(atend)
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)
def likePost(self, mid, postId, likeType=1001):
    if mid is None:
        mid = cl.profile.mid
    if likeType not in [1001,1002,1003,1004,1005,1006]:
        raise Exception('Invalid parameter likeType')
    params = {'homeId': mid, 'sourceType': 'TIMELINE'}
    url = cl.server.urlEncode(cl.server.LINE_TIMELINE_API, '/v23/like/create', params)
    data = {'likeType': likeType, 'postId': postId, 'actorId': mid}
    r = cl.server.postContent(url, data=data, headers=cl.server.channelHeaders)
    return r.json()
def createComment(self, mid, postId, text):
    if mid is None:
        mid = self.profile.mid
    params = {'homeId': mid, 'sourceType': 'TIMELINE'}
    url = self.server.urlEncode(self.server.LINE_TIMELINE_API, '/v39/comment/create.json', params)
    data = {'commentText': text, 'activityExternalId': postId, 'actorId': mid}
    data = json.dumps(data)
    r = self.server.postContent(url, data=data, headers=self.server.timelineHeaders)
    return r.json()
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "「Member Join {}」\ ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+Leakiller["sambutan"]+"\ndi group : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def command(text):
    pesan = text.lower()
    if pesan.startswith(Leakiller["keyCmd"]):
        cmd = pesan.replace(Leakiller["keyCmd"],"")
    else:
        cmd = "command"
    return cmd
def help():
    key = Leakiller["keyCmd"]
    key = key.title()
    helpMessage = "═══════❀ˡᵉᵃ❀═══════╗\n║「ᵐᵉⁿᵘ ᵖʳᵒᵗᵉᶜᵗⁱᵒⁿ ᵖʸ3 ˡᵉᵃᵏⁱˡˡᵉʳ」\n╠═══════❀ˡᵉᵃ❀═══════╝\n" + \
                  "║┍♻️✍ ⚘ " + key + "ᴍᴇ\n" + \
                  "║┝♻️✍ ⚘ " + key + "ᴍɪᴅ「@」\n" + \
                  "║┝♻️✍ ⚘ " + key + "ɪɴғᴏ「@」\n" + \
                  "║┝♻️✍ ⚘ " + key + "ᴋɪᴄᴋᴇʀ ᴋɪᴄᴋ「@」\n" + \
                  "║┝♻️✍ ⚘ " + key + "ᴋɪss「@」\n" + \
                  "║┝♻️✍ ⚘ " + key + "ʙᴏᴛ ᴋɪᴄᴋ「@」\n" + \
                  "║┝♻️✍ ⚘ " + key + "ᴢ1-ᴢ5 ᴋɪᴄᴋ「@」\n" + \
                  "║┝♻️✍ ⚘ " + key + "ᴀᴅᴅ ᴄᴏɴ「@」\n" + \
                  "║┝♻️✍ ⚘ " + key + "ᴍʏʙᴏᴛ\n" + \
                  "║┝♻️✍ ⚘ " + key + "sᴛᴀᴛᴜs\n" + \
                  "║┝♻️✍ ⚘ " + key + "ᴀʙᴏᴜᴛ\n" + \
                  "║┝♻️✍ ⚘ " + key + "/ʀᴇʙᴏᴏᴛ\n" + \
                  "║┝♻️✍ ⚘ " + key + "ʀᴜɴᴛɪᴍᴇ\n" + \
                  "║┝♻️✍ ⚘ " + key + "ᴄʀᴇᴀᴛᴏʀ\n" + \
                  "║┝♻️✍ ⚘ " + key + "Sp\n" + \
                  "║┝♻️✍ ⚘ " + key + ".sp\n" + \
                  "║┝♻️✍ ⚘ " + key + "ᴡᴏʏ\n" + \
                  "║┝♻️✍ ⚘ " + key + "ᴘʀᴏ ɪɴ\n" + \
                  "║┝♻️✍ ⚘ " + key + "ᴘʀᴏ ᴏᴜᴛ\n" + \
                  "║┝♻️✍ ⚘ " + key + "ᴀᴊs sᴛᴀʏ\n" + \
                  "║┝♻️✍ ⚘ " + key + "αʟʟ 1јɵіɳ\n" + \
                  "║┝♻️✍ ⚘ " + key + "αʟʟ 1ʙƴє\n" + \
                  "║┝♻️✍ ⚘ " + key + "/αʟʟ1\n" + \
                  "║┝♻️✍ ⚘ " + key + "αɗɗ  сɵɳ「@」\n" + \
                  "║┝♻️✍ ⚘ " + key + "Leave「Namagrup」\n" + \
                  "║┝♻️✍ ⚘ " + key + "Ginfo\n" + \
                  "║┝♻️✍ ⚘ " + key + "ourl\n" + \
                  "║┝♻️✍ ⚘ " + key + "zourl\n" + \
                  "║┝♻️✍ ⚘ " + key + "curl\n" + \
                  "║┝♻️✍ ⚘ " + key + "zcurl\n" + \
                  "║┝♻️✍ ⚘ " + key + "all grup\n" + \
                  "║┝♻️✍ ⚘ " + key + "zall urlgrup\n" + \
                  "║┝♻️✍ ⚘ " + key + "Gruplist\n" + \
                  "║┝♻️✍ ⚘ " + key + "listbot\n" + \
                  "║┝♻️✍ ⚘ " + key + "Infogrup「angka」\n" + \
                  "║┝♻️✍ ⚘ " + key + "ɪɴғᴏᴍᴇᴍ「angka」\n" + \
                  "║┝♻️✍ ⚘ " + key + "ᴍʏʀᴇᴄʜᴀᴛ\n" + \
                  "║┝♻️✍ ⚘ " + key + "ʀᴇᴄʜᴀᴛ\n" + \
                  "║┝♻️✍ ⚘ " + key + "ʟᴜʀᴋ「on/off」\n" + \
                  "║┝♻️✍ ⚘ " + key + "ʟᴜʀᴋᴇʀs\n" + \
                  "║┝♻️✍ ⚘ " + key + "sɪᴅᴇʀ「on/off」\n" + \
                  "║┝♻️✍ ⚘ " + key + "ᴍᴇᴘɪᴄᴛ\n" + \
                  "║┝♻️✍ ⚘ " + key + "ᴜᴘᴘɪᴄᴛ\n" + \
                  "║┝♻️✍ ⚘ " + key + "ᴘɪᴄᴛɢʀᴜᴘ\n" + \
                  "║┝♻️✍ ⚘ " + key + "ʙᴄɢ:「Text」\n" + \
                  "║┝♻️✍ ⚘ " + key + "sᴇᴛᴋᴇʏ「New Key」\n" + \
                  "║┝♻️✍ ⚘ " + key + "ᴍʏᴋᴇʏ\n" + \
                  "║┝♻️✍ ⚘ " + key + "ʀᴇsᴇᴛᴋᴇʏ\n" + \
                  "║┝♻️✍ ⚘ " + key + "ɪᴅ ʟɪɴᴇ:「Id Line nya」\n" + \
                  "║┝♻️✍ ⚘ " + key + "sʜᴏʟᴀᴛ:「Nama Kota」\n" + \
                  "║┝♻️✍ ⚘ " + key + "ᴄᴜᴀᴄᴀ:「Nama Kota」\n" + \
                  "║┝♻️✍ ⚘ " + key + "ʟᴏᴋᴀsɪ:「Nama Kota」\n" + \
                  "║┝♻️✍ ⚘ " + key + "ᴍᴜsɪᴄ:「Judul Lagu」\n" + \
                  "║┝♻️✍ ⚘ " + key + "ʟɪʀɪᴋ:「Judul Lagu」\n" + \
                  "║┝♻️✍ ⚘ " + key + "ʏᴛ3:「Judul Lagu」\n" + \
                  "║┝♻️✍ ⚘ " + key + "ʏᴛ4:「Judul Video」\n" + \
                  "║┝♻️✍ ⚘ " + key + "ᴘʀᴏғɪʟᴇɪɢ:「Nama IG」\n" + \
                  "║┝♻️✍ ⚘ " + key + "ᴄᴇᴋᴅᴀᴛᴇ:「tgl-bln-thn」\n" + \
                  "║┝♻️✍ ⚘ " + key + "ᴍᴀx:「angka」\n" + \
                  "║┝♻️✍ ⚘ " + key + "sᴘᴀᴍᴛᴀɢ「@」\n" + \
                  "║┝♻️✍ ⚘ " + key + "sᴄᴀʟʟ:「jumlahnya」\n" + \
                  "║┕♻️✍ ⚘ " + key + "sᴄᴀʟʟ \n" + \
                  "╠═══════❀ˡᵉᵃ❀═══════╗\n║「 http://line.me/ti/p/~introvert82 」\n╚═══════❀ˡᵉᵃ❀═══════╝"
    return helpMessage

def helpset():
    key = Leakiller["keyCmd"]
    key = key.title()
    helpMessage1 = "╔═══════☣ℒℯα☣═══════╗\n║「ᵐᵉⁿᵘ ᵖʳᵒᵗᵉᶜᵗⁱᵒⁿ ᵖʸ3 ˡᵉᵃᵏⁱˡˡᵉʳ」\n╠═══════☣ℒℯα☣═══════╝\n" + \
                  "║┍♻️✍ ⚘ " + key + "Notag「on/off」\n" + \
                  "║┝♻️✍ ⚘ " + key + "Protect「on/off」\n" + \
                  "║┝♻️✍ ⚘ " + key + "Proqr「on/off」\n" + \
                  "║┝♻️✍ ⚘ " + key + "Projoin「on/off」\n" + \
                  "║┝♻️✍ ⚘ " + key + "Autokick「on/off」\n" + \
                  "║┝♻️✍ ⚘ " + key + "Procancel「on/off」\n" + \
                  "║┝♻️✍ ⚘ " + key + "Sticker「on/off」\n" + \
                  "║┝♻️✍ ⚘ " + key + "Respon「on/off」\n" + \
                  "║┝♻️✍ ⚘ " + key + "Contact「on/off」\n" + \
                  "║┝♻️✍ ⚘ " + key + "Autojoin「on/off」\n" + \
                  "║┝♻️✍ ⚘ " + key + "Autoadd「on/off」\n" + \
                  "║┝♻️✍ ⚘ " + key + "Welcome「on/off」\n" + \
                  "║┝♻️✍ ⚘ " + key + "Autoleave「on/off」\n" + \
                  "║┝♻️✍ ⚘ " + key + "Jticket「on/off」\n" + \
                  "║┝♻️✍ ⚘ " + key + "Inta「on/off」\n" + \
                  "║┝♻️✍ ⚘ " + key + "Bot:on\n" + \
                  "║┝♻️✍ ⚘ " + key + "Bot:dell\n" + \
                  "║┝♻️✍ ⚘ " + key + "addbot「@」\n" + \
                  "║┝♻️✍ ⚘ " + key + "delbot「@」\n" + \
                  "║┝♻️✍ ⚘ " + key + "Refresh\n" + \
                  "║┝♻️✍ ⚘ " + key + "mybot\n" + \
                  "║┝♻️✍ ⚘ " + key + "admin list\n" + \
                  "║┕♻️✍ ⚘ " + key + "prolist\n" + \
                  "╠═══════☣ℒℯα☣═══════╗\n║「 http://line.me/ti/p/~introvert82 」\n╚═══════☣ℒℯα☣═══════╝"
    return helpMessage1

def helpbot():
    key = Leakiller["keyCmd"]
    key = key.title()
    helpMessage2 = "═══════☣ℒℯα☣═══════╗\n║「ᵐᵉⁿᵘ ᵖʳᵒᵗᵉᶜᵗⁱᵒⁿ ᵖʸ3 ˡᵉᵃᵏⁱˡˡᵉʳ」\n╠═══════☣ℒℯα☣═══════╝\n" + \
                  "║┍ℒℯα✍ ⚘ " + key + "Cban\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Ban:on\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Unban:on\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Ban「@」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Unban「@」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Tban「@」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Utban「@」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Tban:on\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Utban:on\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Banlist\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Tbanlist\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Refresh\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "cekmsg\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "sider:「Text」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "spam:「Text」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "add:「Text」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "tag:「Text」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "welcome:「Text」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "zname:「Nama」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "z1cn:「Nama」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "z2cn:「Nama」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "z3cn:「Nama」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "z4cn:「Nama」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "z5cn:「Nama」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Kicker cn:「Nama」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Kickerpict「K fhoto」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "z1pict「Kirim fhoto」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "z2pict「Kirim fhoto」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "z3pict「Kirim fhoto」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "z4pict「Kirim fhoto」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "z5pict「Kirim fhoto」\n" + \
                  "║┝ℒℯα✍ ⚘ " + key + "Gift:「Mid」「Jumlah」\n" + \
                  "║┕ℒℯα✍ ⚘ " + key + "Spam:「Mid」「Jumlah」\n" + \
                  "╠═══════☣ℒℯα☣═══════╗\n║「 http://line.me/ti/p/~introvert82 」\n╚═══════☣ℒℯα☣═══════╝"
    return helpMessage2

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 11:
            if op.param2 in wait["blacklist"]:
                if cl.getGroup(op.param1).preventedJoinByTicket == False:
                    if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                        random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        cl.updateGroup(G)
                    else:pass
        if op.type == 13:
            if op.param2 in wait["blacklist"]:
                if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                    try:
                        ka.cancelGroupInvitation(op.param1,[op.param3])
                    except:
                        try:
                            kb.cancelGroupInvitation(op.param1,[op.param3])
                        except:
                            try:
                                kc.cancelGroupInvitation(op.param1,[op.param3])
                            except:
                                try:
                                    kd.cancelGroupInvitation(op.param1,[op.param3])
                                except:
                                    try:
                                        ke.cancelGroupInvitation(op.param1,[op.param3])
                                    except:
                                        pass
                else:pass
            if op.param3 in wait["blacklist"]:
                if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                    try:
                        ke.cancelGroupInvitation(op.param1,[op.param3])
                    except:
                        try:
                            kd.cancelGroupInvitation(op.param1,[op.param3])
                        except:
                            try:
                                kc.cancelGroupInvitation(op.param1,[op.param3])
                            except:
                                try:
                                    kb.cancelGroupInvitation(op.param1,[op.param3])
                                except:
                                    try:
                                        ka.cancelGroupInvitation(op.param1,[op.param3])
                                    except:
                                        pass
                else:pass
            if op.param3 in wait["blacklist"]:
                if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                    try:
                        ka.cancelGroupInvitation(op.param1,[op.param3])
                        ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kb.cancelGroupInvitation(op.param1,[op.param3])
                            kb.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.cancelGroupInvitation(op.param1,[op.param3])
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kd.cancelGroupInvitation(op.param1,[op.param3])
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ke.cancelGroupInvitation(op.param1,[op.param3])
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                else:pass
        if op.type == 15:
            if op.param2 in Alfiah:
                try:
                    random.choice(Amin).inviteIntoGroup(op.param1,[Smid])
                except:
                    try:
                        cl.inviteIntoGroup(op.param1,[Smid])
                    except:
                        pass
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kd.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ka.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                else:pass
        if op.type == 32:
            if op.param2 in wait["blacklist"]:
                if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                else:pass
        if op.type == 32:
            if op.param3 in Introvert or op.param3 in Leakiller["Lea"] or op.param3 in Leakiller["admin"]:
                if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.findAndAddContactsByMid(op.param3)
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            kb.findAndAddContactsByMid(op.param3)
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kc.findAndAddContactsByMid(op.param3)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kd.findAndAddContactsByMid(op.param3)
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        ke.findAndAddContactsByMid(op.param3)
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            cl.findAndAddContactsByMid(op.param3)
                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            pass
                else:pass
        if op.type == 19:
            if mid in op.param3:
                if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        cl.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            random.choice(Amin).inviteIntoGroup(op.param1,[op.param3])
                                            random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                                            cl.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                    try:
                        k1.acceptGroupInvitation(op.param1)
                        x = k1.getGroup(op.param1)
                        x.preventedJoinByTicket = False
                        k1.updateGroup(x)
                        Ti = k1.reissueGroupTicket(op.param1)
                        time.sleep(0.001)
                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                        ka.acceptGroupInvitationByTicket(op.param1,Ti)
                        kb.acceptGroupInvitationByTicket(op.param1,Ti)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        kd.acceptGroupInvitationByTicket(op.param1,Ti)
                        ke.acceptGroupInvitationByTicket(op.param1,Ti)
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.leaveGroup(op.param1)
                        x = cl.getGroup(op.param1)
                        x.preventedJoinByTicket = True
                        cl.updateGroup(x)
                    except:
                        try:
                            ke.kickoutFromGroup(op.param1,[op.param2])
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kd.kickoutFromGroup(op.param1,[op.param2])
                                kd.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        cl.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ka.inviteIntoGroup(op.param1,[op.param3])
                                            ka.kickoutFromGroup(op.param1,[op.param2])
                                            cl.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                random.choice(Amin).inviteIntoGroup(op.param1,[op.param3])
                                                random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                                                cl.acceptGroupInvitation(op.param1)
                                            except:
                                                   G = ke.getGroup(op.param1)
                                                   G.preventedJoinByTicket = False
                                                   ke.updateGroup(G)
                                                   Ticket = ke.reissueGroupTicket(op.param1)
                                                   ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                   kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                   kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                   kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                   cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                   random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                else:pass
                return
            if Amid in op.param3:
                if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        ka.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            ka.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kd.inviteIntoGroup(op.param1,[op.param3])
                                kd.kickoutFromGroup(op.param1,[op.param2])
                                ka.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ke.nviteIntoGroup(op.param1,[op.param3])
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    ke.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        ka.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            random.choice(Aakun).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Aakun).inviteIntoGroup(op.param1,[op.param3])
                                            ka.acceptGroupInvitation(op.param1)
                                        except:
                                               G = ke.getGroup(op.param1)
                                               G.preventedJoinByTicket = False
                                               ke.updateGroup(G)
                                               Ticket = ke.reissueGroupTicket(op.param1)
                                               ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                else:pass
                return
            if Bmid in op.param3:
                if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kb.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kd.inviteIntoGroup(op.param1,[op.param3])
                            kd.kickoutFromGroup(op.param1,[op.param2])
                            kb.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                ke.kickoutFromGroup(op.param1,[op.param2])
                                kb.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ka.inviteIntoGroup(op.param1,[op.param3])
                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                    kb.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        kb.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            random.choice(Bakun).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Bakun).inviteIntoGroup(op.param1,[op.param3])
                                            kb.acceptGroupInvitation(op.param1)
                                        except:
                                               G = kd.getGroup(op.param1)
                                               G.preventedJoinByTicket = False
                                               kd.updateGroup(G)
                                               Ticket = kd.reissueGroupTicket(op.param1)
                                               ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                else:pass
                return
            if Cmid in op.param3:
                if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        kd.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ke.kickoutFromGroup(op.param1,[op.param2])
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ka.kickoutFromGroup(op.param1,[op.param2])
                                ka.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            random.choice(Cakun).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Cakun).inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
                                        except:
                                               G = ka.getGroup(op.param1)
                                               G.preventedJoinByTicket = False
                                               ka.updateGroup(G)
                                               Ticket = ka.reissueGroupTicket(op.param1)
                                               ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                else:pass
                return
            if Dmid in op.param3:
                if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        kd.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.inviteIntoGroup(op.param1,[op.param3])
                            kd.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                                kd.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    kd.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        kd.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            random.choice(Dakun).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Dakun).inviteIntoGroup(op.param1,[op.param3])
                                            kd.acceptGroupInvitation(op.param1)
                                        except:
                                               G = kb.getGroup(op.param1)
                                               G.preventedJoinByTicket = False
                                               kb.updateGroup(G)
                                               Ticket = kb.reissueGroupTicket(op.param1)
                                               ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                else:pass
                return
            if Emid in op.param3:
                if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,[op.param3])
                        ke.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                            ke.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                ke.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                    ke.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        ke.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            random.choice(Eakun).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Eakun).inviteIntoGroup(op.param1,[op.param3])
                                            ke.acceptGroupInvitation(op.param1)
                                        except:
                                               G = kc.getGroup(op.param1)
                                               G.preventedJoinByTicket = False
                                               kc.updateGroup(G)
                                               Ticket = kc.reissueGroupTicket(op.param1)
                                               ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                else:pass
                return
            if Smid in op.param3:
                if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Amin).inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            pass
                else:pass
                return
            if op.param3 in Zie:
                if op.param2 not in Introvert:
                    wait["blacklist"][op.param2] = True
                    try:
                        k1.acceptGroupInvitation(op.param1)
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        x = cl.getGroup(op.param1)
                        x.preventedJoinByTicket = False
                        cl.updateGroup(x)
                        Ti = cl.reissueGroupTicket(op.param1)
                        time.sleep(0.001)
                        ka.acceptGroupInvitationByTicket(op.param1,Ti)
                        kb.acceptGroupInvitationByTicket(op.param1,Ti)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        kd.acceptGroupInvitationByTicket(op.param1,Ti)
                        ke.acceptGroupInvitationByTicket(op.param1,Ti)
                        k1.leaveGroup(op.param1)
                        x = cl.getGroup(op.param1)
                        x.preventedJoinByTicket = True
                        cl.updateGroup(x)
                    except:
                        pass
            if op.type == 19:
                if op.param3 in Introvert:
                    if op.param2 not in Introvert:
                        wait["blacklist"][op.param2] = True
                        try:
                            cl.findAndAddContactsByMid(op.param3)
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            x = cl.getGroup(op.param1)
                            x.preventedJoinByTicket = False
                            cl.updateGroup(x)
                            Ti = cl.reissueGroupTicket(op.param1)
                            time.sleep(0.001)
                            ka.acceptGroupInvitationByTicket(op.param1,Ti)
                            kb.acceptGroupInvitationByTicket(op.param1,Ti)
                            kc.acceptGroupInvitationByTicket(op.param1,Ti)
                            kd.acceptGroupInvitationByTicket(op.param1,Ti)
                            ke.acceptGroupInvitationByTicket(op.param1,Ti)
                            k1.leaveGroup(op.param1)
                            x = cl.getGroup(op.param1)
                            x.preventedJoinByTicket = True
                            cl.updateGroup(x)
                        except:
                            try:
                                kb.findAndAddContactsByMid(op.param3)
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kc.findAndAddContactsByMid(op.param3)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        kd.findAndAddContactsByMid(op.param3)
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            ke.findAndAddContactsByMid(op.param3)
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                ka.findAndAddContactsByMid(op.param3)
                                                ka.kickoutFromGroup(op.param1,[op.param2])
                                                ka.inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                try:
                                                    cl.findAndAddContactsByMid(op.param3)
                                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                                except:
                                                    try:
                                                        k1.findAndAddContactsByMid(op.param3)
                                                        k1.kickoutFromGroup(op.param1,[op.param2])
                                                        k1.inviteIntoGroup(op.param1,[op.param3])
                                                    except:
                                                        try:
                                                           random.choice(Amin).findAndAddContactsByMid(op.param3)
                                                           random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                                                           random.choice(Amin).inviteIntoGroup(op.param1,[op.param3])
                                                        except:
                                                            pass
                    else:pass
                    return
                if op.param3 in Leakiller["Bots"]:
                    if op.param2 not in Introvert or op.param2 not in Leakiller["Lea"] or op.param2 not in Leakiller["admin"]:
                        wait["blacklist"][op.param2] = True
                        try:
                            ka.findAndAddContactsByMid(op.param3)
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kb.findAndAddContactsByMid(op.param3)
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kc.findAndAddContactsByMid(op.param3)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        kd.findAndAddContactsByMid(op.param3)
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            ke.findAndAddContactsByMid(op.param3)
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                random.choice(Bismillah).findAndAddContactsByMid(op.param3)
                                                random.choice(Bismillah).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(Bismillah).inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                pass
                    else:pass
                    return
                if op.param3 in Leakiller["admin"]:
                    if op.param2 not in Introvert or op.param2 not in Leakiller["Lea"] or op.param2 not in Leakiller["admin"]:
                        wait["blacklist"][op.param2] = True
                        try:
                            ka.findAndAddContactsByMid(op.param3)
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kb.findAndAddContactsByMid(op.param3)
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kc.findAndAddContactsByMid(op.param3)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        kd.findAndAddContactsByMid(op.param3)
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            ke.findAndAddContactsByMid(op.param3)
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                random.choice(Bismillah).findAndAddContactsByMid(op.param3)
                                                random.choice(Bismillah).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(Bismillah).inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                pass
                    else:pass
                    return
        if op.type == 0:
            return
        if op.type == 5:
            if Leakiller["autoAdd"] == True:
                if op.param2 not in Introvert:
                    cl.findAndAddContactsByMid(op.param1)
                    if (Leakiller["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, Leakiller["message"])
        if op.type == 11:
            if op.param1 in Leakiller["proqr"]:
                if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        wait["blacklist"][op.param2] = True
                        random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                        Z = random.choice(Bismillah).getGroup(op.param1)
                        Z.preventedJoinByTicket = True
                        random.choice(Bismillah).updateGroup(Z)
                else:
                    pass
        if op.type == 11:
            if op.param1 in Leakiller["intaPoint"]:
                if op.param2 in Introvert and op.param2 in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                    pass
                else:
                    X = cl.getGroup(op.param1)
                    if X.preventedJoinByTicket == True:
                        pass
                    else:
                        cl.updateGroup(X)
                        invsend = 0
                        Ti = cl.reissueGroupTicket(op.param1)
                        ka.acceptGroupInvitationByTicket(op.param1,Ti)
                        kb.acceptGroupInvitationByTicket(op.param1,Ti)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        kd.acceptGroupInvitationByTicket(op.param1,Ti)
                        ke.acceptGroupInvitationByTicket(op.param1,Ti)
        if op.type == 13:
            if mid in op.param3:
                if Leakiller["autoJoin"] == True:
                    if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                        cl.acceptGroupInvitation(op.param1)
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
            if Amid in op.param3:
                if Leakiller["autoJoin"] == True:
                    if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                        ka.acceptGroupInvitation(op.param1)
                        ka.leaveGroup(op.param1)
                    else:
                        ka.acceptGroupInvitation(op.param1)
            if Bmid in op.param3:
                if Leakiller["autoJoin"] == True:
                    if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                        kb.acceptGroupInvitation(op.param1)
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
            if Cmid in op.param3:
                if Leakiller["autoJoin"] == True:
                    if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                        kc.acceptGroupInvitation(op.param1)
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
            if Dmid in op.param3:
                if Leakiller["autoJoin"] == True:
                    if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                        kd.acceptGroupInvitation(op.param1)
                        kd.leaveGroup(op.param1)
                    else:
                        kd.acceptGroupInvitation(op.param1)
            if Emid in op.param3:
                if Leakiller["autoJoin"] == True:
                    if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                        ke.acceptGroupInvitation(op.param1)
                        ke.leaveGroup(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
        if op.type == 13:
            if op.param1 in Leakiller["proInvite"]:
                if op.param2 in Introvert or op.param2 in Leakiller["Lea"] or op.param2 in Leakiller["admin"]:
                    pass
                else:
                    try:
                        if op.param3 in Introvert or op.param3 in Leakiller["Lea"] or op.param3 in Leakiller["admin"]:
                            pass
                        else:
                           if op.param2 not in Introvert or op.param2 not in Leakiller["Lea"] or op.param2 not in Leakiller["admin"]:
                                wait["blacklist"][op.param2] = True
                                random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                                anu = cl.getCompactGroup(op.param1)
                                if anu.invitee is not None:
                                    pipo = [a.mid for a in anu.invitee]
                                    for target in pipo:
                                        if target in op.param3 and target not in Introvert and target not in Leakiller["Lea"] and target not in Leakiller["admin"]:
                                            wait["blacklist"][target] = True
                                            random.choice(Bismillah).cancelGroupInvitation(op.param1,[target])
                           else:pass
                    except:
                        pass
        if op.type == 15:
            if op.param1 in Leakiller["leaveMsg"]:
                if op.param2 not in Introvert and op.param2 not in Leakiller["admin"] and op.param2 not in Leakiller["Lea"]:
                    return
                else:
                    cl.sendMessage(op.param1, Leakiller["leftmsg"])
        if op.type == 17:
            if op.param1 in Leakiller["welcome"]:
                if op.param2 in Introvert or op.param2 in Leakiller["Lea"] or op.param2 in Leakiller["admin"]:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)
        if op.type == 19:
            if op.param1 in Leakiller["proKick"]:
                if op.param2 in Introvert or op.param2 in Leakiller["Lea"] or op.param2 in Leakiller["admin"]:
                    pass
                else:
                    try:
                        if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                            wait["blacklist"][op.param2] = True
                            if op.param3 not in wait["blacklist"]:
                                try:
                                    ka.findAndAddContactsByMid(op.param3)
                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                    ka.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        kb.findAndAddContactsByMid(op.param3)
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            kc.findAndAddContactsByMid(op.param3)
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                kd.findAndAddContactsByMid(op.param3)
                                                kd.kickoutFromGroup(op.param1,[op.param2])
                                                kd.inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                try:
                                                    ke.findAndAddContactsByMid(op.param3)
                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                except:
                                                    pass
                            else:pass
                        else:pass
                    except:
                        pass
        if op.type == 32:
            if op.param1 in Leakiller["proCancel"]:
                if op.param2 in Introvert or op.param2 in Leakiller["Lea"] or op.param2 in Leakiller["admin"]:
                    pass
                else:
                    try:
                        if op.param2 not in Introvert and op.param2 not in Leakiller["Lea"] and op.param2 not in Leakiller["admin"]:
                            wait["blacklist"][op.param2] = True
                            if op.param3 not in wait["blacklist"]:
                                try:
                                    ka.findAndAddContactsByMid(op.param3)
                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                    ka.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        kb.findAndAddContactsByMid(op.param3)
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            kc.findAndAddContactsByMid(op.param3)
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                kd.findAndAddContactsByMid(op.param3)
                                                kd.kickoutFromGroup(op.param1,[op.param2])
                                                kd.inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                try:
                                                    ke.findAndAddContactsByMid(op.param3)
                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                except:
                                                    pass
                            else:pass
                        else:pass
                    except:
                        pass
        if op.type == 55:
            try:
                if op.param1 in Leakiller["readPoint"]:
                   if op.param2 in Leakiller["readMember"][op.param1]:
                       pass
                   else:
                       Leakiller["readMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass
        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
        if op.type == 65:
            if Leakiller["Unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)
        if op.type == 65:
            if Leakiller["Unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != cl.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
                if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n• Sticker ID : {}".format(stk_id)
                   ret_ += "\n• Sticker Version : {}".format(stk_ver)
                   ret_ += "\n• Sticker Package : {}".format(pkg_id)
                   ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 and msg.toType == 2:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                    names = re.findall(r'@(\w+)', text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    lists = []
                    for mention in mentionees:
                        if mid in mention['M']:
                            if Leakiller["detectMention"] == True:
                                ca = cl.getContact(sender)
                                cl.sendMessage(to, "halo...☛❲ " + ca.displayName + "❳☚ ")
                                cl.sendMessage(to, Leakiller["msgTag"])
                                cl.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}" .format(str(ca.pictureStatus)))
                            else:
                                pass
            if msg.contentType == 13:
              if Leakiller["contact"] == True:
                 msg.contentType = 0
                 cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                 if 'displayName' in msg.contentMetadata:
                     contact = cl.getContact(msg.contentMetadata["mid"])
                     path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                     image = 'http://dl.profile.line.naver.jp'+path
                     cl.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                     cl.sendImageWithURL(msg.to, image)
            if msg.contentType == 16:
                if Leakiller["LikeOn"] == True:
                    url = msg.contentMetadata["postEndUrl"]
                    daftarLike = [1001,1002,1003,1004,1005,1006]
                    likeType = random.choice(daftarLike)
                    cl.likePost(url[25:58], url[66:], likeType)
                    cl.createComment(url[25:58], url[66:], Leakiller["comment"])
            if msg.contentType == 16:
              if Leakiller["checkPost"] == True:
                  try:
                      ret_ = "╔════[ Post Detail ]"
                      if msg.contentMetadata["serviceType"] == "GB":
                          contact = cl.getContact(sender)
                          auth = "\n╠☛ Author : {}".format(str(contact.displayName))
                      else:
                          auth = "\n╠☛ Author : {}".format(str(msg.contentMetadata["serviceName"]))
                      purl = "\n╠☛ Url : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                      ret_ += auth
                      ret_ += purl
                      if "mediaOid" in msg.contentMetadata:
                          object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                          if msg.contentMetadata["mediaType"] == "V":
                              if msg.contentMetadata["serviceType"] == "GB":
                                  ourl = "\n╠☛ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                  murl = "\n╠☛ Url Media : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                              else:
                                  ourl = "\n╠☛ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                  murl = "\n╠☛ Url Media : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                              ret_ += murl
                          else:
                              if msg.contentMetadata["serviceType"] == "GB":
                                  ourl = "\n╠☛ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                              else:
                                  ourl = "\n╠☛ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                          ret_ += ourl
                      if "stickerId" in msg.contentMetadata:
                          stck = "\n╠☛ Sticker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                          ret_ += stck
                      if "text" in msg.contentMetadata:
                          text = "\n╠☛ Note : {}".format(str(msg.contentMetadata["text"]))
                          ret_ += text
                      ret_ += "\n╚══[ ✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴ ]"
                      cl.sendMessage(to, str(ret_))
                  except:
                      cl.sendMessage(msg.to,"Invalid Post")
        if op.type == 25 or op.type == 26:
          try:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if Leakiller["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"╔══════════════\n╠☛❲Check Sticker❳\n╠☛ STKID : " + msg.contentMetadata["STKID"] +"\n╠☛ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n╠☛ STKVER : " + msg.contentMetadata["STKVER"] + "\n╠☛ " + "line://shop/detail/" + msg.contentMetadata["STKPKGID"] +"\n╚══════════════")
               if msg.contentType == 13:
                 if Leakiller["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"╔══════════════\n╠☛ Nama : " + msg.contentMetadata["displayName"] + "\n╠☛ Mid : " + msg.contentMetadata["mid"] + "\n╠☛ Status : " + contact.statusMessage + "\n╠☛ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n╚══════════════")
                        cl.sendImageWithURL(msg.to, image)
               if msg.contentType == 13:
                 if msg._from in Zie:
                  if Leakiller["abots"] == True:
                    if msg.contentMetadata["mid"] in Leakiller["Lea"]:
                        cl.sendMessage(msg.to,"was bot friend")
                    else:
                        Leakiller["Lea"][msg.contentMetadata["mid"]] = True
                        cl.sendMessage(msg.to,"succes add bots")
                 if Leakiller["dbots"] == True:
                    if msg.contentMetadata["mid"] in Leakiller["Lea"]:
                        del Leakiller["Lea"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Succes remove bots")
                    else:
                        cl.sendMessage(msg.to,"Contact not in list bots")
                 if msg._from in Zie:
                  if Leakiller["addadmin"] == True:
                    if msg.contentMetadata["mid"] in Leakiller["admin"]:
                        cl.sendMessage(msg.to,"was admin")
                    else:
                        Leakiller["admin"][msg.contentMetadata["mid"]] = True
                        cl.sendMessage(msg.to,"succes add admin")
                 if Leakiller["deladmin"] == True:
                    if msg.contentMetadata["mid"] in Leakiller["admin"]:
                        del Leakiller["admin"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Succes remove admin")
                    else:
                        cl.sendMessage(msg.to,"Contact not in list admin")
                 if msg._from in Zie:
                  if Leakiller["ablacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"was blacklist")
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        cl.sendMessage(msg.to,"succes add in blacklist")
                 if Leakiller["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Succes remove blacklist")
                    else:
                        cl.sendMessage(msg.to,"Contact not in blacklist")
               if msg.toType == 2:
                 if msg._from in Zie:
                   if Leakiller["gPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     Leakiller["gPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Succes")
               if msg.contentType == 1:
                 if msg._from in Zie:
                   if Leakiller["DPicture"] == True:
                     path1 = ka.downloadObjectMsg(msg_id)
                     path2 = kb.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     path4 = kd.downloadObjectMsg(msg_id)
                     path5 = ke.downloadObjectMsg(msg_id)
                     Leakiller["DPicture"] = False
                     ka.updateProfilePicture(path1)
                     ka.sendMessage(msg.to, "Succes change pic")
                     kb.updateProfilePicture(path2)
                     kb.sendMessage(msg.to, "Succes change pic")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Succes change pic")
                     kd.updateProfilePicture(path4)
                     kd.sendMessage(msg.to, "Succes change pic")
                     ke.updateProfilePicture(path5)
                     ke.sendMessage(msg.to, "Succes change pic")
               if msg.contentType == 1:
                 if msg._from in Zie:
                   if mid in Leakiller["cPicture"]:
                     path6 = cl.downloadObjectMsg(msg_id)
                     del Leakiller["cPicture"][mid]
                     cl.updateProfilePicture(path6)
                     cl.sendMessage(msg.to,"succes update display picture")
                   if Amid in Leakiller["cPicture"]:
                     path1 = ka.downloadObjectMsg(msg_id)
                     del Leakiller["cPicture"][Amid]
                     ka.updateProfilePicture(path1)
                     ka.sendMessage(msg.to,"succes update display picture")
                   if Bmid in Leakiller["cPicture"]:
                     path2 = kb.downloadObjectMsg(msg_id)
                     del Leakiller["cPicture"][Bmid]
                     kb.updateProfilePicture(path2)
                     kb.sendMessage(msg.to,"succes update display picture")
                   if Cmid in Leakiller["cPicture"]:
                     path3 = kc.downloadObjectMsg(msg_id)
                     del Leakiller["cPicture"][Cmid]
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to,"succes update display picture")
                   if Dmid in Leakiller["cPicture"]:
                     path4 = kd.downloadObjectMsg(msg_id)
                     del Leakiller["cPicture"][Dmid]
                     kd.updateProfilePicture(path4)
                     kd.sendMessage(msg.to,"succes update display picture")
                   if Emid in Leakiller["cPicture"]:
                     path5 = ke.downloadObjectMsg(msg_id)
                     del Leakiller["cPicture"][Emid]
                     ke.updateProfilePicture(path5)
                     ke.sendMessage(msg.to,"succes update display picture")
                   if Smid in Leakiller["cPicture"]:
                     path7 = k1.downloadObjectMsg(msg_id)
                     del Leakiller["cPicture"][Smid]
                     k1.updateProfilePicture(path7)
                     k1.sendMessage(msg.to,"succes update display picture")
               if msg.contentType == 0:
                    if Leakiller["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "menu":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               helpMessage = help()
                               cl.sendMessage(to,"╔"+str(helpMessage))

                        if cmd == "menubot":
                            if msg._from in Zie:
                               helpMessage = help()
                               ka.sendMessage(to,"╔"+str(helpMessage))

                        if cmd == "menu1":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               helpMessage1 = helpset()
                               cl.sendMessage(to,str(helpMessage1))

                        if cmd == "menubot1":
                            if msg._from in Zie:
                               helpMessage1 = helpset()
                               ka.sendMessage(to,"╔"+str(helpMessage1))

                        if cmd == "on":
                            if msg._from in Zie:
                                Leakiller["selfbot"] = True
                                cl.sendMessage(msg.to, "✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴diaktifkan")

                        elif cmd == "off":
                            if msg._from in Zie:
                                Leakiller["selfbot"] = False
                                cl.sendMessage(msg.to, "✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴ dimatikan")

                        elif cmd == "menu2":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               helpMessage2 = helpbot()
                               cl.sendMessage(to,"╔"+str(helpMessage2))

                        elif cmd == "menubot2":
                            if msg._from in Zie:
                               helpMessage2 = helpbot()
                               ka.sendMessage(to,"╔"+str(helpMessage2))

                        elif cmd == "grupset":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                md = ""
                                if msg.to in Leakiller["proqr"]: md+="􁤁􀇜╠☛ PʀᴏQr : ✓\n"
                                else: md+="􀔃􀆓╠☛ PʀᴏQr: ✘\n"
                                if msg.to in Leakiller["proKick"]: md+="􁤁􀇜╠☛ Auto ᴋɪᴄᴋ : ✓\n"
                                else: md+="􀔃􀆓╠☛ Auto ᴋɪᴄᴋ : ✘\n"
                                if msg.to in Leakiller["proCancel"]: md+="􁤁􀇜╠☛ Pʀᴏᴄᴀɴᴄᴇʟ : ✓\n"
                                else: md+="􀔃􀆓╠☛ PʀᴏᴄᴀɴᴄᴇL : ✘\n"
                                if msg.to in Leakiller["proInvite"]: md+="􁤁􀇜╠☛ PʀᴏInvite : ✓\n"
                                else: md+="􀔃􀆓╠☛ PʀᴏInvite : ✘\n"
                                if msg.to in Leakiller["intaPoint"]: md+="􁤁􀇜╠☛ IntaPoint : ✓\n"
                                else: md+="􀔃􀆓╠☛ IntaPoint : ✘\n"
                                if msg.to in Leakiller["welcome"]: md+="􁤁􀇜╠☛ Welcome Msg : ✓\n"
                                else: md+="􀔃􀆓╠☛ Welcome Msg : ✘\n"
                                if msg.to in Leakiller["leaveMsg"]: md+="􁤁􀇜╠☛ Leave Msg : ✓\n"
                                else: md+="􀔃􀆓╠☛ Leave Msg : ✘\n"
                                cl.sendMessage(msg.to, "╔══❲ Sett Group ❳══\n"+ md +"╚══════════════")

                        elif text.lower() == "status":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                md = ""
                                if Leakiller["autoJoin"] == True: md+="􁤁􀇜╠☛ AᴜᴛᴏJᴏɪɴ : ✓\n"
                                else: md+="􀔃􀆓╠☛ AutoJoin : ✘\n"
                                if Leakiller["sticker"] == True: md+="􁤁􀇜╠☛ Stickeʀ : ✓\n"
                                else: md+="􀔃􀆓╠☛ Stickeʀ ✘\n"
                                if Leakiller["contact"] == True: md+="􁤁􀇜╠☛ Cᴏntacᴛ : ✓\n"
                                else: md+="􀔃􀆓╠☛ Cᴏntacᴛ : ✘ \n"
                                if Leakiller["detectMention"] == True: md+="􁤁􀇜╠☛ Mention : ✓\n"
                                else: md+="􀔃􀆓╠☛ Mention : ✘\n"
                                if Leakiller["autoAdd"] == True: md+="􁤁􀇜╠☛ Msg ᴀᴅᴅ : ✓\n"
                                else: md+="􀔃􀆓╠☛ Msg ᴀᴅᴅ : ✘\n"
                                userid = "https://line.me/ti/p/~" + cl.profile.userid
                                cl.sendMessage(msg.to, "╔══❲ Status Group ❳══\n"+ md +"╚══════════════")

                        elif cmd == "me" or text.lower() == 'me':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               cl.sendMentionFooter(to, '「My Name」\n', sender, "https://line.me/ti/p/Qs-GbY_YPG", "http://dl.profile.line-cdn.net/"+cl.getContact(sender).pictureStatus, cl.getContact(sender).displayName);cl.sendMessage(to, cl.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+cl.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/ankrust86', 'type': 'mt', 'subText': "✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴", 'a-installUrl': 'https://line.me/ti/p/~calon_almarhum99', 'a-installUrl': ' https://line.me/ti/p/ankrust86', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/ankrust86', 'i-linkUri': 'https://line.me/ti/p/ankrust86', 'id': 'mt000000000a6b79f9', 'text': '✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴', 'linkUri': 'https://line.me/ti/p/ankrust86'}, contentType=19)

                        elif cmd == "reject":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)
                                  cl.sendMessage(to, "Berhasil tolak sebanyak {} undangan grup".format(str(len(ginvited))))
                              else:
                                  cl.sendMessage(to, "Tidak ada undangan yang tertunda")

                        elif cmd == 'bot:room':
                            a = []
                            b = cl.getGroup(to)
                            lss = cl.refreshContacts()
                            for i in b.members:
                              if i.mid not in mid:
                                 a.append(i.mid)
                                 if i.mid not in lss:
                                    cl.findAndAddContactsByMid(i.mid)
                                 time.sleep(3)
                            if a == []:
                               cl.sendMessage(to,"Nothing to added.")
                            else:cl.sendMessage(to,'Add whitelist')

                        elif cmd == 'bot1:room':
                            a = []
                            b = ka.getGroup(to)
                            lss = ka.refreshContacts()
                            for i in b.members:
                              if i.mid not in mid:
                                 a.append(i.mid)
                                 if i.mid not in lss:
                                    ka.findAndAddContactsByMid(i.mid)
                                 time.sleep(3)
                            if a == []:
                               ka.sendMessage(to,"Nothing to added.")
                            else:ka.sendMessage(to,'Add whitelist')

                        elif cmd == 'bot2:room':
                            a = []
                            b = kb.getGroup(to)
                            lss = kb.refreshContacts()
                            for i in b.members:
                              if i.mid not in mid:
                                 a.append(i.mid)
                                 if i.mid not in lss:
                                    kb.findAndAddContactsByMid(i.mid)
                                 time.sleep(3)
                            if a == []:
                               kb.sendMessage(to,"Nothing to added.")
                            else:kb.sendMessage(to,'Add whitelist')

                        elif cmd == 'bot3:room':
                            a = []
                            b = kc.getGroup(to)
                            lss = kc.refreshContacts()
                            for i in b.members:
                              if i.mid not in mid:
                                 a.append(i.mid)
                                 if i.mid not in lss:
                                    kc.findAndAddContactsByMid(i.mid)
                                 time.sleep(3)
                            if a == []:
                               kc.sendMessage(to,"Nothing to added.")
                            else:kc.sendMessage(to,'Add whitelist')

                        elif cmd == 'bot4:room':
                            a = []
                            b = kd.getGroup(to)
                            lss = kd.refreshContacts()
                            for i in b.members:
                              if i.mid not in mid:
                                 a.append(i.mid)
                                 if i.mid not in lss:
                                    kd.findAndAddContactsByMid(i.mid)
                                 time.sleep(3)
                            if a == []:
                               kd.sendMessage(to,"Nothing to added.")
                            else:kd.sendMessage(to,'Add whitelist')

                        elif cmd == 'bot5:room':
                            a = []
                            b = ke.getGroup(to)
                            lss = ke.refreshContacts()
                            for i in b.members:
                              if i.mid not in mid:
                                 a.append(i.mid)
                                 if i.mid not in lss:
                                    ke.findAndAddContactsByMid(i.mid)
                                 time.sleep(3)
                            if a == []:
                               ke.sendMessage(to,"Nothing to added.")
                            else:ke.sendMessage(to,'Add whitelist')

                        elif cmd == 'kicker:room':
                            a = []
                            b = k1.getGroup(to)
                            lss = k1.refreshContacts()
                            for i in b.members:
                              if i.mid not in mid:
                                 a.append(i.mid)
                                 if i.mid not in lss:
                                    k1.findAndAddContactsByMid(i.mid)
                                 time.sleep(3)
                            if a == []:
                               k1.sendMessage(to,"Nothing to added.")
                            else:k1.sendMessage(to,'Add whitelist')

                        elif cmd.startswith("smuleaudio "):
                          if msg._from in Zie:
                            try:
                                sep = msg.text.split(" ")
                                dancoeg = msg.text.replace(sep[0] + " ","")
                                r = requests.get("https://smule.com/FFV_Zie_RockStar?link={}".format(dancoeg))
                                data = r.text
                                data = json.loads(data)
                                cl.sendImageWithURL(to, str(data["result"][0]["thumb"]))
                                cl.sendAudioWithURL(to, str(data["result"][0]["video"]))
                            except:
                                sendMention(to, sender, "「", "」\nWaiting Progres Audio 🔊")
                                cl.sendAudioWithURL(to, str(data["result"][0]["video"]))

                        elif ("Gn " in msg.text):
                          if msg._from in Zie:
                              X = cl.getGroup(msg.to)
                              X.name = msg.text.replace("Gn ","")
                              cl.updateGroup(X)

                        elif ("Mid " in msg.text):
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                   names = re.findall(r'@(\w+)', text)
                                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                   mentionees = mention['MENTIONEES']
                                   lists = []
                                   for mention in mentionees:
                                       if mention["M"] not in lists:
                                           lists.append(mention["M"])
                                   ret_ = ""
                                   for ls in lists:
                                       ret_ += "{}".format(str(ls))
                                   cl.sendMessage(to, str(ret_),{'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+'M', 'AGENT_NAME': 'Mention', 'AGENT_LINK': 'http://line.me/ti/p/~{}'.format(cl.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + cl.getProfile().picturePath})

                        elif cmd == "mymid":
                               cl.sendMessage(to, "Mid:\n{}".format(sender))

                        elif ("Info " in msg.text):
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "☛ Nama : "+str(mi.displayName)+"\n☛ Mid : " +key1+"\n☛ Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               ka.sendContact(msg.to, Amid)
                               time.sleep(0.15)
                               kb.sendContact(msg.to, Bmid)
                               time.sleep(0.15)
                               kc.sendContact(msg.to, Cmid)
                               time.sleep(0.15)
                               kd.sendContact(msg.to, Dmid)
                               time.sleep(0.15)
                               ke.sendContact(msg.to, Emid)

                        elif text.lower() == "myrechat":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               try:
                                   cl.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "rechat":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               try:
                                   ka.removeAllMessages(op.param2)
                                   ka.sendMessage(msg.to,"ᵇᵉʳʰᵃˢⁱˡ ᵇᵘᵃⁿᵍ ˢᵃᵐᵖᵃʰ ᵇᵒˢˢ")
                                   kb.removeAllMessages(op.param2)
                                   kb.sendMessage(msg.to,"ᵇᵉʳʰᵃˢⁱˡ ᵇᵘᵃⁿᵍ ˢᵃᵐᵖᵃʰ ᵇᵒˢˢ")
                                   kc.removeAllMessages(op.param2)
                                   kc.sendMessage(msg.to,"ᵇᵉʳʰᵃˢⁱˡ ᵇᵘᵃⁿᵍ ˢᵃᵐᵖᵃʰ ᵇᵒˢˢ")
                                   kd.removeAllMessages(op.param2)
                                   kd.sendMessage(msg.to,"ᵇᵉʳʰᵃˢⁱˡ ᵇᵘᵃⁿᵍ ˢᵃᵐᵖᵃʰ ᵇᵒˢˢ")
                                   ke.removeAllMessages(op.param2)
                                   ke.sendMessage(msg.to,"ᵇᵉʳʰᵃˢⁱˡ ᵇᵘᵃⁿᵍ ˢᵃᵐᵖᵃʰ ᵇᵒˢˢ")
                               except:
                                   ka.removeAllMessages(op.param2)
                                   ka.sendMessage(msg.to,"ᵇᵉʳʰᵃˢⁱˡ ᵇᵘᵃⁿᵍ ˢᵃᵐᵖᵃʰ ᵇᵒˢˢ")
                                   kb.removeAllMessages(op.param2)
                                   kb.sendMessage(msg.to,"ᵇᵉʳʰᵃˢⁱˡ ᵇᵘᵃⁿᵍ ˢᵃᵐᵖᵃʰ ᵇᵒˢˢ")
                                   kc.removeAllMessages(op.param2)
                                   kc.sendMessage(msg.to,"ᵇᵉʳʰᵃˢⁱˡ ᵇᵘᵃⁿᵍ ˢᵃᵐᵖᵃʰ ᵇᵒˢˢ")
                                   kd.removeAllMessages(op.param2)
                                   kd.sendMessage(msg.to,"ᵇᵉʳʰᵃˢⁱˡ ᵇᵘᵃⁿᵍ ˢᵃᵐᵖᵃʰ ᵇᵒˢˢ")
                                   ke.removeAllMessages(op.param2)
                                   ke.sendMessage(msg.to,"ᵇᵉʳʰᵃˢⁱˡ ᵇᵘᵃⁿᵍ ˢᵃᵐᵖᵃʰ ᵇᵒˢˢ")
                                   k1.removeAllMessages(op.param2)
                                   k1.sendMessage(msg.to,"ᵇᵉʳʰᵃˢⁱˡ ᵇᵘᵃⁿᵍ ˢᵃᵐᵖᵃʰ ᵇᵒˢˢ")

                        elif cmd.startswith("bcg: "):
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"[ Broadcast ]\n" + str(pesan))

                        elif text.lower() == "mykey":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               cl.sendMessage(msg.to, "key Now「 " + str(Leakiller["keyCmd"]) + " 」")

                        elif cmd.startswith("setkey "):
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "change key failed")
                               else:
                                   Leakiller["keyCmd"] = str(key).lower()
                                   cl.sendMessage(msg.to, "succes at「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               Leakiller["keyCmd"]=""
                               cl.sendMessage(msg.to, "succes resset key command")

                        elif cmd == "/reboot":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               cl.sendMessage(msg.to, "waiting a second")
                               Leakiller["rePoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "bot was restarting")

                        elif cmd == "runtime":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               eltime = time.time() - mulai
                               bot = "was run " +waktu(eltime)
                               cl.sendMessage(msg.to,bot)

                        elif cmd == "ginfo":
                          if msg._from in Zie:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "  •⌻「Grup Info」⌻•\n\n Nama Group : {}".format(G.name)+ "\nID Group : {}".format(G.id)+ "\nPembuat : {}".format(G.creator.displayName)+ "\nWaktu Dibuat : {}".format(str(timeCreated))+ "\nJumlah Member : {}".format(str(len(G.members)))+ "\nJumlah Pending : {}".format(gPending)+ "\nGroup Qr : {}".format(gQr)+ "\nGroup Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup"):
                          if msg._from in Zie:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "No file"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "  •⌻ List Grup Info ⌻•\n"
                                ret_ += "\n⌬ Nama Group : {}".format(G.name)
                                ret_ += "\n⌬ ID Group : {}".format(G.id)
                                ret_ += "\n⌬ Pembuat : {}".format(gCreator)
                                ret_ += "\n⌬ Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n⌬ Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n⌬ Jumlah Pending : {}".format(gPending)
                                ret_ += "\n⌬ Group Qr : {}".format(gQr)
                                ret_ += "\n⌬ Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem"):
                          if msg._from in Zie:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "● "+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"● Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except:
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in Zie:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    ka.leaveGroup(i)
                                    kb.leaveGroup(i)
                                    kc.leaveGroup(i)
                                    ka.sendMessage(msg.to,"Succes leave in group " +str(ginfo.name))

                        elif cmd == "friendlist":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "gruplist":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "z1grup":
                            if msg._from in Zie:
                               ma = ""
                               a = 0
                               gid = ka.getGroupIdsJoined()
                               for i in gid:
                                   G = ka.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               ka.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "z2grup":
                            if msg._from in Zie:
                               ma = ""
                               a = 0
                               gid = kb.getGroupIdsJoined()
                               for i in gid:
                                   G = kb.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kb.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "z3grup":
                            if msg._from in Zie:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kc.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "z4grup":
                            if msg._from in Zie:
                               ma = ""
                               a = 0
                               gid = kd.getGroupIdsJoined()
                               for i in gid:
                                   G = kd.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kd.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "z5grup":
                            if msg._from in Zie:
                               ma = ""
                               a = 0
                               gid = ke.getGroupIdsJoined()
                               for i in gid:
                                   G = ke.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               ke.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "kickergrup":
                            if msg._from in Zie:
                               ma = ""
                               a = 0
                               gid = k1.getGroupIdsJoined()
                               for i in gid:
                                   G = k1.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               k1.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "ourl":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                gurl = cl.reissueGroupTicket(msg.to)
                                cl.sendMessage(msg.to,"line://ti/g/" + gurl)

                        elif cmd == "curl":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "done°")

                        elif cmd == "zourl":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                if msg.toType == 2:
                                   X = ka.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   ka.updateGroup(X)
                                gurl = ka.reissueGroupTicket(msg.to)
                                ka.sendMessage(msg.to,"line://ti/g/" + gurl)

                        elif cmd == "zcurl":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                if msg.toType == 2:
                                   X = ka.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   ka.updateGroup(X)
                                   ka.sendMessage(msg.to, "done°")

                        elif cmd == "all urlgrup":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "●Nama : "+str(x.name)+ "\n● Url grup : http://line.me/R/ti/g/"+gurl)

                        elif cmd == "zall urlgrup":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                if msg.toType == 2:
                                   x = ka.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      ka.updateGroup(x)
                                   gurl = ka.reissueGroupTicket(msg.to)
                                   ka.sendMessage(msg.to, "● Nama : "+str(x.name)+ "\n● Url grup : http://line.me/R/ti/g/"+gurl)

#===========================================#
                        elif cmd == "pictgrup":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                              if msg.toType == 2:
                                Leakiller["gPicture"] = True
                                cl.sendMessage(msg.to,"please send pict")
                        elif cmd == "updp bot":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["DPicture"] = True
                                cl.sendMessage(msg.to,"please send pict")
                        elif 'Dpbot ' in msg.text:
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                              spl = msg.text.replace('Dpbot ','')
                              if spl == '1':
                                  Leakiller["cPicture"][Amid] = True
                                  ka.sendMessage(msg.to, "send pict boss")
                              if spl == '2':
                                  Leakiller["cPicture"][Bmid] = True
                                  kb.sendMessage(msg.to, "send pict boss")
                              if spl == '3':
                                  Leakiller["cPicture"][Cmid] = True
                                  kc.sendMessage(msg.to, "send pict boss")
                              if spl == '4':
                                  Leakiller["cPicture"][Dmid] = True
                                  kd.sendMessage(msg.to, "send pict boss")
                              if spl == '5':
                                  Leakiller["cPicture"][Emid] = True
                                  ke.sendMessage(msg.to, "send pict boss")
                        elif cmd == "my pict":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["cPicture"][mid] = True
                                cl.sendMessage(msg.to,"please Send pict")
                        elif cmd == "kickerpict":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["cPicture"][Smid] = True
                                k1.sendMessage(msg.to,"please Send pict")
                        elif cmd.startswith("zname: "):
                          if msg._from in Zie:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("z1cn: "):
                          if msg._from in Zie:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ka.getProfile()
                                profile.displayName = string
                                ka.updateProfile(profile)
                                ka.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("z2cn: "):
                          if msg._from in Zie:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kb.getProfile()
                                profile.displayName = string
                                kb.updateProfile(profile)
                                kb.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("z3cn: "):
                          if msg._from in Zie:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("z4cn: "):
                          if msg._from in Zie:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kd.getProfile()
                                profile.displayName = string
                                kd.updateProfile(profile)
                                kd.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("z5cn: "):
                          if msg._from in Zie:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ke.getProfile()
                                profile.displayName = string
                                ke.updateProfile(profile)
                                ke.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("kickercn: "):
                          if msg._from in Zie:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k1.getProfile()
                                profile.displayName = string
                                k1.updateProfile(profile)
                                k1.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd == "woy" or text.lower() == 'mention':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                group = cl.getGroup(msg.to)
                                k = len(group.members)//20
                                for j in range(k+1):
                                    aa = []
                                    for x in group.members[j*20 : (j+1)*20]:
                                        aa.append(x.mid)
                                    try:
                                        arrData = ""
                                        textx = "╔══════════════════\n╠☛ . "
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += "╠☛ . ".format(str(b))
                                            else:
                                                textx += "╚══════════════════\n╔══════════════════\n  「 ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀ : {} 」\n╚══════════════════".format(str(len(aa)))
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))

                                                except:
                                                    no = " "
                                        msg.to = msg.to
                                        msg.text = textx
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage(to, textx,{'AGENT_NAME':'[ Mentions ]', 'AGENT_LINK': 'line://ti/p/~{}'.format(cl.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + cl.getProfile().picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                    except Exception as e:
                                        cl.sendText(msg.to,str(e))
                        elif cmd == "botlist":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                ma = ""
                                a = 0
                                for m_id in Leakiller["Lea"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"  ✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴\n\n"+ma+"\nTotal : %s Bot" %(str(len(Leakiller["Lea"]))))

                        elif cmd == "adminlist":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                mb = ""
                                b = 0
                                for m_id in Leakiller["admin"]:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"「✴ᥣᵋᵅᵝᵒᵗᤰᤈᤌѴᶟᣴᶳᶦᶱᶯᤰᤈᤌ✴」\n\n"+mb+"\nTotal : %s  Admin Bot" %(str(len(Leakiller["admin"]))))

                        elif cmd == "respon":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                ka.sendMessage(msg.to,"ʜᴀᴅɪʀ ʙᴏss ϙᴜʜ...!!")
                                kb.sendMessage(msg.to,"ʜᴀᴅɪʀ ʙᴏss ϙᴜʜ...!!")
                                kc.sendMessage(msg.to,"ʜᴀᴅɪʀ ʙᴏss ϙᴜʜ...!!")
                                kd.sendMessage(msg.to,"ʜᴀᴅɪʀ ʙᴏss ϙᴜʜ...!!")
                                ke.sendMessage(msg.to,"ʜᴀᴅɪʀ ʙᴏss ϙᴜʜ...!!")

                        elif cmd == ".inv":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                try:
                                    ang = [Amid,Bmid,Cmid,Dmid,Emid]
                                    cl.inviteIntoGroup(msg.to, ang)
                                    ka.acceptGroupInvitation(msg.to,)
                                    kb.acceptGroupInvitation(msg.to,)
                                    kc.acceptGroupInvitation(msg.to,)
                                    kd.acceptGroupInvitation(msg.to,)
                                    ke.acceptGroupInvitation(msg.to,)
                                except:
                                    pass

                        elif cmd == "ajs stay":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                try:
                                    ang = [Smid]
                                    random.choice(Amin).inviteIntoGroup(msg.to, ang)
                                except:
                                    try:
                                        ang = [Smid]
                                        cl.inviteIntoGroup(msg.to, ang)
                                    except:
                                        pass

                        elif cmd == "ajs bye":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                G = k1.getGroup(msg.to)
                                k1.sendMessage(msg.to, "see u member "+str(G.name))
                                k1.leaveGroup(msg.to)

                        elif cmd == "z1bye":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                G = ka.getGroup(msg.to)
                                ka.sendMessage(msg.to, "すぐに終わらせてやる "+str(G.name))
                                ka.leaveGroup(msg.to)

                        elif cmd == "z2bye":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                G = kb.getGroup(msg.to)
                                kb.sendMessage(msg.to, "すぐに終わらせてやる "+str(G.name))
                                kb.leaveGroup(msg.to)

                        elif cmd == "z3bye":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                G = kc.getGroup(msg.to)
                                kc.sendMessage(msg.to, "すぐに終わらせてやる "+str(G.name))
                                kc.leaveGroup(msg.to)

                        elif cmd == "z4bye":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                G = kd.getGroup(msg.to)
                                kd.sendMessage(msg.to, "すぐに終わらせてやる "+str(G.name))
                                kd.leaveGroup(msg.to)

                        elif cmd == "z5bye":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                G = ke.getGroup(msg.to)
                                ke.sendMessage(msg.to, "すぐに終わらせてやる "+str(G.name))
                                ke.leaveGroup(msg.to)

                        elif cmd == "pro in":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)

                        elif cmd == "pro out":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                G = cl.getGroup(msg.to)
                                ka.sendMessage(msg.to, "強がるな、だから貴様は倒れているんのだ 😘 "+str(G.name))
                                kb.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                kd.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                ka.leaveGroup(msg.to)

                        elif cmd == "/leave":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                G = cl.getGroup(msg.to)
                                cl.sendMessage(msg.to, "ブロックリストに入れたぞ 🙏 "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in Zie:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        ka.sendMessage(i, "")
                                        kb.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        kd.leaveGroup(i)
                                        ke.leaveGroup(i)
                                        ka.sendMessage(to,"Leave succes from " +h)

                        elif cmd == "z1join":
                            if msg._from in Zie:
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ka.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ka.updateGroup(G)

                        elif cmd == "z2join":
                            if msg._from in Zie:
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kb.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kb.updateGroup(G)

                        elif cmd == "z3join":
                            if msg._from in Zie:
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)

                        elif cmd == "z4join":
                            if msg._from in Zie:
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kd.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kd.updateGroup(G)

                        elif cmd == "z5join":
                            if msg._from in Zie:
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ke.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ke.updateGroup(G)

                        elif cmd == "ajs join":
                            if msg._from in Zie:
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = k1.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k1.updateGroup(G)

                        elif cmd == ".speed respon":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "🚩response 🚩\n\n - 🌏 Speed Profile\n   %.10f\n - ➡ Speed Contact\n   %.10f\n - ➡ Speed Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               start = time.time()
                               cl.sendMessage(to, "•••")
                               elapsed_time = time.time() - start
                               cl.sendMessage(to,format(str(elapsed_time)))

                        elif cmd == ".speed" or cmd == ".sp":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               start = time.time()
                               ka.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                               elapsed_time = time.time() - start
                               ka.sendMessage(msg.to, "%s s" % (elapsed_time))
                               start2 = time.time()
                               kb.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                               elapsed_time = time.time() - start2
                               kb.sendMessage(msg.to, "%s s" % (elapsed_time))
                               start3 = time.time()
                               kc.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                               elapsed_time = time.time() - start3
                               kc.sendMessage(msg.to, "%s " % (elapsed_time))
                               start4 = time.time()
                               kd.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                               elapsed_time = time.time() - start4
                               kd.sendMessage(msg.to, "%s s" % (elapsed_time))
                               start5 = time.time()
                               ke.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                               elapsed_time = time.time() - start5
                               ke.sendMessage(msg.to, "%s s" % (elapsed_time))

                        elif cmd == "lurk on":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Leakiller['readPoint'][msg.to] = msg_id
                                 Leakiller['readMember'][msg.to] = {}
                                 cl.sendMessage(msg.to, "Lurking berhasil diaktifkan\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "lurk off":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Leakiller['readPoint'][msg.to]
                                 del Leakiller['readMember'][msg.to]
                                 cl.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "lurkers":
                          if msg._from in Zie:
                            if msg.to in Leakiller['readPoint']:
                                if Leakiller['readMember'][msg.to] != {}:
                                    aa = []
                                    for x in Leakiller['readMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\n⌬ Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n⌚ Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Leakiller['readPoint'][msg.to]
                                        del Leakiller['readMember'][msg.to]
                                    except:
                                        pass
                                    Leakiller['readPoint'][msg.to] = msg.id
                                    Leakiller['readMember'][msg.to] = {}
                                else:
                                    cl.sendMessage(msg.to, "User kosong...")
                            else:
                                cl.sendMessage(msg.to, "Ketik lurking on ")

                        elif cmd == "sider on":
                          if Leakiller["selfbot"] == True:
                           if msg._from in Zie:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "╔══════════════\n╠☛ starting cek sider\n╚══════════════\n╔══════════════\n╠☛ date : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n╠☛ hour "+ datetime.strftime(timeNow,'%H:%M:%S')+"\n╚══════════════")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if Leakiller["selfbot"] == True:
                           if msg._from in Zie:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "╔══════════════\n╠☛ sider off mode\n╚══════════════")
                              else:
                                  cl.sendMessage(msg.to, "sider in off mode")

                        elif cmd.startswith("sholat: "):
                          if msg._from in Zie:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                         ret_ = "「Jadwal Sholat」"
                                         ret_ += "\n Lokasi : " + data[0]
                                         ret_ += "\n⌬ " + data[1]
                                         ret_ += "\n⌬ " + data[2]
                                         ret_ += "\n⌬ " + data[3]
                                         ret_ += "\n⌬ " + data[4]
                                         ret_ += "\n⌬ " + data[5]
                                         ret_ += "\n\n Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                         ret_ += "\n Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                  cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("cuaca: "):
                          if msg._from in Zie:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "「Status Cuaca」"
                                    ret_ += "\n Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n Suhu : " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\n Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\n Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\n Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\n Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("lokasi: "):
                          if msg._from in Zie:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "「Info Lokasi」"
                                    ret_ += "\n Location : " + data[0]
                                    ret_ += "\n Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                cl.sendMessage(msg.to,str(ret_))

                        elif cmd.startswith("lirik: "):
                           if msg._from in Zie:
                               sep = msg.text.split(" ")
                               search = msg.text.replace(sep[0] + " ","")
                               params = {'songname': search}
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                   try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          songs = song[5]
                                          lyric = songs.replace('ti:','Title - ')
                                          lyric = lyric.replace('ar:','Artist - ')
                                          lyric = lyric.replace('al:','Album - ')
                                          removeString = "[1234567890.:]"
                                          for char in removeString:
                                              lyric = lyric.replace(char,'')
                                          ret_ = "╔══[ Lyric ]"
                                          ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Finish ]\n\nLirik nya :\n{}".format(str(lyric))
                                          cl.sendMessage(msg.to, str(ret_))
                                   except:
                                       cl.sendMessage(to, "Lirik tidak ditemukan")

                        elif cmd.startswith("music: "):
                           if msg._from in Zie:
                              sep = msg.text.split(" ")
                              search = msg.text.replace(sep[0] + " ","")
                              params = {'songname': search}
                              with requests.session() as web:
                                  web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                  r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                  try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          ret_ = "╔══[ Music ]"
                                          ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Waiting Audio ]"
                                      cl.sendMessage(msg.to, str(ret_))
                                      cl.sendMessage(msg.to, "Loading....")
                                      cl.sendAudioWithURL(msg.to, song[3])
                                  except:
                                      cl.sendMessage(to, "Musik tidak ditemukan")

                        elif cmd.startswith("zimage: "):
                          if msg._from in Zie:
                            sep = msg.text.split(" ")
                            search = msg.text.replace(sep[0] + " ","")
                            url = "https://api.xeonwz.ga/api/image/google?q={}".format(urllib.parse.quote(search))
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["data"] != []:
                                    start = timeit.timeit()
                                    items = data["data"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    cl.sendMessage(msg.to,"「Google Image」\nType : Search Image\nTime taken : %seconds" % (start))
                                    cl.sendImageWithURL(msg.to, str(path))

                        elif cmd.startswith("smule: "):
                          if msg._from in Zie:    
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                cl.sendMessage(msg.to, "Sedang Mencari...")
                                time.sleep(2)
                                cl.sendMessage(msg.to, "ID Smule : "+smule+"\nLink : "+links)
                                cl.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass

                        elif cmd.startswith("yt4: "):
                          if msg._from in Zie:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n Author : ' + str(vid.author)
                                    durasi = '\n Duration : ' + str(vid.duration)
                                    suka = '\n Likes : ' + str(vid.likes)
                                    rating = '\n Rating : ' + str(vid.rating)
                                    deskripsi = '\n Deskripsi : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                cl.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendText(msg.to,str(e))

                        elif cmd.startswith("yt3: "):
                          if msg._from in Zie:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n Author : ' + str(vid.author)
                                    durasi = '\n Duration : ' + str(vid.duration)
                                    suka = '\n Likes : ' + str(vid.likes)
                                    rating = '\n Rating : ' + str(vid.rating)
                                    deskripsi = '\n Deskripsi : ' + str(vid.description)
                                cl.sendImageWithURL(msg.to, me)
                                cl.sendAudioWithURL(msg.to, shi)
                                cl.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))

                        elif cmd.startswith("profileig: "):
                          if msg._from in Zie:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['user']['full_name'])
                                bioIG = str(data['user']['biography'])
                                mediaIG = str(data['user']['media']['count'])
                                verifIG = str(data['user']['is_verified'])
                                usernameIG = str(data['user']['username'])
                                followerIG = str(data['user']['followed_by']['count'])
                                profileIG = data['user']['profile_pic_url_hd']
                                privateIG = str(data['user']['is_private'])
                                followIG = str(data['user']['follows']['count'])
                                link = " Link : " + "https://www.instagram.com/" + instagram
                                text = " Name : "+namaIG+"\n Username : "+usernameIG+"\n Biography : "+bioIG+"\n Follower : "+followerIG+"\n Following : "+followIG+"\n Post : "+mediaIG+"\n Verified : "+verifIG+"\n Private : "+privateIG+"" "\n" + link
                                cl.sendImageWithURL(msg.to, profileIG)
                                cl.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("cekdate: "):
                          if msg._from in Zie:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"⇸「 I N F O 」⇷\n\n"+" Date Of Birth : "+lahir+"\n Age : "+usia+"\n Ultah : "+ultah+"\n Zodiak : "+zodiak)

                        elif cmd.startswith("max: "):
                          if Leakiller["selfbot"] == True:
                           if msg._from in Zie:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Leakiller["Maxlimit"] = num
                                cl.sendMessage(msg.to,"Max spam Tag " +strnum)

                        elif cmd.startswith("scall: "):
                          if Leakiller["selfbot"] == True:
                           if msg._from in Zie:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Leakiller["limit"] = num
                                cl.sendMessage(msg.to,"Max spam call " +strnum)

                        elif cmd.startswith("stag "):
                          if Leakiller["selfbot"] == True:
                           if msg._from in Zie:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Leakiller["Maxlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                    else:
                                        cl.sendMessage(msg.to,"Jumlah melebihi 1000")

                        elif cmd == "scall":
                          if Leakiller["selfbot"] == True:
                           if msg._from in Zie:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(Leakiller["limit"])
                                cl.sendMessage(to, "Succes {} Spam Call".format(str(Leakiller["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                         cl.acquireGroupCallRoute(to)
                                         cl.inviteIntoGroupCall(to, contactIds=members)
                                     except:
                                         pass
                                else:
                                    cl.sendMessage(to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if Leakiller["selfbot"] == True:
                           if msg._from in Zie:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if Leakiller["selfbot"] == True:
                           if msg._from in Zie:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Leakiller["spamMsg"]))
                                      ka.sendMessage(midd, str(Leakiller["spamMsg"]))
                                      kb.sendMessage(midd, str(Leakiller["spamMsg"]))
                                      kc.sendMessage(midd, str(Leakiller["spamMsg"]))
                                      kd.sendMessage(midd, str(Leakiller["spamMsg"]))
                                      ke.sendMessage(midd, str(Leakiller["spamMsg"]))

                        elif 'ID line: ' in msg.text:
                          if Leakiller["selfbot"] == True:
                           if msg._from in Zie:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

                        elif 'Welcome ' in msg.text:
                          if Leakiller["selfbot"] == True:
                           if msg._from in Zie:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in Leakiller["welcome"]:
                                       msgs = "Msg Welcome was on"
                                  else:
                                       Leakiller["welcome"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "In Group: " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「on mode」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Leakiller["welcome"]:
                                         del Leakiller["welcome"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "In Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Msg Welcome mode on"
                                    cl.sendMessage(msg.to, "「off mode」\n" + msgs)
                        elif 'Left ' in msg.text:
                          if Leakiller["selfbot"] == True:
                           if msg._from in Zie:
                              spl = msg.text.replace('Left ','')
                              if spl == 'on':
                                  if msg.to in Leakiller["leaveMsg"]:
                                       msgs = "Msg Left was on"
                                  else:
                                       Leakiller["leaveMsg"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "In Group: " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「on mode」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Leakiller["leaveMsg"]:
                                         del Leakiller["leaveMsg"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "In Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Msg Leave mode on"
                                    cl.sendMessage(msg.to, "「off mode」\n" + msgs)
                        elif 'Proqr ' in msg.text:
                          if Leakiller["selfbot"] == True:
                           if msg._from in Zie:
                              spl = msg.text.replace('Proqr ','')
                              if spl == 'on':
                                  if msg.to in Leakiller["proqr"]:
                                       msgs = "Succes"
                                  else:
                                       Leakiller["proqr"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "In Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「on mode」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Leakiller["proqr"]:
                                         del Leakiller["proqr"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "In Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url on"
                                    cl.sendMessage(msg.to, "「off mode」\n" + msgs)
                        elif 'Autokick ' in msg.text:
                          if Leakiller["selfbot"] == True:
                           if msg._from in Zie:
                              spl = msg.text.replace('Autokick ','')
                              if spl == 'on':
                                  if msg.to in Leakiller["proKick"]:
                                       msgs = "Autokick on"
                                  else:
                                       Leakiller["proKick"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "In Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「on mode」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Leakiller["proKick"]:
                                         del Leakiller["proKick"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "In Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Autokick off"
                                    cl.sendMessage(msg.to, "「off mode」\n" + msgs)
                        elif 'Procancel ' in msg.text:
                          if Leakiller["selfbot"] == True:
                           if msg._from in Zie:
                              spl = msg.text.replace('Procancel ','')
                              if spl == 'on':
                                  if msg.to in Leakiller["proCancel"]:
                                       msgs = "Procancel on"
                                  else:
                                       Leakiller["proCancel"] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "In Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「on mode」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Leakiller["proCancel"]:
                                         Leakiller["proCancel"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "In Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Procancel off"
                                    cl.sendMessage(msg.to, "「off mode」\n" + msgs)
                        elif 'Protect ' in msg.text:
                          if Leakiller["selfbot"] == True:
                           if msg._from in Zie:
                              spl = msg.text.replace('Protect ','')
                              if spl == 'on':
                                  if msg.to in Leakiller["proqr"]:
                                       msgs = ""
                                  else:
                                      Leakiller["proqr"][msg.to] = True
                                  if msg.to in Leakiller["proKick"]:
                                      msgs = ""
                                  else:
                                       Leakiller["proKick"][msg.to] = True
                                  if msg.to in Leakiller["proInvite"]:
                                      msgs = ""
                                  else:
                                       Leakiller["proInvite"][msg.to] = True
                                  if msg.to in Leakiller["proCancel"]:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "High Allprotection mode on at : " +str(ginfo.name)
                                  else:
                                       Leakiller["proCancel"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "High Allprotection mode on at : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「on mode」\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Leakiller["proqr"]:
                                         del Leakiller["proqr"][msg.to]
                                    else:
                                         msgs = ""
                                    if msg.to in Leakiller["proKick"]:
                                         del Leakiller["proKick"][msg.to]
                                    else:
                                         msgs = ""
                                    if msg.to in Leakiller["proInvite"]:
                                         del Leakiller["proInvite"][msg.to]
                                    else:
                                         msgs = ""
                                    if msg.to in Leakiller["proCancel"]:
                                         del Leakiller["proCancel"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protection mode off at : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protection mode off at : " +str(ginfo.name)
                                    cl.sendMessage(msg.to, "「off mode」\n\n" + msgs)
                        elif 'Inta ' in msg.text:
                          if Leakiller["selfbot"] == True:
                           if msg._from in Zie:
                              spl = msg.text.replace('Inta ','')
                              if spl == 'on':
                                  if msg.to in Leakiller["intaPoint"]:
                                       msgs = "Inta on"
                                  else:
                                       Leakiller["intaPoint"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "IntaPoint on at Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「on mode」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Leakiller["intaPoint"]:
                                         del Leakiller["intaPoint"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Intapoint off at Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Inta off"
                                    cl.sendMessage(msg.to, "「off mode」\n" + msgs)

                        elif ("Add con " in msg.text):
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                   targets.append(x["M"])
                               for target in targets:
                                   try:
                                       kays = cl.getContact(target)
                                       cl.findAndAddContactsByMid(kays.mid)
                                       cl.sendMessage(msg.to,"Done add " + cl.getContact(target).displayName + " Done add my friend")
                                   except Exception as e:
                                       print(e)

                        elif ("Bot kick " in msg.text):
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Introvert:
                                       try:
                                           cl.sendMessage(msg.to, "sorry bocah lu,,gw kick..!!!")
                                           random.choice(Amin).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Z1 kick " in msg.text):
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Angrust:
                                       try:
                                           ka.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Z2 kick " in msg.text):
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Introvert:
                                       try:
                                           kb.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Z3 kick " in msg.text):
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Introvert:
                                       try:
                                           kc.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Z4 kick " in msg.text):
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Introvert:
                                       try:
                                           kd.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Z5 kick " in msg.text):
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Introvert:
                                       try:
                                           ke.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Kiss " in msg.text):
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Introvert:
                                       try:
                                           cl.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Kicker kick " in msg.text):
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Introvert:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ti = cl.reissueGroupTicket(msg.to)
                                           k1.acceptGroupInvitationByTicket(msg.to,Ti)
                                           k1.kickoutFromGroup(msg.to, [target])
                                           X = k1.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           k1.updateGroup(X)
                                           k1.leaveGroup(msg.to)
                                       except:
                                           pass

                        elif ("Cancel" in msg.text):
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               group = cl.getGroup(msg.to)
                               if group.invitee is None:
                                   cl.sendMessage(op.message.to, "empty ")
                               else:
                                   nama = [contact.mid for contact in group.invitee]
                                   for x in nama:
                                     if x not in Introvert and x not in Leakiller["Lea"] and x not in Leakiller["admin"]:
                                       cl.cancelGroupInvitation(msg.to, [x])
                                       time.sleep(0.3)
                                   cl.sendMessage(to, "done.")

                        elif ("Bot cancel" in msg.text):
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               group = cl.getGroup(msg.to)
                               if group.invitee is None:
                                   cl.sendMessage(op.message.to, "empty ")
                               else:
                                   nama = [contact.mid for contact in group.invitee]
                                   for x in nama:
                                     if x not in Introvert and x not in Leakiller["Lea"] and x not in Leakiller["admin"]:
                                       random.choice(Amin).cancelGroupInvitation(msg.to, [x])
                                       time.sleep(0.3)
                                   cl.sendMessage(to, "done.")

                        elif ("Addadmin " in msg.text):
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target in Leakiller["admin"]:
                                       cl.sendMessage(msg.to,"was admin")
                                   else:
                                       try:
                                           Leakiller["admin"][target] = True
                                           cl.sendMessage(msg.to,"Succes add admin")
                                       except:
                                           pass
                        elif ("Addbot " in msg.text):
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target in Leakiller["Lea"]:
                                       cl.sendMessage(msg.to,"was bot")
                                   else:
                                       try:
                                           Leakiller["Bots"][target] = True
                                           cl.sendMessage(msg.to,"Succes add bot")
                                       except:
                                           pass
                        elif ("Deladmin " in msg.text):
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Leakiller["admin"]:
                                       cl.sendMessage(msg.to,"not in admin")
                                   else:
                                        try:
                                            del Leakiller["admin"][target]
                                            cl.sendMessage(msg.to,"Succes delete admin")
                                        except:
                                            pass
                        elif ("Delbot " in msg.text):
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Leakiller["Lea"]:
                                       cl.sendMessage(msg.to,"not in bots")
                                   else:
                                        try:
                                            del Leakiller["Lea"][target]
                                            cl.sendMessage(msg.to,"Succes delete bots")
                                        except:
                                            pass
                        elif cmd == "cbot" or text.lower() == 'clear bot':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                              ang = cl.getContacts(Leakiller["Lea"])
                              mc = "%i Bots " % len(ang)
                              cl.sendMessage(msg.to,"done boss " +mc)
                              Leakiller["Lea"] = {}
                        elif cmd == "cadmin" or text.lower() == 'clear admin':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                              ang = cl.getContacts(Leakiller["admin"])
                              mc = "%i Admin " % len(ang)
                              cl.sendMessage(msg.to,"done boss " +mc)
                              Leakiller["admin"] = {}
                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["addadmin"] = True
                                cl.sendMessage(msg.to,"Send Contact...")
                        elif cmd == "admin:del" or text.lower() == 'admin:del':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["deladmin"] = True
                                cl.sendMessage(msg.to,"Send Contact...")
                        elif cmd == "admin:off" or text.lower() == 'admin off':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["addadmin"] = False
                                cl.sendMessage(msg.to,"Send Contact...")
                        elif cmd == "deladmin:off" or text.lower() == 'deladmin off':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["deladmin"] = False
                                cl.sendMessage(msg.to,"done")
                        elif cmd == "bot:on" or text.lower() == 'bot on':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["abots"] = True
                                cl.sendMessage(msg.to,"Send Contact...")
                        elif cmd == "bot:off" or text.lower() == 'bot off':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["abots"] = False
                                cl.sendMessage(msg.to,"done boss")
                        elif cmd == "bot:del" or text.lower() == 'bot del':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["dbots"] = True
                                cl.sendMessage(msg.to,"Send Contact...")
                        elif cmd == "delbot:off" or text.lower() == 'delbot off':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["dbots"] = False
                                cl.sendMessage(msg.to,"done")
                        elif cmd == "allrefresh" or text.lower() == 'refresh':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["addadmin"] = False
                                Leakiller["deladmin"] = False
                                Leakiller["abots"] = False
                                Leakiller["dbots"] = False
                                Leakiller["ablacklist"] = False
                                Leakiller["dblacklist"] = False
                                cl.sendMessage(msg.to,"done bosquh")
                        elif cmd == "killban":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                if msg.toType == 2:
                                    group = cl.getGroup(msg.to)
                                    gMembMids = [contact.mid for contact in group.members]
                                    matched_list = []
                                    for tag in wait["blacklist"]:
                                        matched_list+=filter(lambda str: str == tag, gMembMids)
                                    if matched_list == []:
                                        return
                                    for jj in matched_list:
                                        try:
                                            klist=[ka,kb,kc,kd,ke]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[jj])
                                            print (msg.to,[jj])
                                        except:
                                            pass
                        elif cmd == "ctbot" or text.lower() == 'ctbot':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                ma = ""
                                for i in Leakiller["Lea"]:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                        elif cmd == "contact:on" or text.lower() == 'contact on':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["contact"] = True
                                cl.sendMessage(msg.to,"Contact allready on")
                        elif cmd == "contact:off" or text.lower() == 'contact off':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["contact"] = False
                                cl.sendMessage(msg.to,"Contact allready off")
                        elif cmd == "respon:on" or text.lower() == 'respon on':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["detectMention"] = True
                                cl.sendMessage(msg.to,"Auto allready on")
                        elif cmd == "respon:off" or text.lower() == 'respon off':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["detectMention"] = False
                                cl.sendMessage(msg.to,"Auto respon allready off")
                        elif cmd == "autojoin:on" or text.lower() == 'autojoin on':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["autoJoin"] = True
                                cl.sendMessage(msg.to,"Autojoin allredy on")
                        elif cmd == "autojoin:off" or text.lower() == 'autojoin off':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["autoJoin"] = False
                                cl.sendMessage(msg.to,"Autojoin allready off")
                        elif cmd == "like:on" or text.lower() == 'like on':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                              Leakiller["LikeOn"] = True
                              cl.sendMessage(msg.to,"Auto Like allready on")
                        elif cmd == "like:off" or text.lower() == 'like off':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                              Leakiller["LikeOn"] = False
                              cl.sendMessage(msg.to,"Auto Like allready off")
                        elif cmd == "scan:on" or text.lower() == 'scan on':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["checkmid"] = True
                                cl.sendMessage(msg.to," allredy on")
                        elif cmd == "scan:off" or text.lower() == 'scan off':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["checkmid"] = False
                                cl.sendMessage(msg.to," allready off")
                        elif cmd == "post:on" or text.lower() == 'post on':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["checkPost"] = True
                                cl.sendMessage(msg.to,"Check Post allredy on")
                        elif cmd == "post:off" or text.lower() == 'post off':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["checkPost"] = False
                                cl.sendMessage(msg.to,"Check Post allready off")
                        elif cmd == "unsend:on" or text.lower() == 'unsend on':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["Unsend"] = True
                                cl.sendMessage(msg.to,"Detect unsend allredy on")
                        elif cmd == "unsend:off" or text.lower() == 'unsend off':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["Unsend"] = False
                                cl.sendMessage(msg.to,"Detect unsend allready off")
                        elif cmd == "autoadd:on" or text.lower() == 'autoadd on':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["autoAdd"] = True
                                cl.sendMessage(msg.to,"Auto add allready on")
                        elif cmd == "autoadd:off" or text.lower() == 'autoadd off':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["autoAdd"] = False
                                cl.sendMessage(msg.to,"Auto add allready off")
                        elif cmd == "sticker:on" or text.lower() == 'sticker on':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["sticker"] = True
                                cl.sendMessage(msg.to,"Sticker allready on")
                        elif cmd == "sticker:off" or text.lower() == 'sticker off':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["sticker"] = False
                                cl.sendMessage(msg.to,"Sticker alleady off")
                        elif cmd == "jticket:on" or text.lower() == 'jticket on':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["autoJoinTicket"] = True
                                cl.sendMessage(msg.to,"Join ticket allready on")
                        elif cmd == "jticket:off" or text.lower() == 'jticket off':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["autoJoinTicket"] = False
                                cl.sendMessage(msg.to,"Notag allready off")
                        elif ("Ban " in msg.text):
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target in wait["blacklist"]:
                                       cl.sendMessage(msg.to,"was blacklist")
                                   else:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"Succes add blacklist")
                                       except:
                                           pass
                        elif ("Delban " in msg.text):
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in wait["blacklist"]:
                                       cl.sendMessage(msg.to,"not in blacklist")
                                   else:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMessage(msg.to,"Succes removed blacklist")
                                       except:
                                           pass
                        elif cmd == "ban:on" or text.lower() == 'ban on':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["ablacklist"] = True
                                cl.sendMessage(msg.to,"Send Contact...")
                        elif cmd == "ban:off" or text.lower() == 'ban off':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["ablacklist"] = False
                                cl.sendMessage(msg.to,"done boss")
                        elif cmd == "unban:on" or text.lower() == 'unban on':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["dblacklist"] = True
                                cl.sendMessage(msg.to,"Send Contact...")
                        elif cmd == "unban:off" or text.lower() == 'unban off':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                Leakiller["dblacklist"] = False
                                cl.sendMessage(msg.to,"done boss")
                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"| Blacklist ●\n\n"+ma+"\nTotal : 「%s」 Blacklist User " %(str(len(wait["blacklist"]))))
                        elif cmd == "cban" or text.lower() == 'cban':
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                              ang = cl.getContacts(wait["blacklist"])
                              mc = "%i Blacklist " % len(ang)
                              cl.sendMessage(msg.to,"done boss " +mc)
                              wait["blacklist"] = {}
                        elif 'Add: ' in msg.text:
                          if Leakiller["selfbot"] == True:
                           if msg._from in Zie:
                              ang = msg.text.replace('Add: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Leakiller["message"] = ang
                                  cl.sendMessage(msg.to, "「Msg add」 :\n\n「{}」".format(str(ang)))
                        elif 'Left: ' in msg.text:
                          if Leakiller["selfbot"] == True:
                           if msg._from in Zie:
                              ang = msg.text.replace('Left: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Leakiller["leftmsg"] = ang
                                  cl.sendMessage(msg.to, "「Msg leave」 :\n\n「{}」".format(str(ang)))
                        elif 'Welcome: ' in msg.text:
                          if Leakiller["selfbot"] == True:
                           if msg._from in Zie:
                              ang = msg.text.replace('Welcome: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Leakiller["sambutan"] = ang
                                  cl.sendMessage(msg.to, "「Msg wellcome」 :\n\n「{}」".format(str(ang)))
                        elif 'Tag: ' in msg.text:
                          if Leakiller["selfbot"] == True:
                           if msg._from in Zie:
                              ang = msg.text.replace('Tag: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Leakiller["msgTag"] = ang
                                  cl.sendMessage(msg.to, "「Msg tag」:\n\n「{}」".format(str(ang)))
                        elif 'Spam: ' in msg.text:
                          if Leakiller["selfbot"] == True:
                           if msg._from in Zie:
                              ang = msg.text.replace('Spam: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Leakiller["spamMsg"] = ang
                                  cl.sendMessage(msg.to, "「Msg spam」 :\n\n「{}」".format(str(ang)))
                        elif 'Sider: ' in msg.text:
                          if Leakiller["selfbot"] == True:
                           if msg._from in Zie:
                              znf = msg.text.replace('Sider: ','')
                              if znf in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Leakiller["siderMsg"] = znf
                                  cl.sendMessage(msg.to, "「Msg cctv」:\n\n「{}」".format(str(znf)))
                        elif text.lower() == "cekmsg":
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               cl.sendMessage(msg.to, "「Msg add」 :\n「 " + str(Leakiller["message"]) + " 」")
                               cl.sendMessage(msg.to, "「Msg cctv」:\n「 " + str(Leakiller["siderMsg"]) + " 」")
                               cl.sendMessage(msg.to, "「Msg tag」:\n「 " + str(Leakiller["msgTag"]) + " 」")
                               cl.sendMessage(msg.to, "「Msg spam」:\n「 " + str(Leakiller["spamMsg"]) + " 」")
                               cl.sendMessage(msg.to, "「Msg welcome」:\n「 " + str(Leakiller["sambutan"]) + " 」")
                               cl.sendMessage(msg.to, "「Msg leave」:\n「 " + str(Leakiller["leftmsg"]) + " 」")
#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                              if Leakiller["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "succes join : %s" % str(group.name))
                        elif (msg.text in "Cleanse"):
                          if Leakiller["selfbot"] == True:
                            if msg._from in Zie:
                               if msg.toType == 2:
                                  group = cl.getGroup(msg.to)
                                  group = ka.getGroup(msg.to)
                                  group = kb.getGroup(msg.to)
                                  group = kc.getGroup(msg.to)
                                  group = kd.getGroup(msg.to)
                                  group = ke.getGroup(msg.to)
                                  nama = [contact.mid for contact in group.members]
                                  for x in nama:
                                      if x not in Introvert:
                                          if x not in Leakiller["Lea"]:
                                              if x not in Leakiller["admin"]:
                                                  try:
                                                      klist=[ka,kb,kc,kd,ke]
                                                      ang=random.choice(klist)
                                                      ang.kickoutFromGroup(msg.to,[x])
                                                      time.sleep(0.001)
                                                  except:
                                                      print ("limit")
                        elif msg.text.lower() in ["check"]:
                            if msg._from in Zie:
                                anu = cl.getGroup(msg.to)
                                oncom = ["ub7081271bf7414f6af87a999bb5f07d7"] #MID PUSKUN
                                for _mid in oncom:
                                    message="╭━ᬼᬼᬼ͜͡ʟ͜͡є͜͡ɑ͜͡ᬽ͜͡ʙ͜͡ɵ͜͡τ͜͡ʂ͜͡ᬼ͜͡ѵ͜͡е͜͡ʀ͜͡ƽ͜͡і͜͡ɵ͜͡ɳ͜͡ᬽᬽ━─\n"
                                    try:
                                        cl.kickoutFromGroup(msg.to,[_mid])
                                        message+="│「☇Fresh」Kick\n"
                                    except:
                                        message+="│「☹ Limit」Kick\n"
                                    try:
                                        ka.inviteIntoGroup(msg.to,[_mid])
                                        message+="│「☇Fresh」Invite\n"
                                    except:
                                        message+="│「☹ Limit」Invite\n"
                                    try:
                                        kb.kickoutFromGroup(msg.to,[_mid])
                                        message+="│「☇Fresh」Kick\n"
                                    except:
                                        message+="│「☹ Limit」Kick\n"
                                    try:
                                        kc.inviteIntoGroup(msg.to,[_mid])
                                        message+="│「☇Fresh」Invite\n"
                                    except:
                                        message+="│「☹ Limit」Invite\n"
                                    try:
                                        kd.kickoutFromGroup(msg.to,[_mid])
                                        message+="│「☇Fresh」Kick\n"
                                    except:
                                        message+="│「☹ Limit」Kick\n"
                                    try:
                                        ke.inviteIntoGroup(msg.to,[_mid])
                                        message+="│「☇Fresh」Invite\n"
                                    except:
                                        message+="│「☹ Limit」Invite\n"
                                    message+="╰━━━━━━━━─"
                                    cl.sendMessage(msg.to,message)
#=====================#
          except Exception as error:
              print (error)
    except Exception as error:
        print (error)

while True:
    try:
        ops = linePoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                linePoll.setRevision(op.revision)
                thread = threading.Thread(target=bot, args=(op,))
                thread.start()
    except Exception as e:
        print(e)

