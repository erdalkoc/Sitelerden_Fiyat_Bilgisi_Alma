import requests
import smtplib
import time
from bs4 import BeautifulSoup

url = "https://www.hepsiburada.com/logitech-m90-usb-optik-kablolu-mouse-siyah-p-BS3504"

headers ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

def check_Price():
    global content
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    title= soup.find(id='product-name').get_text().strip()     # Sayfadaki (id='product-name') olan satrı alır ve gettext() ile içinden sadece metin olan kısmı geri döndürür.Strip() ile kenarlarındaki boşlukları atar.
    print(title)

    span = soup.find(id='offering-price')                      # Sayfadaki (id='offering-price') olan satrı alır
    content = span.attrs.get('content')                        # alınan metin içerisinde başlığı 'content' olan kısmı alır
    price = float(content)                                     # metni sayıya dönüştürür
    print(price)

    # if (price < 100) :              # Bir Karşılaştırmaya göre mail atmaya karar verilebilir
    #     # send_mail(title)

    send_mail(title)


def send_mail(title):
    sender ='erdalerdal166@gmail.com'
    receiver = 'erdalkoc166@hotmail.com'

    try:
        server =smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()                                   # server'i başlatır
        server.starttls()                               # Güvenliği sağlar
        server.login(sender,'qaatqeywllulwqqx')               # Bu Şifre Google hesabından geçici olarak oluşturuldu

        subject = title + ' Fiyat Bilgisi  :    ' + content + ' TL'
        body    = 'Bu Linkten Gidebilirsin    : '+ url
        mailcontent= f"To:{receiver}\nFrom:{sender}\nSubject:{subject}\n\n{body}"
        server.sendmail(sender,receiver,mailcontent)

        print('Mail Gönderildi')
    except smtplib.SMTPException as e:
        print(e)
    finally:
        server.quit()


while(1):
    check_Price()
    time.sleep(60*60)












