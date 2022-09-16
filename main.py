import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com/Razer-Basilisk-Ultimate-HyperSpeed-Wireless/dp/B07YPBX9Y7/ref=sr_1_8?crid=YN0IWE51I8&keywords=razer+mouse&qid=1663306362&sprefix=Razer%2Caps%2C179&sr=8-8&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(name="span", class_="a-offscreen").get_text()
price = price[1:]
price_as_float = float(price)
print(price_as_float)


title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200
my_email = "email"
my_password = "app passawor"  # this is app passaword you need generated in gmail setting

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='773517485@qq.com',
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )