import urllib.request
import time
import smtplib


def notification(signal=0):
    if signal == 1:
        content = "Easton_avaliable"
    elif signal == 2:
        content = "Polaris_avaliable"
    elif signal == 3:
        content = "Both are avaliable"

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('email', 'password')
    mail.sendmail('email', 'password', content)
    mail.close()


def main():
    while True:
        time.sleep(2)
        with urllib.request.urlopen(
                'http://www.apple.com/shop/retail/pickup-message?parts.0=MN5T2LL%2FA&cppart=VERIZON%2FUS&store=R009') as response:
            html_easton = response.read()

        with urllib.request.urlopen(
                'http://www.apple.com/shop/retail/pickup-message?parts.0=MN5T2LL%2FA&cppart=VERIZON%2FUS&store=R417') as response:
            html_polaris = response.read()

        easton = str(html_easton)

        polaris = str(html_polaris)

        ip7_easton = easton.find('"storeSelectionEnabled":true')
        ip7_polaris = polaris.find('"storeSelectionEnabled":true')
        if ip7_easton == -1 and ip7_polaris == -1:
            print(time.ctime())

            print("Easton&Polaris_unavaliable")
            print("--------")
        elif ip7_easton != -1 and ip7_polaris == -1:
            print("Easton_avaliable")
            signal = 1
            return signal
        elif ip7_easton == -1 and ip7_polaris != -1:
            print("Polaris_avaliable")
            signal = 2
            return signal
        else:
            print("Both are avaliable")
            signal = 3
            return signal


ifErr = False

try:
   notification(main())
except urllib.error.HTTPError as err:
    print(err.code)
    ifErr = True

while ifErr:
    try:
       notification(main())
    except urllib.error.HTTPError as err:
        print(err.code)







