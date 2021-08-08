import schedule
import scraper
import db
import emailer
import time


def update():
    users = db.updateWatchList()
    for user in users:
        print(user)
        watch_list = db.getWatchList(user["email"])
        for item in watch_list:
            res = scraper.get_products(item["item_name"])
            lowest = res[0]
            for option in res[1:]:
                if lowest[1] > option[1]:
                    lowest = option
            curr_lowest = db.getCheapestOption(user["email"], item["item_name"])
            if curr_lowest is not None and lowest[1] < curr_lowest["price"]:
                print("lower found")
                emailer.email_lower_price(item["item_name"], lowest, user["email"])
            db.addItem(user["email"], item["item_name"], res)
    db.updateWatchList()


if __name__ == "__main__":
    schedule.every().day.at("00:00").do(update)
    while True:
        schedule.run_pending()
        time.sleep(300)
