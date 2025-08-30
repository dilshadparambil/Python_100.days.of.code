# Automated Birthday Wisher
# download all the contents of intermediate_plus/d32/my_code

# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# go to account->security ->turn on 2 factor authentication->search for app passwords and create a app password and copyb paste it in the my_password variable without spaces
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.

import pandas,datetime,os,random,smtplib

my_email="dilshadkareemparambil@gmail.com"
password="zvgqypeikwrddtdc"

birthday_data=pandas.read_csv("./birthdays.csv")
birthday_data=birthday_data.to_dict(orient='records')

now=datetime.datetime.now()
day=now.day
month=now.month

for item in birthday_data:
    if item['month']==month and item['day']==day:
        chosen_dir=random.choice(os.listdir("./letter_templates"))
        print(chosen_dir)
        with open(f"./letter_templates/{chosen_dir}") as file:
            contents=file.read()
            send_letter=contents.replace('[NAME]',item['name'])
            connection=smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=item['email'],
                msg=f"Subject:Happy Birthday!!\n\n{send_letter}"
            )
            connection.close()



