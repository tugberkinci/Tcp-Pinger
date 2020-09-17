# Tcp-Pinger


Öncelikle server.py dosyasını çalıştınız.
Ardından client.py dosyasını çalıştırınız.

Client.py dosyası server.py dosyasına targethost.txt dosyasında bulunan ip adreslerine göre, her ip adresi için beş defa olmak üzere ping mesajı gönderir ve pong mesajı bekler.Dosyaya erişim sağlanamaz ise kullanıcıya dosyaya erişim sağlanamadığına dair bir mesaj verilir.
Client ping mesajı gönderirken server bir saniye içinde yanıt vermez ise istek timeout olur.Kullanıcıya isteğin timeout olduğu bilgisi verilir ve client bir sonraki adıma geçer.Her adım için ekrana gönderme süresi, saniye cinsinden ve RTT süresi, milisaniye cinsinden yazdırılmıştır.Program ,döngüsünü tamamladıktan sonra kullanıcıdan çıkış girdisi beklemektedir.Bu girdi girilene kadar program çalışmaya devam eder.
