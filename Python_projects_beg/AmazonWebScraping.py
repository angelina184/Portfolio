from bs4 import BeautifulSoup
import requests
import time
import datetime
import csv
import pandas as pd
import os
import smtplib


EMAIL = 'xxxxxxxxxx@gmail.com'
FILE = r'C:\my work\Amazon_file.csv'
STUDENT_EMAIL = 'xxxxxxxx@st.swps.edu.pl'
#Connect to the website
URL = "https://www.amazon.com/Lytiarul-Christian-Tshirts-Religious-Inspirational/dp/B0DZ29GKH5/ref=sr_1_3?crid=3RI3NQ19EJE9&dib=eyJ2IjoiMSJ9.EFvx7nxQXp6Ta1M03yqz50LeUJ1f-TRl2d6GNADCxd5uHh5_SMerXy_7moCEHUA-Ic1ECMLvkLaSxBVl6ZwsrrRwXlUF8xZ5VhubIGFiIOhdFEHxBErjkWFSGGgL3ywcRcVDYkH0vwdg70jVw0fa7ro19lYWra4BiyIEfWz5NagxDJuG4FLJOcUU1v4tEJqFKFZYsDgTmvoZOPujGspBexaN4-NVKWbWqn0o9E0P_KLOKhO63g3pmSfbc0TGEU36cDIGcdftz7G-OteUjtieGO1UCp72ad7V8dQvdNu-kdE.CS8fEKkKN4FZJjY38gVbBXFvHRmpM8M5mxgsRAA0AWs&dib_tag=se&keywords=tshirt+got+data&qid=1756124122&sprefix=tshirt+got+data%2Caps%2C218&sr=8-3"
#avoid getting blocked(shows that I am not a bot) + https://httpbin.org/get +
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36","Accept-Encoding": "gzip, deflate, br, zstd","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Language": "en-US;q=0.6,en;q=0.5"}


def data_scraping():
    page = requests.get(URL,headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    #prints all html code
    #print(soup1)

    #make it look better
    soup2 = BeautifulSoup(soup1.prettify(),"html.parser")
    # print(soup2)

    title = soup2.find(id = "productTitle").get_text().strip()
    print(title)

    price = soup2.find(class_ = "a-offscreen").get_text().strip()[1:]
    print(price) #$14.99 -> 14.99

    rate = soup2.find(class_ = "a-icon a-icon-star a-star-5 cm-cr-review-stars-spacing-big").get_text().strip()
    print(rate)

    today = datetime.date.today()
    print(today)
    
    data_dict = {"Title": title,"Price": price,"Rate": rate,"Date": today}
    return data_dict

def apdate_file():
    data = data_scraping()
    file_exists = os.path.isfile(FILE)
    fieldnames = list(data.keys())
    #a+ = otwórz plik do dopisywania i czytania.
    # append new data to csv
    with open(FILE,'a+', newline='',encoding='UTF8') as file:
        #to solve prblem(everithing writes down in one column) added delimiter=';'
        writer = csv.DictWriter(file, fieldnames=fieldnames,delimiter=';')
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)
    df = pd.read_csv(FILE, sep = ';')
    print(df)

def email_sender():
    data = data_scraping()
    price = float(data["Price"])  # price is the 2nd element in the list
    if price>10:
        #For Gmail, we use port number 587
        server = smtplib.SMTP("smtp.gmail.com", 587)
        # start TLS for security
        server.ehlo()
        server.starttls()
        server.ehlo()
        # Authentication
        server.login(EMAIL, "xxxxxxxxxxx")
        subj = "The price is now lower!"
        body = "Go and buy it on Amazon"
        # message to be sent
        message = f"Subject: {subj}\n\n{body}"
            # sending the mail
        server.sendmail(EMAIL,STUDENT_EMAIL,message)
        # terminating the session
        server.quit()

def save_data():
    while True:
        apdate_file()
        #checks price,rate and other data every single day (86400)
        check_when = 86400
        time.sleep(check_when)
        email_sender()

def main():
    save_data()


if __name__=='__main__':
    main()