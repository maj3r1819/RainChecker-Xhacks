import schedule
import scraper
import db


def update():
    users = db.updateWatchList()
    for user in users:
        print(user)
        watch_list = db.getWatchList(user["email"])
        for item in watch_list:
            print(item)
            res = scraper.get_products(item["item_name"])
            print(db.addItem(user["email"], item["item_name"], res))
    print(db.updateWatchList())


if __name__ == "__main__":
    schedule.every().day.at("00:00").do(update)
