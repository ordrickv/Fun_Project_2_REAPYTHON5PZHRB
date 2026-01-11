# Fun_Project_2_REAPYTHON5PZHRB

AI Chatbot sederhana berbasis web menggunakan Streamlit dan OpenRouter API.  
Project ini dibuat sebagai tugas pengumpulan Web Academy.

## Deskripsi
Aplikasi ini memungkinkan pengguna melakukan percakapan dengan AI melalui antarmuka web sederhana. Riwayat chat disimpan selama sesi berjalan dan dapat dihapus kapan saja. API Key dikelola menggunakan environment variable untuk menjaga keamanan.

## Fitur
- Chat AI berbasis teks
- Riwayat percakapan per sesi
- Tombol hapus riwayat obrolan
- Penggunaan environment variable untuk API Key (aman untuk GitHub)

## Teknologi yang Digunakan
- Python
- Streamlit
- Requests
- OpenRouter API

## Cara Menjalankan Aplikasi

1. Clone repository ini
2. Masuk ke folder project
3. Buat file `.env` di folder yang sama dengan `app.py`
4. Isi file `.env` dengan format:
   ```
   OPENROUTER_API_KEY=API_KEY_KAMU
   ```
5. Install dependency:
   ```bash
   pip install streamlit requests python-dotenv
   ```
6. Jalankan aplikasi:
   ```bash
   streamlit run app.py
   ```

## Keamanan
- API Key tidak ditulis langsung di source code
- File `.env` tidak di-upload ke GitHub
- Konfigurasi mengikuti praktik standar pengembangan aplikasi

## Author
Nama: Ordrick Valencio
