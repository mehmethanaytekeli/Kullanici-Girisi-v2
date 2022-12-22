print("""**********************
Kullanıcı Girişi
**********************""")

sys_kullanıcıadı ="polohan"
sys_kullanıcıparola ="12345"
giriş_hakkı = 3

while True :

   kullanıcı_adı = input("Kullanıcı Adınızı Giriniz :")
   kullanıcı_parola = input("Kullanıcı Parolasını Giriniz :")

   if (kullanıcı_adı == sys_kullanıcıadı and sys_kullanıcıparola != kullanıcı_parola):
        print("Parola Yanlış")
        giriş_hakkı -=1
        print("Giriş Hakkınız:",giriş_hakkı)
   elif (kullanıcı_adı != sys_kullanıcıadı and sys_kullanıcıparola == kullanıcı_parola):
        print("Kullanıcı Adı Yanlış")
        giriş_hakkı -= 1
        print("Giriş Hakkınız:", giriş_hakkı)

   elif (kullanıcı_adı != sys_kullanıcıadı and sys_kullanıcıparola != kullanıcı_parola):
        print("Kullanıcı Adı Yanlış Ve Parola Yanlış")
        giriş_hakkı -= 1
        print("Giriş Hakkınız:", giriş_hakkı)

   else :
        print("Giriş Başarılı")

        break

   if giriş_hakkı == 0 :
        print("Giriş Hakkınız Bitti")
        break