import image
import urllib

import re
from pip._vendor.distlib.compat import raw_input
#from pygame import mixer # Load the required library
#import vlc
#p = vlc.libvlc_media_player_get_media("http://your_mp3_url")
#p = vlc.MediaPlayer("http://your_mp3_url")
#p.play()

#url = "https://i.imgur.com/lqb0GJ6.jpg"
#urllib3.get_host("https://i.imgur.com/lqb0GJ6.jpg")

#Image.open(urllib3.urlopen(url))
words = ""

#Image.open(requests.get(url, stream=True).raw)
while words != "Bye Eliza":
    words = raw_input("You : ")

    # Matching words
    match1 = re.search(r'feel+.(so \w+|\w+)+.[\w\s]+.because+.([\w\s]+)',words)
    match2 = re.search(r'bad+.(\w+|\w+)',words)
    match3 = re.search(r'([S|s]he|[H|h]e)+.always+.(\w+)',words)
    match4 = re.search(r'I\'m (sad|guilty|bored|annoyed|angry)',words)
    match5 = re.search(r'[l|L]ike',words)
    match6 = re.search(r'[\w\s\W]+.want to tell something',words)
    match7 = re.search(r'I\'m+.(so \w+|\w^a+)',words)
    match8 = re.search(r'[m|M]y (boy|girl)friend',words)
    match9 = re.search(r'[m|M]y ex (girlfriend|boyfriend)',words)
    match10 = re.search(r'I don\'t understand',words)
    match11 = re.search(r'another+.(man|woman)',words)
    match12 = re.search(r'fight',words)
    match13 = re.search(r'([S|s]he|[h|H]e)+.angry',words)
    match14 = re.search(r'([T|t]hank you)',words)
    match15 = re.search(r'without any reason',words)
    match16 = re.search(r'[h|H]ow?',words)
    match17 = re.search(r'I love (him|her)',words)
    match18 = re.search(r'beautiful',words)
    match19 = re.search(r'don\'t want to hurt+.(him|her)',words)
    match20 = re.search(r'why asking',words)
  

    if words == "Bye Eliza":
        print("MEMEllie : Byee!")
    elif match1:
        print("MEMEllie : Never going to give you  up, never going to  let you down... ")
    elif match2:
        print("MEMEllie :  " + "Cause baby now we got bad blood You know it used to be mad love So take a look at what you've done And baby now we got bad blood Did you have to do this?"+match2.groups()[0])
    elif match3:
        if match3.groups()[1] == "bad":
            print("MEMEllie : Look what you just made me do ")
        else:
            print("MEMEllie : ")
    elif match4:
        print("MEMEllie : Mad World, I'm feeling so "+match4.groups()[0] +". "+groups()[0]+" sad world")
    elif match5:
        print("MEMEllie : O'Rly?")
    elif match6:
        print("MEMEllie : Don't blame me, love made me crazy. If it doesn't, you ain't doin' it right")
    elif match7:
        print("MEMEllie : Why are you "+match7.groups()[0]+"?")
    elif match8:
        if match8.groups()[0] == "girl":
            print("MEMEllie : gurrrl ")
    elif match9:
        print("MEMEllie :  "+match9.groups()[0]+"?")
    elif match10:
        print("MEMEllie : You can ask Google if you don't understand")
    elif match11 or match12:
        print("MEMEllie : didn't know there'd be beef at dis barbeque")
    elif match13:
        print("MEMEllie : Why "+match13.groups()+" angry with you?")
    elif match14:
        print("MEMEllie : You don't need to say "+match14.groups()[0].lower()+". I know everybody needs me. I'm so useful")
    elif match15:
        print("MEMEllie : There is a reason, you have to find it")
    elif match16:
        print("MEMEllie : Don't ask me, i don't even have an experience about it. I'm just a bot. A smart bot")
    elif match17:
        print("MEMEllie : May I know what makes you love "+match17.groups()[0]+"?")
    elif match18:
        print("MEMEllie : you are beautiful just the way you are, cause when you smile.. ")
    elif match19:
        print("MEMEllie : See you don't want to hurt "+match19.groups()[0]+". Woah i saw a pair of wings behind your back there. You are such an angel!")
    elif match20:
        print("MEMEllie : Just want to know")
    else:
        print("MEMEllie : hey whats up hello ")
