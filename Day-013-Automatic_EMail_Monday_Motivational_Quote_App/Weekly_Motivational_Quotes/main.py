import smtplib
import random
import datetime as dt

my_email = "youremail@email.com"
my_password = "your_smtp_app_password"

now = dt.datetime.now()

if now.weekday() == 0: # 0 = Monday
    with open("./quotes.txt",mode="r") as datafile:
        quotes_list = datafile.readlines()
        current_quote = random.choice(quotes_list)

    try:
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="qrtwry@yahoo.com",
                msg = f"Subject:Monday Motivational Quote\n\n{current_quote}"
            )
    
        print("Email Send Successfully")
    
    except smtplib.SMTPException as e:
            print(f"Error: Failed to send email to {my_email}.")
            print(f"Details: {e}")