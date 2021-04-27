
#Author : Kgyya
#Github : github.com/Kgyya
#Join Us: t.me/tempat_config - t.me/bebas_berinternet


import os,sys,time
os.system("clear")
import requests
garis = 19*"="
banner = """╔╦╗╦╔╗╔╦ ╦╦ ╦╦═╗╦  
 ║ ║║║║╚╦╝║ ║╠╦╝║  
 ╩ ╩╝╚╝ ╩ ╚═╝╩╚═╩═╝"""
menu = ["Exit","Short URL","About Tools","More Tools"]
yametteh = []
def more():
  os.system("xdg-open https://github.com/Kgyya")
def about():
  if garis and banner != True:
      os.system("clear")
      print(garis)
      print(banner)
      print(garis)
  print("""Author : Kgyya
Github : github.com/Kgyya
Join Us: t.me/bebas_berinternet
         t.me/tempatconfig""")
  print(garis)
  print("\t>>>> Back To Menu <<<<")
  input()
  os.system("python "+sys.argv[0])
def url():
   if garis and banner != True:
      os.system("clear")
      print(garis)
      print(banner)
      print(garis)
   urr = input("Input Link/URL > ")
   r = requests.post("https://tinyurl.com/api-create.php?url="+urr)
   print(garis)
   time.sleep(2)
   print("Success > "+str(r.text))
def bikin():
   if garis and banner != True:
      print(garis)
      print(banner)
      print(garis)
   count = 0
   for menuu in menu:
      print(str(count)+") "+str(menuu))
      count += 1
      yametteh.append(menuu)
   print(garis)
   pilih = input("Pilih Menu > ")
   try:
      pil = yametteh[int(pilih) - 0]
   except (ValueError,IndexError):
      exit("pilih Nomor Nya Aja Bre..")
   if pil == "Exit":
      exit("Dhlh")
   elif pil == "Short URL":
      url()
   elif pil == "About Tools":
      about()
   elif pil == "More Tools":
      more()
if __name__ == "__main__":
   bikin()
