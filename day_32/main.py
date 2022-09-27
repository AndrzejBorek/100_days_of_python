# import smtplib
#
# my_email_gmail = ""
# my_email_yahoo = ""

# Yahoo : smtp.mail.yahoo.com
# Google : smtp.gmail.com

# AS FOR DAY 26.09.2022 this version generates error:  smtplib.SMTPConnectError
# connection = smtplib.SMTP("smtp.mail.yahoo.com", port=465)
# print("Created connection")
# connection.starttls()  # This command secures my email
# print("Connection stat=rt tls")
# connection.login(user=my_email_yahoo, password=password)
# print("Successful login")
# connection.sendmail(from_addr=my_email_yahoo, to_addrs=my_email_gmail, msg='HELLO WORLD')
# connection.close()

# I DO NOT KNOW HOW TO SEND FROM YAHOO TO GMAIL, AS 26.09.2022 YAHOO GENERATING APP PASSWORD DOES NOT WORK
# THIS VERSION DOES NOT WORK:
# app_password ="" # THIS PASSWORD WILL NOT WORK AS 26.09.2022
# with smtplib.SMTP_SSL("smtp.mail.yahoo.com", port=465) as connection:
#     connection.login(user=my_email_yahoo, password=password)
#     connection.sendmail(from_addr=my_email_yahoo, to_addrs=my_email_gmail, msg='HELLO WORLD from yahoo')

# app_password = ""  # THIS IS MY APP PASSWORD GENERATED IN GOOGLE
# # TO THIS VERSION WORKING I HAD TO GENERATE APP PASSWORD IN MY GMAIL PROFILE
# with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
#     connection.login(user=my_email_gmail, password=app_password)
#     connection.sendmail(from_addr=my_email_gmail, to_addrs=my_email_yahoo,
#                         msg='Subject: Hello \n\n This is the body of my email')


import datetime as dt

# now = dt.datetime.now()
# print(now)
#
# current_year = now.year
# print(current_year)
#
# current_month = now.month
#
# current_day = now.day
#
# current_hour = now.hour
#
# current_minute = now.minute
#
# current_second = now.second
#
# current_microsecond = now.microsecond
#
# current_weekday = now.weekday()
# print(current_weekday)
#
# date_of_birth = dt.datetime(year=1998, month=1, day=01, hour=00, minute=00)
# print(date_of_birth)


# import datetime as dt
# import random
# import smtplib
#
# my_email_gmail = ""
# my_email_yahoo = ""
# app_password = ""
# google_id = "smtp.gmail.com"
#
# with open('quotes.txt') as f:
#     quotes = [quote.replace("\"", '').rstrip('\n') for quote in f.readlines()]
#
# now = dt.datetime.now()
#
#
# if now.isoweekday() == 1:
#     with open('quotes.txt') as f:
#         quotes = [quote.replace("\"", '').rstrip('\n') for quote in f.readlines()]
#         quote = random.choice(quotes)
#     with smtplib.SMTP_SSL(google_id, port=465) as connection:
#         connection.login(user=my_email_gmail, password=app_password)
#         connection.sendmail(from_addr=my_email_gmail, to_addrs=my_email_gmail,
#                             msg=f'Subject: Motivational quote \n\n {quote}')
