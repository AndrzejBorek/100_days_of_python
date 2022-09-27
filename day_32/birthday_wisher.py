import random
import smtplib
import datetime as dt
import pandas as pd

my_email_gmail = ""
app_password = ""
google_id = "smtp.gmail.com"

data = pd.read_csv('birthdays.csv')


def email_pattern(name: str, age: int):
    file_path = f"letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", name).replace("[AGE]", str(age))
    return contents


def send_birthday_wish():
    now = dt.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    person_birthday = {
        row['name']: {'age': year - row['year'], 'month': row['month'], 'day': row['day'], 'email': row['email']}
        for index, row
        in data.iterrows() if row['month'] == month and row['day'] == day}
    for person in person_birthday.items():
        msg = email_pattern(name=person[0], age=person[1]['age'])
        with smtplib.SMTP_SSL(google_id, port=465) as connection:
            connection.login(user=my_email_gmail, password=app_password)
            connection.sendmail(from_addr=my_email_gmail, to_addrs=person[1]['email'],
                                msg=f"Subject:Happy Birthday!\n\n{msg}".encode('utf-8'))


send_birthday_wish()
