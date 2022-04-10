# Connect Database
import psycopg2
import os
DB_NAME = "Tugas"
DB_USER = "abdul"
DB_PASS = "123"
DB_HOST = "localhost"
DB_PORT = "5432"
try:
    db = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
    print("\nServer Telah Terkoneksi Di Database\n")
except:
    print("\nServer Belum Terkoneksi Di Database\n")
cur = db.cursor()

# Create Tabel
def create_tabel(db):
    cur.execute("""
                CREATE TABLE SMK
                (
                  Nik VARCHAR PRIMARY KEY NOT NULL,
                  Nama TEXT NOT NULL,
                  JenisKelamin TEXT NOT NULL,
                  Jurusan TEXT NOT NULL
                  )
                  """)
    db.commit()
    print("Selamat Anda Telah Berhasil Membuat Tabel...")

# Insert Data
def insert_data(db):
  Nik = input("\nMasukan Nik: ")
  Nama = input("Masukan Nama: ")
  JenisKelamin = input("Masukan Jenis Kelamin: ")
  Jurusan = input("Dari Jurusan Mana: ")
  val = (Nik, Nama, JenisKelamin, Jurusan)
  cursor = db.cursor()
  sql = "INSERT INTO SMK (Nik, Nama, JenisKelamin, Jurusan) VALUES (%s, %s, %s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} Selamat Data Telah Tersimpan".format(cursor.rowcount))
def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM SMK"
  cursor.execute(sql)
  results = cursor.fetchall()
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)

# Update Data
def update_data(db):
  cursor = db.cursor()
  show_data(db)
  Nik = input("\nPilih Nik> ")
  Nama = input("Nama baru: ")
  JenisKelamin = input("Masukan Jenis Kelamin: ")
  Jurusan = input("Dari Jurusan Mana: ")
  sql = "UPDATE SMK SET Nama=%s, JenisKelamin=%s, Jurusan=%s WHERE Nik=%s"
  val = (Nama, JenisKelamin, Jurusan, Nik)
  cursor.execute(sql, val)
  db.commit()
  print("{} Selamat Data Telah TerUpdate".format(cursor.rowcount))

# Hapus Data
def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  Nik = input("\nPilih Nik> ")
  sql = "DELETE FROM SMK WHERE Nik=%s"
  val = (Nik,)
  cursor.execute(sql, val)
  db.commit()
  print("{} Selamat Data Telah Terhapus".format(cursor.rowcount))

# Cari Data
def search_data(db):
  cursor = db.cursor()
  keyword = input("Kata kunci: ")
  sql = "SELECT * FROM SMK WHERE Nama LIKE %s OR Nik LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)

# Tampilkan Menu
def show_menu(db):
  print("\n=== CRUD PYTHON PORTGRES ===")
  print("1. Membuat Tabel Data SMK")
  print("2. Insert Data")
  print("3. Tampilkan Data")
  print("4. Update Data")
  print("5. Hapus Data")
  print("6. Cari Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")
  os.system("cls")
  if menu == "1":
    create_tabel(db)
  elif menu == "2":
    insert_data(db)
  elif menu == "3":
    show_data(db)
  elif menu == "4":
    update_data(db)
  elif menu == "5":
    delete_data(db)
  elif menu == "6":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")
if __name__ == "__main__":
  while(True):
    show_menu(db)