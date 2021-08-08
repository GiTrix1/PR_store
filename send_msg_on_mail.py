import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

user_login = 'Логин почты'
user_password = 'Временный пароль почты'
to_address_all = []
to_address_20 = []
circle = 0
all_to_address = []

with open('База электронных почт', 'r', encoding='utf8') as for_spam:
    for one_address in for_spam.read().split('\n'):
        to_address_all.append(one_address)
    for _ in range(2):
        to_address_20 = to_address_all[:20]
        subject = 'Ваш заголовок'
        text = 'Ваш текст для продвижения'

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['To'] = ', '.join(to_address_20)
        msg['From'] = 'Имя вашего дела <' + user_login + '>'

        part_text = MIMEText(text)

        msg.attach(part_text)

        mail = smtplib.SMTP('smtp.mail.ru: 25')
        mail.starttls()
        mail.login(user_login, user_password)
        mail.sendmail(from_addr=user_login, to_addrs=to_address_20, msg=msg.as_string())
        print(f'Вот кто получил сообщение: {to_address_20}')
        all_to_address.append(to_address_all[:20])
        del to_address_all[:20]
        circle += 1
        mail.quit()
        print(f'Цикл {circle} пройден\n')
    print(f'Отправил {circle} сообщении, всего {circle * len(to_address_20)} людей получили сообщении\n'
          f'Вот список адресов тех, кто получил сообщение:'
          '\n_____________________________________________')
    for i in all_to_address:
        print(i)
    print('_____________________________________________')
