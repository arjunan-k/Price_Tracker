import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "your email"
PASSWORD = "your password"

# ------------------ You can add your desired product URL ------------------ #

URL = "https://www.amazon.com/dp/B08PWR7NBY/ref=sbl_dpx_kitchen-electric-cookware_B09BLBGK2T_0"
HEADER = {
    "User-Agent": "type your user agent, can be obtained by searching in google",
    "Accept-Language": "your language, can be obtained by searching in google"
}

response = requests.get(url=URL, headers=HEADER)
data = response.text
soup = BeautifulSoup(data, "lxml")     # "lxml" parser is used if "html.parser" is not working.
price = soup.find("span", class_="a-offscreen").getText().split("$")
product_price = float(price[1])
product_name = soup.find(id="productTitle").get_text().strip()
my_price = 300

if product_price < my_price:

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        quote = f"{product_name} is now ${product_price}"
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="email you want to send price alert",
            msg=f"Subject:Price alert, Your favourite item can be grabbed for a low price now!....\n\n{quote}")