from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://www.amazon.in/Samsung-Galaxy-Storage-Corning-Gorilla/dp/B0FW3XS6YG/ref=sr_1_9?s=electronics&sr=1-9"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0",
    "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
    "Accept-Language": "en-GB,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Connection": "keep-alive",
    "Referer": "https://www.amazon.in/",
    "Cookie": "session-id=524-0657700-8417929; session-id-time=2082787201l; i18n-prefs=INR; lc-acbin=en_IN; ubid-acbin=522-9856409-0204929; session-token=WBOjsA9kKRgjMfNtuaFzUKh1f4pZySnmq5dMVxeRcOb0UHUqB4JQP41f4e7WE6QrV0V9Xoyuw3DxmuTulou7ZhOyJQUxoPvC3HmczGNFkIaLf3BzKJfITXNPsQLfofszJuVqJfZH2R7LsQ//bbzEOZE6dBHYneHXW4sHX/OpeRfABctrXFmV1xdcT/J0YchI8KZ0XLxz66iY2jLxzXAUjSxE/B+9H8QN",
    "Sec-Fetch-Dest": "image",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-site",
    "Priority": "u=5, i",
    "TE": "trailers"
}

response = requests.get(url,headers=header)

soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(class_ = "a-offscreen").get_text()

price_without_currency = price.split("₹")[1]

price_as_float = float(price_without_currency.replace(",", ""))
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 19999

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for \n\n {price}!"

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"],port = 587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg = f"Subject:Amazon Price Alert!\n\n{message}\n\n{url}".encode("utf-8")
        )
