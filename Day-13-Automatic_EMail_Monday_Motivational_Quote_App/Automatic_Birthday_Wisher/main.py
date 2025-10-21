import pandas
import datetime as dt
import random
import smtplib

my_email = "youremail@email.com"
my_password = "your_smtp_app_password"

df = pandas.read_csv("./birthdays.csv")

birthday_records = df.to_dict(orient="records")

now = dt.datetime.now()

for record in birthday_records:
    if now.month == record['month'] and now.day == record['day']:
        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt", mode="r") as letter:
            letter_content = letter.read()
            current_letter = letter_content.replace("[NAME]",record['name'])

        try:
            with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
                connection.starttls()
                connection.login(user=my_email,password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=record["email"],
                    msg=f"Subject:Happy Birthday {record['name']}\n\n{current_letter}"
                )

        except smtplib.SMTPException as e:
            print(f"Error: Failed to send email to {record['name']} ({record['email']}).")
            print(f"Details: {e}")
    
        print(f"Message sent successfully to {record['name']}")