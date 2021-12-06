

print(" -- > Bayburt Usulu Yemek Tarifleri<-- ")



yemekkayıt = open("yemektarifleri.txt", "w") 
yemekkayıt.write(input("Yemek Adı Giriniz = " )) 
yemekkayıt.write(input("Yemek Tarifi Giriniz = " ))
yemekkayıt.close()

dosya = open("yemektarifleri.txt","r")
oku = dosya.read()
print("Yemek Adı ve Tarifiniz = " ,oku)