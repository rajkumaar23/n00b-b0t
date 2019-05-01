import json
import requests
import config
URL="https://api.telegram.org/bot{}/".format(config.token)
commands=["ly","Ly","Lc","lc","qu","QU","Qu","wiki","Wiki","WIKI"]


def sendMessage(text,chatID):
    url=URL+"sendMessage?chat_id={}&text={}".format(chatID,text)
    response=requests.get(url)



def quotes(cat):
    url="https://andruxnet-random-famous-quotes.p.mashape.com/?cat={}&count=1".format(cat) 
    r=requests.get(url,headers={"X-Mashape-Key": "TnRwfAX1FOmshuQxxYye0IloqkFvp1FeTN2jsnsfTrUALCDJ8w","Content-Type": "application/x-www-form-urlencoded","Accept": "application/json"})
    k=0
    try:
        data=json.loads(r.content)
        k=1
    except:
        pass
    if k==1:
        cat=data["quote"]
        author=data["author"]
        result=cat+" \n -"+author
        return result
    else:
        return "Error!Not found!! :("
  




def lca(fname,sname):
    url="https://love-calculator.p.mashape.com/getPercentage?fname={}&sname={}".format(fname,sname)
    r=requests.get(url,headers={"X-Mashape-Key": "TnRwfAX1FOmshuQxxYye0IloqkFvp1FeTN2jsnsfTrUALCDJ8w","Accept": "application/json"})
    data = json.loads(r.content)
    percent=data["percentage"]
    comment=data["result"]
    result="Percentage is : {} \n Comment is : {}".format(percent,comment)
    return result
    
def lyrics(song,artist):
    url="https://musixmatchcom-musixmatch.p.mashape.com/wsr/1.1/matcher.lyrics.get?q_artist={}&q_track={}".format(artist,song)
    r=requests.get(url,headers={"X-Mashape-Key": "TnRwfAX1FOmshuQxxYye0IloqkFvp1FeTN2jsnsfTrUALCDJ8w","Accept": "application/json"})
    k=0
    try:
        data = json.loads(r.content)
        k=1
    except:
        pass
    if k==1:
        return data["lyrics_body"]
    else:
        return "Error! Lyrics not found :("
    


def isCommand(text):
    command=text.split("-")[0]
    if command in commands:
        return True
    else:
        return False

def process(text):
    if isCommand(text):
        command=text.split('-')
        if command[0]=="ly" or command[0]=="Ly":
            if command[1]:
                song = command[1]
                artist = command[2]
                value=lyrics(song,artist) 
                return value
        if command[0]=="lc" or command[0]=="Lc":
            if command[1]:
                fname=command[1]
                sname=command[2]
                return lca(fname,sname)
        if command[0]=="Qu" or command[0]=="QU" or command[0]=="qu":
            if command[1]:
                cat=command[1]
                return quotes(cat)
        if command[0]=="wiki":
            if command[1]:
                return wiki()    


                
        
    else:
        return text


def extract(json):
    try:
        text=json["message"]["text"]
    except:
        text=" "
    chatID=json["message"]["chat"]["id"]
    name=json["message"]["chat"]["first_name"]
    
    return text,chatID,name

def getJSON(url):
    response = requests.get(url)
    jsonData=json.loads(response.content.decode("utf-8"))
    return jsonData

def getUpdates(offset=None):
    url=URL+"getUpdates?timeout=100"
    if offset:
        url=URL+"getUpdates?offset={}".format(offset)
    jsonData=getJSON(url)
    return jsonData


def getLatestUpdateID(updates):
    ids =[]
    for update in updates["result"]:
        ids.append(int(update["update_id"]))
        return max(ids)


def replyToAll(updates):
    for update in updates["result"]:
            text=update["message"]["text"]
            chatID=update["message"]["chat"]["id"]
            sendMessage(text,chatID)




