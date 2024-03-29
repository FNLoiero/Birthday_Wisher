import random
import pandas
import smtplib
from datetime import datetime

my_email = "federico.apli.py@gmail.com"
password = "btnm uebw otng miai"

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"],data_row["day"] ): data_row for (index,data_row) in data.iterrows()}
today = datetime.now()
today_tuple = (today.month,today.day)

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt", 'r') as archivo:
        letter = archivo.read()
        letter = letter.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Para fede\n\n{letter}")