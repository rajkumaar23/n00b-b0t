from main import *
lastUpdateID=None
print ('firing up\n')
while True:
    updates=getUpdates(lastUpdateID)
    if len(updates["result"])>0:
        lastUpdateID=getLatestUpdateID(updates) + 1
        for update in updates["result"]:
            message,who,name=extract(update)
            try:
                print("from",name,"message",message)
            except:
                pass 
            if message=="/start":
                reply="Hello, "+name+". I'm Horny Horse, found by RAJKUMAR! Don't get anxious coz my name is horny :P Talk to me and I'll try to serve your purpose :)"
                #reply=reply+"\n1)A wikipedia article? \nType wiki-articlename \nExample : wiki-Shah Rukh Khan"
                reply=reply+"\n 1)Shall I find lyrics of a song of your interest?(But I've more collections of English songs than any other language ) \n Type like Ly-songname-artistname \n Example : Ly-Maps-Maroon 5"
                reply=reply+"\n2)Shall I tell you the chemistry between you and your lover? In simple terms, shall I calculate your love? \n Type Lc-yourname-partnername \nExample: Lc-Dhanush-Aishwarya"
                reply=reply+"\n3)Shall I find famous quotes or quotes from movies? \nType qu-Quotetype \n(In Quotetype, use either 'movies' or 'famous'\n Example: qu-famous "
            else:
                
                reply=process(message)
            sendMessage(reply,who)
            print(reply, "reply sent")    

       
