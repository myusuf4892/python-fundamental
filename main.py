from var import *
from pkg import *
import subprocess

# instance
profil = entity.profil(
  nama="muhamad yusup",
  keahlian="golang, python, mysql",
  data=[])

# print out profil
print("nama\t\t: %s \nkeahlian\t: %s" % (profil.nama, profil.keahlian))

# split koma dan spasi
semua_keahlian = profil.keahlian.split(', ')
# extend data split
profil.data.extend(semua_keahlian)

# print grafik
print("grafik keahlian:")
grafik.run(profil.data)
print("\n")
link = "https://wa.me/082246068248"
print(f'<a href ="{link}">{link}</a>\n')
print(f"Click this URL or copy and paste it into your browser: {link}")

subprocess.run(["termux-open", link])

print("\n-------- Ping Host dengan Python ---------")    
host = input("\ninput host: ")

if __name__ == "__main__":
  result = ping.run(host)
  print(result)