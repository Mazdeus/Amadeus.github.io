#Import Modul
import datetime
import requests
from bs4 import BeautifulSoup
import json

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
    
# menulis data ke dalam sebuah file dengan format JSON
with open('D:\\headline.json', 'w') as f:
    json.dump(data, f, indent=4) #data adalah sebuah list yang berisi dictionary-dictionary yang telah kita kumpulkan dari proses scraping sebelumnya. f adalah objek file tempat kita akan menulis data JSON. Sedangkan, indent=4 adalah Parameter yang memberi tahu fungsi json.dump untuk memberi indentasi sebanyak 4 spasi pada setiap tingkat dalam data JSON. Ini membuat struktur JSON menjadi lebih mudah dibaca ketika dibuka dengan editor teks.
    