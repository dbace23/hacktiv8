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
    print("hasil konversi dari", angka2,"celcius ke farenheit adalah")
    return ubahC2K(angka=angka2)
  elif mode.lower()=="farenheit":
    print("hasil konversi dari", angka2,"farenheit ke celcius adalah")
    return ubahK2C(angka=angka2)
  else:
    print("masukin celcius/ farenheit")
ubahTemp(mode="farenheit")
