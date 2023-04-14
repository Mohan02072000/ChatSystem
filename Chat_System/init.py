from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
 
 
 
bot= ChatBot('bot')

def Trainer():
   

    trainer=ChatterBotCorpusTrainer(bot)

    trainer.train('chatterbot.corpus.english')



r=input("Need to train the bot?: y or n")
if(r=="y" or r=="Y"):
    Trainer()

while 1:
    message=input("You: ")
    response=bot.get_response(message)
    print("Bot: "+str(response))
    if(message=="bye"):
        break
