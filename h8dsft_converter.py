#fungsi untuk hitung celcius ke farenheit
##parameter angka digunakan untuk hitungan hasil perubahan celcius ke farenheit
def ubahC2K(angka=0):
  hasil = int(round((9 * angka) / 5 + 32))
  return hasil
#fungsi untuk hitung farenheit ke celcius
##parameter angka digunakan untuk hitungan hasil perubahan farenheit ke celcius
def ubahK2C(angka=0):
  hasil = int(round((angka - 32) * 5 / 9))
  return hasil

#fungsi untuk cek mode adalah farenheit atau celcius dan input mode dilower case agar tidak case sensitive
##apabila celcius maka jalankan fungsi ubah C2K dan sebaliknya
###cek kondisi dengan else apabila kondisi mode tidak dipenuhi akan end
def ubahTemp(angka2=0,mode="farenheit"):
  if mode.lower()=="celcius":
    return f"hasil konversi dari {angka2} celcius adalah {ubahC2K(angka=angka2)} farenheit "
  elif mode.lower()=="farenheit":
    return f"hasil konversi dari {angka2} farenheit adalah {ubahK2C(angka=angka2)} celcius" 
    print("masukin celcius/ farenheit")
ubahTemp(mode="farenheit")
