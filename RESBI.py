#automatic startup is confiured in the "sudo crontab -e" file
'''1st -) ilk olarak raspberry pi bilgisayarımızı ethernet kablosu ile internete bağlıyoruz.
   2=> internetimizi statik olarak ayarlıyoruz.
   statik ip nasıl yapılır => a) Terminali aç
                              b) " sudo nano /etc/dhcpcd.conf " yaz enter'a bas.
                              c) Açılan konfigürasyon dosyasına aşağıdaki satrıları yaz;
                                          -> interface wlan0
                                          -> static_routers 193.140.221.254 not:(Bu kısım gateway olarak geçiyor.)
                                          -> static domain_name_servers 193.140.221.5
                                          -> static ip_address 193.140.221.141
                              d) ctrl+o 'ya bas sonra enter de ctrl+x 'e bas kaydet ve çık.
                              e)Raspberry pi bilgisayarı yeniden başlat.
                              f)Terminali aç "ifconfig" yaz. Çıkan sayfada "inet" kısmında yukarıda yazılan
                              ıp adresi varsa statik ip olmuş demektir.
                              g) son olarak internet simgesine sağ tıklayıp "wireless & wired network setting
                              yazan kısımlara yukarıdaki belirlediğiniz ıp adreslerini girip kayıt edip çıkacaksınız.
    3=> UPS'i pirize takıyoruz.
    4=>UPS 'in ön panelindeki ledlere bağlı olan kabloların kırmızı olanı voltaj(GPIO-14- 8 nolu pin),
    siyah olanı ground(Ground pini yani 9 nolu pin) onları raspberry pi bilgisayarımızın pinlerine bağlıyoruz.
    5=>F5 yaparak kodu çalıştırıyoruz.  Ve bitti :)
    6=> Test: Kodu test etmek için UPS'in fişi çek ve terminalede e-posta gönderildi-güç kaybı yazıyorsa
    elektrik gitmiştir. Fişi prize taktıktan sonra terminalde e-posta gönderildi-güç geri geldi yazıyorsa
    elektrik gelmiştir. Testi bu şekilde yapabilirsiniz.
    
    KOCAMAN NOT: En ama en ama en önemlisi mail adresinizin çift taraflı doğrulama sistemini kapatıp, tekrar
    açıp hemen altta bulunan app password kısmından kullanacağınız uygulamalar ile ilgili şifre oluşturmalısınız.
    Bu şifre ile kod satırında yer alan e-posta değişkenleri kısmındaki GMAIL_PASSWORD kısmına yazınız. 
    Bu bölüm atlanmamalıdır.
                                  
'''
import RPi.GPIO as GPIO
import smtplib
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(14, GPIO.BOTH, bouncetime=200)

# E-posta değişkenleri
SMTP_SERVER = 'smtp.gmail.com'  # E-posta sunucusu
SMTP_PORT = 587  # Sunucu portu
GMAIL_USERNAME = 'hueeneurolab@gmail.com'
GMAIL_PASSWORD = 'wtxulrdorzrthkts'
RECIPIENTS = ['tanercetin0420@gmail.com', 'onurcanyilmaz@gmail.com', 'orhunkoc0@gmail.com','ibisoglufatmagul@gmail.com','demirel.alp@gmail.com','eminyusufaydin@gmail.com','uyanikismail@gmail.com','merveteoman123456@gmail.com']  # E-posta alıcıları

class Emailer:
    def sendmail(self, recipient, subject, content):
        # E-posta başlıklarını oluşturun
        headers = [
            "From: " + GMAIL_USERNAME,
            "To: " + recipient,
            "Subject: " + subject,
            "MIME-Version: 1.0",
            "Content-Type: text/html; charset=utf-8"  # Charset'i UTF-8 olarak ayarlayın
        ]
        headers = "\r\n".join(headers)

        # Gmail sunucusuna bağlanın
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.starttls()
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        # E-postayı gönderin ve oturumu kapatın
        session.sendmail(GMAIL_USERNAME, recipient, (headers + "\r\n\r\n" + content).encode('utf-8'))  # İçeriği UTF-8 olarak kodlayın
        session.quit()

sender = Emailer()

power_loss = False  # Güç kaybı durumu

while True:
    if GPIO.event_detected(14):
        if GPIO.input(14):  # Güç kaybı
            if not power_loss:
                for recipient in RECIPIENTS:
                    emailSubject = "Güç kaybı tespit edildi!"
                    emailContent = "Güç kaybı tespit edildi: " + time.ctime()
                    sender.sendmail(recipient, emailSubject, emailContent)
                print("E-posta gönderildi - Güç kaybı")
                power_loss = True
        else:  # Güç geri geldi
            if power_loss:
                for recipient in RECIPIENTS:
                    emailSubject = "Güç geri geldi!"
                    emailContent = "Güç geri geldi: " + time.ctime()
                    sender.sendmail(recipient, emailSubject, emailContent)
                print("E-posta gönderildi - Güç geri geldi")
                power_loss = False

    time.sleep(0.1)
