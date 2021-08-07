import getpass
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
import re


DRIVER_PATH = "C:/Users/" + getpass.getuser() + "/Downloads/edgedriver_win64/msedgedriver.exe"


def urlify(s):

    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)

    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '+', s)

    return s


def get_products(product):
    product = urlify(product)

    address = "https://www.google.com/search?q=" + product + "&tbm=shop"

    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument("headless")
    options.add_argument("disable-gpu")

    driver = Edge(executable_path=DRIVER_PATH, options=options)
    driver.get(address)
    driver.implicitly_wait(10)
    products = []

    if len(driver.find_elements_by_css_selector("div.CSEDeb.V5niGc.bOFGdf.sh-sr__shop-result-header.wcUdwf")) > 0: # check if the website format is the column instead of grid
        all_res = driver.find_elements_by_css_selector("div.sh-dlr__content.xal5Id")
        if len(all_res) == 0:
            print("No results found")
        for res in all_res[1:11]:
            price = res.find_element_by_css_selector("span.a8Pemb")
            product_name = res.find_element_by_css_selector("h3.OzIAJc")
            vendor = res.find_element_by_css_selector("div.b07ME.mqQL1e").find_element_by_tag_name("span")
            link = res.find_element_by_css_selector("a.VZTCjd").get_attribute("href")
            image = res.find_element_by_css_selector("img.TL92Hc").get_attribute("src")
            products.append(
                [product_name.text.rstrip(" ..."), float(re.sub(r'[^\d.]+', "", price.text)), vendor.text, link, image])
        driver.close()
        products.sort(key=lambda x: x[1])
    else:
        all_res = driver.find_elements_by_css_selector("div.i0X6df")
        if len(all_res) == 0:
            print("No results found")
        for res in all_res[:10]:
            price = res.find_element_by_css_selector("span.a8Pemb")
            product_name = res.find_element_by_css_selector("h4.A2sOrd")
            vendor = res.find_element_by_css_selector("div.aULzUe.IuHnof")
            link = res.find_element_by_css_selector("a.eaGTj.mQaFGe.shntl").get_attribute("href")
            image = res.find_element_by_css_selector("div.ArOc1c").find_element_by_tag_name("img").get_attribute("src")
            products.append([product_name.text.rstrip(" ..."), float(re.sub(r'[^\d.]+', "", price.text)), vendor.text, link, image])
        driver.close()
        products.sort(key=lambda x: x[1])
    return products


if __name__ == "__main__":
    wanted = input("What product do you want?")
    print(get_products(wanted))
