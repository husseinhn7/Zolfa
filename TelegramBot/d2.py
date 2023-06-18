from telebot import  TeleBot
bot = TeleBot('6202700443:AAFV2jcNIVDet6hC_v2fCx0N9MfrK_sfEpg')

@bot.message_handler(commands=['start'])
def d(message):
    chat = message.chat
    response = f"Chat ID: {chat.id}\nChat Type: {chat.type}\nTitle: {chat.title} \n user {chat.username} \n user {chat.first_name}"
    bot.send_message(chat.id, "بيقولك مره واحد منوفي بعت ابنه يجيب تلات ارغفه مراته ماتت اتصل بابنه وقاله هات اتنين بس")
    
    
    
def send(m):   
    bot.send_message(1494250709 , m)
 
  
class TelegramBot(TeleBot):   
    def __init__(self ):
        super().__init__()
    @staticmethod
    def s():
        print('ddd')
        
        
if __name__ == '__main__':
    bot.polling()

