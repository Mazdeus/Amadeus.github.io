#Import Modul
import datetime
import requests
from bs4 import BeautifulSoup
import json
import os
import subprocess

#Request ke website
page = requests.get('https://www.republika.co.id/')

#Extract konten menjadi objek BeautifulSoup
obj = BeautifulSoup(page.text, 'html.parser')

#Deklarasi List Kosong
data = []


headlines = obj.find_all('div', class_='main-content__left')
# Melakukan iterasi melalui setiap elemen yang ditemukan sebelumnya
for headline in headlines:
    # Mencari judul
    titles = headline.find_all('h3')
    # Mencari tanggal publikasi
    dates = headline.find_all('div', class_='date')
    # Mencari Kategori 
    kategori_elems = headline.find_all('span', class_='kanal-info')
    
    # Menggunakan fungsi zip untuk menggabungkan setiap judul, tanggal, dan kategori artikel menjadi satu
    for title, date_elem, kategori_elem in zip(titles, dates, kategori_elems):
        # Mengambil teks kategori dan membersihkannya dari spasi di awal dan akhir.
        kategori = kategori_elem.text.strip()
        # Mengambil teks waktu publikasi dan membersihkannya dari spasi di awal dan akhir.
        waktu_text = date_elem.text.strip()
        
        # Memeriksa apakah teks waktu mengandung ' - '
        if ' - ' in waktu_text:
            waktu = waktu_text.split(' - ')[1].strip()
            # Waktu ketika scraping dilakukan
            scraping_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Menambahkan sebuah dictionary yang berisi judul artikel, kategori, waktu publikasi, dan waktu scraping ke dalam list data.
            data.append({"judul": title.text.strip(), "kategori": kategori, "publish_time": waktu, "scraping_time": scraping_time})
    
# Mendapatkan jalur ke direktori saat ini
current_dir = os.path.dirname(os.path.realpath(__file__))

# menulis data ke dalam sebuah file dengan format JSON di direktori yang sama dengan file Python
with open(os.path.join(current_dir, 'headline.json'), 'w') as f:
    json.dump(data, f, indent=4)

# Mendefinisikan fungsi untuk melakukan commit dan push perubahan ke GitHub
def commit_and_push_changes():
    try:
        # Perintah Git untuk menambahkan semua perubahan
        subprocess.run(["git", "add", "."], check=True)
        # Perintah Git untuk melakukan commit dengan pesan "Update data"
        subprocess.run(["git", "commit", "-m", "Update data"], check=True)
        # Perintah Git untuk melakukan push ke branch saat ini
        subprocess.run(["git", "push"], check=True)
        print("Perubahan berhasil di-commit dan di-push ke GitHub")
    except subprocess.CalledProcessError as e:
        # Menangani kesalahan jika terjadi
        print("Terjadi kesalahan saat melakukan commit dan push perubahan:", e)

# Memanggil fungsi commit_and_push_changes setelah menulis data ke file JSON
commit_and_push_changes()