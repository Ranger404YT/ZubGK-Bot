import random
from bot import bot, settings, db

class Logs:
    def __init__(self):
        self.bot=bot

    def log(self):
        if settings['chat'] == 1:
            chat_id = 959170286505295892
        elif settings['chat'] == 2:
            chat_id = 959522267287654431
        return self.bot.get_channel(chat_id)#959168952532078622

class Quest:
    def __init__(self,db):
        self.db = db

    def quest_add(self):
        pass

    def end_quest(self):
        pass

    def check_quest(self):
        pass

    def get_quest(self,member,quest=None):
        if quest == None:
            return db.get_quests(member)
        else:
            return db.get_quest(member,quest)

def rand_ball():
    rand=random.randint(0,5)
    if rand == 0:
        return 'Да!'
    elif rand == 1:
        return 'Бессомненно!'
    elif rand == 2:
        return 'Нет!'
    elif rand == 3:
        return 'Даже не думай!'
    elif rand == 4:
        return 'Сомневаюсь!'
    elif rand == 5:
        return 'Не хочу с тобой говорить!'
    elif rand == 6:
        return 'Я занят!'
