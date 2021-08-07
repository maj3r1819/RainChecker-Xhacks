import json
from flask_login import UserMixin
from mongoengine import connect, Document, EmbeddedDocument,EmbeddedDocumentListField, StringField, BooleanField, SortedListField, EmbeddedDocumentField, ListField, FloatField

connect('RainChecker')

# sudo service mongod status


# [[option name,  price, vendor name, link, image link], [option name,  price, vendor name, link, image link]]

class Option(EmbeddedDocument):
    optionName = StringField()
    price = FloatField()
    supplier = StringField()
    link = StringField()
    imageLink = StringField()


class Item(EmbeddedDocument):
    item_name = StringField()
    options = SortedListField(EmbeddedDocumentField(Option), ordering = 'price')
    # link = StringField()
    # price = StringField()

class User(Document):
    # username = StringField()
    email = StringField()
    password = StringField()
    # watchList = SortedListField(EmbeddedDocumentField(Item), ordering = 'item_name')
    watchList = ListField(EmbeddedDocumentField(Item))

class LoginUser(Document, UserMixin):
    email = StringField()




def addUser(email, password):
    if User.objects(email = email).first():
        return 'email already used'

    User(email = email, password = password).save()
    LoginUser(email = email).save()
    return 'new user created'


def removeUser(email):
    if not User.objects(email = email).first():
        return 'user not exist'

    User.objects(email = email).first().delete()
    LoginUser.objects(email = email).first().delete()


# [[option name,  price, vendor name, link, image link], [option name,  price, vendor name, link, image link]]

def addItem(email, item_name, allOptions):
    user = User.objects(email = email).first()
    if not user:
        return 'user not exist'

    watchList = user.watchList
    for item in watchList:
        if item.item_name == item_name:
            # replace all options for existing items
            for i in range(len(item.options)):
                item.options.pop(0)
                for opt in allOptions:
                    temp = Option(optionName = opt[0], price = opt[1], supplier = opt[2], link = opt[3], imageLink = opt[4])
                    item.options.append(temp)
            
            user.save()
            return 'item options renewed'

    item = Item(item_name = item_name)
    
    for opt in allOptions:
        temp = Option(optionName = opt[0], price = opt[1], supplier = opt[2], link = opt[3], imageLink = opt[4])
        item.options.append(temp)

    watchList.append(item)
    user.save()
    return 'item added into watch list'


def removeItem(email, item_name):
    user = User.objects(email = email).first()
    if not user:
        return 'user does not exist'

    watchList = user.watchList
    for i in range(len(watchList)):
        if watchList[i].item_name == item_name:
            watchList.pop(i)
            user.save()
            return 'item removed from watch list'

    return 'item not found in watch list'

# [[option name,  price, vendor name, link, image link], [option name,  price, vendor name, link, image link]]

def getWatchList(email):
    user = User.objects(email = email).first()
    if not user:
        return 'user not found'

    temp_watchlist = []
    for item in user.watchList:
        temp_item = {}
        temp_item['item_name'] = item.item_name
        temp_item['options'] = []
        for option in item.options:
            temp_option = {}
            temp_option['option_name'] = option.optionName
            temp_option['price'] = option.price
            temp_option['supplier'] = option.supplier
            temp_option['link'] = option.link
            temp_option['image_link'] = option.imageLink

            temp_item['options'].append(temp_option)

        temp_watchlist.append(temp_item)
    
    return temp_watchlist


# [[option name,  price, vendor name, link, image link], [option name,  price, vendor name, link, image link]]


if __name__ == '__main__':
    User.drop_collection()
    LoginUser.drop_collection()
    print(json.dumps(json.loads(User.objects().to_json()), sort_keys=True, indent=4))
    print(json.dumps(json.loads(LoginUser.objects().to_json()), sort_keys=True, indent=4))
    print('\n\n\n')
    print(addUser('wzheng2013@gmail.com', '123456'))
    print(addItem('wzheng2013@gmail.com', 'apple', [['apple 1', 100, 'sup 1', 'apple.com', 'image.link']]))
    print(addItem('wzheng2013@gmail.com', 'soccer', [['soccer 1', 100, 'sup 1', 'soccer.com', 'image.link'], ['soccer 2', 50, 'sup 2', 'soccer.com', 'image.link']]))
    # expect soccer price be 50 then 100
    print(getWatchList('wzheng2013@gmail.com'))
    print(addItem('wzheng2013@gmail.com', 'soccer', [['soccer 3', 100, 'sup 3', 'soccer.com', 'image.link']]))
    print(getWatchList('wzheng2013@gmail.com'))

    print(json.dumps(json.loads(User.objects().to_json()), sort_keys=True, indent=4))
    print('\n\n\n')
    print(json.dumps(json.loads(LoginUser.objects().to_json()), sort_keys=True, indent=4))
    User.drop_collection()
    LoginUser.drop_collection()