def print_grafik(nilai: int, keahlian: str):
  count = 0
  lebar_grafik = []
  while count < nilai/10:
    count += 1
    lebar_grafik.append("|")
    
  grafik = "".join(lebar_grafik)
  result = f"{keahlian}\t\t: {grafik} {nilai}%"
  return result

# i: variabel array keahlian
def run(i: [str]):
  count = 0
  while count < len(i):
    if i[count] == "golang":
      nilai = 30
      print(print_grafik(nilai, i[count]))
    elif i[count] == "python":
      nilai = 20
      print(print_grafik(nilai, i[count]))
    else:
      nilai = 80
      print(print_grafik(nilai, i[count]))
    count += 1