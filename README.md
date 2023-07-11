# RESBI
UPS_RESBI_PROJECT
   1st -) ilk olarak raspberry pi bilgisayarımızı ethernet kablosu ile internete bağlıyoruz.
   2=> internetimizi statik olarak ayarlıyoruz.
   statik ip nasıl yapılır => a) Terminali aç
                              b) " sudo nano /etc/dhcpcd.conf " yaz enter'a bas.
                              c) Açılan konfigürasyon dosyasına aşağıdaki satrıları yaz;
                                          -> interface wlan0
                                          -> static_routers .../.../.../... not:(Bu kısım gateway olarak geçiyor.)
                                          -> static domain_name_servers .../.../.../...
                                          -> static ip_address .../.../.../...1
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
