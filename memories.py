import os, sys, telebot
from termcolor import colored
bot = telebot.TeleBot('СЮДА ВСТАВТЕ ТОКЕН ВАШЕГО БОТА')
os.system("clear")
print(colored("""
 ::::::::  :::   ::: :::::::::  :::::::::: :::::::::  :::    :::  ::::::::      :::           
:+:    :+: :+:   :+: :+:    :+: :+:        :+:    :+: :+:    :+: :+:    :+:   :+: :+:         
+:+         +:+ +:+  +:+    +:+ +:+        +:+    +:+ +:+    +:+ +:+         +:+   +:+        
+#+          +#++:   +#++:++#+  +#++:++#   +#++:++#:  +#+    +:+ +#++:++#++ +#++:++#++:       
+#+           +#+    +#+    +#+ +#+        +#+    +#+ +#+    +#+        +#+ +#+     +#+       
#+#    #+#    #+#    #+#    #+# #+#        #+#    #+# #+#    #+# #+#    #+# #+#     #+#       
 ########     ###    #########  ########## ###    ###  ########   ########  ###     ###       
::::    ::::  :::::::::: ::::    ::::   ::::::::  :::::::::  ::::::::::: :::::::::: ::::::::  
+:+:+: :+:+:+ :+:        +:+:+: :+:+:+ :+:    :+: :+:    :+:     :+:     :+:       :+:    :+: 
+:+ +:+:+ +:+ +:+        +:+ +:+:+ +:+ +:+    +:+ +:+    +:+     +:+     +:+       +:+        
+#+  +:+  +#+ +#++:++#   +#+  +:+  +#+ +#+    +:+ +#++:++#:      +#+     +#++:++#  +#++:++#++ 
+#+       +#+ +#+        +#+       +#+ +#+    +#+ +#+    +#+     +#+     +#+              +#+ 
#+#       #+# #+#        #+#       #+# #+#    #+# #+#    #+#     #+#     #+#       #+#    #+# 
###       ### ########## ###       ###  ########  ###    ### ########### ########## ########  

  """, 'red'))
print(colored("""                                                                            
 ----------------------MODE---------------------
 [1] - USER
 [2] - CHAT
 [3] - CLEAR USER
 [4] - CLEAR CHAT
 _______________________________________________
 """, 'yellow'))
 
 
action = input(colored("MODE: ", 'green'))


if action == '1':
 os.system("clear")
 global userid
 userid = input(colored("ID: ", 'green'))
 
 print(colored("STATUS: RECORDING", 'red'))
 
 @bot.message_handler(content_types=['text'])
 def save_file(message):
  if str(message.from_user.id) == str(userid):
   save_file = open("user.txt", "a+")
   save_file.write("user-> "+str(message.from_user.first_name))
   save_file.write("\nid-> "+str(message.from_user.id))
   save_file.write("\nmsg-> "+str(message.text))
   save_file.write("\n\n")
   save_file.close()
   print(colored("STATUS: REWRITE", 'green'))
  else:
   print('azaza')
   
elif action == '2':
 os.system("clear")

 print(colored("STATUS: RECORDING", 'red'))

 @bot.message_handler(content_types=['text'])
 def save_file_chat(message):
  save_file = open("chat.txt", "a+")
  save_file.write("user-> "+str(message.from_user.first_name))
  save_file.write("\nid-> "+str(message.from_user.id))
  save_file.write("\nmsg-> "+str(message.text))
  save_file.write("\n\n")
  save_file.close()
  print(colored("STATUS: REWRITE", 'green'))
  
  
elif action == '3':
 c_file = open("user.txt", "w+")
 c_file.write("")
 c_file.close()
 
 
elif action == '4':
 c_file = open("chat.txt", "w+")
 c_file.write("")
 c_file.close()
else:
 pass

bot.polling()


