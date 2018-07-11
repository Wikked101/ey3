import platform
import random
import socket
import sys

reload(sys)
sys.setdefaultencoding('utf8')

server = "irc.cygen.net"
channel = "#chat"
botnick = "ey3"
sentUser = False
sentNick = False

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "\nConnecting to:" + server
irc.connect((server, 6667))

try:
   while 1:
      text = irc.recv(2048)
      if len(text) > 0:
         print text
      else:
         continue

      if text.find("PING") != -1:
         irc.send("PONG " + text.split()[1] + "\n")

      if sentUser == False:
         irc.send("USER " + botnick + " " + botnick + " " + botnick + " :Ey3\n")
         sentUser = True
         continue

      if sentUser and sentNick == False:
         irc.send("NICK " + botnick + "\n")
         sentNick = True
         continue

      if text.find("255 " + botnick) != -1:
         irc.send("JOIN " + channel + "\n")

      if text.find(":!host") != -1:
         irc.send("PRIVMSG " + channel + " :" + str(platform.platform()) + "\n")

except KeyboardInterrupt:
   irc.send("QUIT :I have to go for now!\n")
   print "\n"
   sys.exit()
