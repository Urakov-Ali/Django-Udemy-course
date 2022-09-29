import requests
from telebot.models import Tele_Settings

#---------------------with get method
# def sendMessage():
#     api = 'https://api.telegram.org/bot'
#     method = api + bot_token + '/SendMessage?' + 'chat_id=' + chat_id + '&text=' + text
#     req = requests.get(method)


#----------------------with post method
def sendTelegram(tele_name, tele_number):
    if Tele_Settings.objects.get(pk=1):
        telebot = Tele_Settings.objects.get(pk=1)
        bot_token = str(telebot.tele_token)
        chat_id = str(telebot.tele_chat_id)
        text = str(telebot.tele_text)
        api = 'https://api.telegram.org/bot'
        method = api + bot_token + '/SendMessage?' 
    
        if text.find('{') and text.find('}') and text.rfind('{'):  
            a = text.find('{')
            b = text.find('}')
            c = text.rfind('{')

            part1 = text[0:a]
            part2 = text[b+1:c]

            text_slice = part1 + tele_name + part2 + tele_number
        else:
            text_slice = text
    
        try:
            req = requests.post(method, data={
                'chat_id':chat_id,
                'text':text_slice
            })
        except: 
            pass
        finally:
            if req.status_code != 200:
                print('Ошибка отправки')
            elif req.status_code == 500:
                print('Ошибка 505')
            else:
                print('Все ок сообшение отправлено')

    else: 
        pass
        print('база данных не сушествует')

    
    

