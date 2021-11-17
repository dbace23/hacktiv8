list1 = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949]
print(list1)
pilihan=input("pilih tampil angka yang genap/ ganjil ")
while pilihan.lower() != "genap" and pilihan.lower() !="ganjil":
  pilihan=input("isi genap/ ganjil ")
if pilihan.lower() =="genap": 
  x=0
else:
  x=1

pilihanStop=input("pilih stop tampil angka di ")
while int(pilihanStop) not in list1:
  pilihanStop=input("pilih angka yang ada di list atas ")

for num in list1:
  if num %2 == x:
    print (num,end=" ")
  if num==int(pilihanStop):
    break
print("\nDone")
      