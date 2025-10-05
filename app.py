"""
MAHESSA TRANS - Website Rental Mobil
Struktur Project:
mahessa-trans/
├── app.py (file ini)
├── templates/
│   └── index.html (file single page)
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── main.js
    └── img/
        └── (gambar mobil)
"""

# ========== app.py ==========
from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)

# Data mobil sesuai dengan gambar yang diberikan - DIPISAH PER MOBIL
MOBIL_DATA = [
    {
        'id': 1,
        'nama': 'Toyota Agya',
        'kategori': 'City Car',
        'tahun': 2023,
        'transmisi': 'Automatic',
        'kapasitas': 5,
        'bahan_bakar': 'Bensin',
        'fitur': ['AC', 'Audio', 'Power Steering', 'Central Lock'],
        'harga_lepas_kunci_12': 350000,
        'harga_lepas_kunci_24': 350000,
        'harga_driver_dalam': 450000,
        'harga_driver_luar': 550000,
        'deskripsi': 'Mobil city car ekonomis dengan transmisi automatic, cocok untuk perjalanan dalam kota.',
        'foto': 'toyota_agya.jpg'
    },
    {
        'id': 2,
        'nama': 'Honda Brio',
        'kategori': 'City Car',
        'tahun': 2023,
        'transmisi': 'Automatic',
        'kapasitas': 5,
        'bahan_bakar': 'Bensin',
        'fitur': ['AC', 'Audio', 'Power Steering', 'Central Lock'],
        'harga_lepas_kunci_12': 350000,
        'harga_lepas_kunci_24': 350000,
        'harga_driver_dalam': 450000,
        'harga_driver_luar': 550000,
        'deskripsi': 'City car compact dengan desain modern dan efisiensi bahan bakar optimal.',
        'foto': 'honda_brio.jpg'
    },
    {
        'id': 3,
        'nama': 'Daihatsu Sirion',
        'kategori': 'City Car',
        'tahun': 2023,
        'transmisi': 'Automatic',
        'kapasitas': 5,
        'bahan_bakar': 'Bensin',
        'fitur': ['AC', 'Audio', 'Power Steering', 'Central Lock'],
        'harga_lepas_kunci_12': 350000,
        'harga_lepas_kunci_24': 350000,
        'harga_driver_dalam': 450000,
        'harga_driver_luar': 550000,
        'deskripsi': 'Mobil city car dengan performa responsif dan irit bahan bakar.',
        'foto': 'daihatsu_sirion.jpg'
    },
    {
        'id': 4,
        'nama': 'Honda City Hatchback',
        'kategori': 'City Car',
        'tahun': 2023,
        'transmisi': 'Automatic',
        'kapasitas': 5,
        'bahan_bakar': 'Bensin',
        'fitur': ['AC', 'Audio Premium', 'Magic Seat', 'Rear Camera'],
        'harga_lepas_kunci_12': 500000,
        'harga_lepas_kunci_24': 500000,
        'harga_driver_dalam': 600000,
        'harga_driver_luar': 700000,
        'deskripsi': 'Hatchback premium dengan desain sporty dan fitur lengkap untuk kenyamanan berkendara.',
        'foto': 'honda_city_hatchback.jpg'
    },
    {
        'id': 5,
        'nama': 'Honda Jazz',
        'kategori': 'City Car',
        'tahun': 2023,
        'transmisi': 'Automatic',
        'kapasitas': 5,
        'bahan_bakar': 'Bensin',
        'fitur': ['AC', 'Audio Premium', 'Magic Seat', 'Rear Camera'],
        'harga_lepas_kunci_12': 500000,
        'harga_lepas_kunci_24': 500000,
        'harga_driver_dalam': 600000,
        'harga_driver_luar': 700000,
        'deskripsi': 'MPV compact dengan magic seat yang fleksibel untuk berbagai kebutuhan.',
        'foto': 'honda_jazz.jpg'
    },
    {
        'id': 6,
        'nama': 'Honda HR-V SE Panoramic',
        'kategori': 'SUV',
        'tahun': 2024,
        'transmisi': 'Automatic',
        'kapasitas': 5,
        'bahan_bakar': 'Bensin',
        'fitur': ['Panoramic Roof', 'AC Dual Zone', 'Touchscreen', 'Safety System'],
        'harga_lepas_kunci_12': 750000,
        'harga_lepas_kunci_24': 750000,
        'harga_driver_dalam': 850000,
        'harga_driver_luar': 950000,
        'deskripsi': 'SUV compact dengan panoramic roof dan fitur keselamatan lengkap.',
        'foto': 'honda_hrv.jpg'
    },
    {
        'id': 7,
        'nama': 'Toyota Rush',
        'kategori': 'SUV',
        'tahun': 2023,
        'transmisi': 'Automatic',
        'kapasitas': 7,
        'bahan_bakar': 'Bensin',
        'fitur': ['AC', 'Audio', '7-Seater', 'High Ground Clearance'],
        'harga_lepas_kunci_12': 400000,
        'harga_lepas_kunci_24': 400000,
        'harga_driver_dalam': 500000,
        'harga_driver_luar': 600000,
        'deskripsi': 'SUV tangguh dengan kapasitas 7 penumpang, cocok untuk keluarga dan berbagai medan.',
        'foto': 'toyota_rush.jpg'
    },
    {
        'id': 8,
        'nama': 'Toyota New Avanza',
        'kategori': 'MPV',
        'tahun': 2024,
        'transmisi': 'Automatic',
        'kapasitas': 7,
        'bahan_bakar': 'Bensin',
        'fitur': ['AC', 'Audio', '7-Seater', 'Power Window'],
        'harga_lepas_kunci_12': 450000,
        'harga_lepas_kunci_24': 450000,
        'harga_driver_dalam': 550000,
        'harga_driver_luar': 650000,
        'deskripsi': 'MPV keluarga dengan desain modern dan kapasitas 7 penumpang yang nyaman.',
        'foto': 'toyota_avanza.jpg'
    },
    {
        'id': 9,
        'nama': 'Mitsubishi Xpander',
        'kategori': 'MPV',
        'tahun': 2024,
        'transmisi': 'Automatic',
        'kapasitas': 7,
        'bahan_bakar': 'Bensin',
        'fitur': ['AC', 'Audio', '7-Seater', 'Power Window'],
        'harga_lepas_kunci_12': 450000,
        'harga_lepas_kunci_24': 450000,
        'harga_driver_dalam': 550000,
        'harga_driver_luar': 650000,
        'deskripsi': 'MPV dengan desain dinamis dan kabin luas untuk kenyamanan keluarga.',
        'foto': 'mitsubishi_xpander.jpg'
    },
    {
        'id': 10,
        'nama': 'Toyota Innova Reborn 2.4',
        'kategori': 'MPV',
        'tahun': 2023,
        'transmisi': 'Automatic',
        'kapasitas': 7,
        'bahan_bakar': 'Diesel',
        'fitur': ['AC', 'Audio Premium', 'Leather Seat', 'Rear Camera'],
        'harga_lepas_kunci_12': 600000,
        'harga_lepas_kunci_24': 600000,
        'harga_driver_dalam': 700000,
        'harga_driver_luar': 800000,
        'deskripsi': 'Innova Reborn dengan mesin diesel 2.4 yang bertenaga dan irit.',
        'foto': 'toyota_innova.jpg'
    },
    {
        'id': 11,
        'nama': 'Toyota Zenix Hybrid G',
        'kategori': 'MPV',
        'tahun': 2024,
        'transmisi': 'Automatic',
        'kapasitas': 7,
        'bahan_bakar': 'Hybrid',
        'fitur': ['Hybrid Engine', 'AC Dual Zone', 'Premium Audio', 'Smart Key'],
        'harga_lepas_kunci_12': 850000,
        'harga_lepas_kunci_24': 850000,
        'harga_driver_dalam': 950000,
        'harga_driver_luar': 1050000,
        'deskripsi': 'MPV hybrid premium dengan teknologi terbaru dan efisiensi bahan bakar optimal.',
        'foto': 'toyota_zenix_hybrid_g.jpg'
    },
    {
        'id': 12,
        'nama': 'Toyota Zenix Hybrid Q',
        'kategori': 'MPV',
        'tahun': 2024,
        'transmisi': 'Automatic',
        'kapasitas': 7,
        'bahan_bakar': 'Hybrid',
        'fitur': ['Hybrid Engine', 'AC Dual Zone', 'Premium Audio', 'Smart Key', 'Leather Seat'],
        'harga_lepas_kunci_12': 1000000,
        'harga_lepas_kunci_24': 1000000,
        'harga_driver_dalam': 1100000,
        'harga_driver_luar': 1200000,
        'deskripsi': 'MPV hybrid varian tertinggi dengan fitur premium dan kenyamanan maksimal.',
        'foto': 'toyota_zenix_hybrid_q.jpg'
    },
    {
        'id': 13,
        'nama': 'Toyota Fortuner GR',
        'kategori': 'SUV',
        'tahun': 2024,
        'transmisi': 'Automatic',
        'kapasitas': 7,
        'bahan_bakar': 'Diesel',
        'fitur': ['GR Sport Package', '4WD', 'Leather Seat', 'Premium Audio'],
        'harga_lepas_kunci_12': 1200000,
        'harga_lepas_kunci_24': 1200000,
        'harga_driver_dalam': 1300000,
        'harga_driver_luar': 1400000,
        'deskripsi': 'SUV premium dengan paket GR Sport dan performa tangguh untuk perjalanan eksekutif.',
        'foto': 'toyota_fortuner.jpg'
    },
    {
        'id': 14,
        'nama': 'Mitsubishi Pajero Sport',
        'kategori': 'SUV',
        'tahun': 2024,
        'transmisi': 'Automatic',
        'kapasitas': 7,
        'bahan_bakar': 'Diesel',
        'fitur': ['4WD', 'Leather Seat', 'Premium Audio', 'Safety System'],
        'harga_lepas_kunci_12': 1200000,
        'harga_lepas_kunci_24': 1200000,
        'harga_driver_dalam': 1300000,
        'harga_driver_luar': 1400000,
        'deskripsi': 'SUV legendaris dengan kemampuan off-road dan kenyamanan premium.',
        'foto': 'mitsubishi_pajero.jpg'
    },
    {
        'id': 15,
        'nama': 'Toyota Camry Hybrid',
        'kategori': 'Sedan',
        'tahun': 2024,
        'transmisi': 'Automatic',
        'kapasitas': 5,
        'bahan_bakar': 'Hybrid',
        'fitur': ['Hybrid Engine', 'Leather Seat', 'Premium Audio', 'Sunroof'],
        'harga_lepas_kunci_12': 1800000,
        'harga_lepas_kunci_24': 1800000,
        'harga_driver_dalam': 1900000,
        'harga_driver_luar': 2000000,
        'deskripsi': 'Sedan executive hybrid dengan kenyamanan dan efisiensi bahan bakar terbaik.',
        'foto': 'toyota_camry.jpg'
    },
    {
        'id': 16,
        'nama': 'Mercedes-Benz',
        'kategori': 'Luxury',
        'tahun': 2024,
        'transmisi': 'Automatic',
        'kapasitas': 5,
        'bahan_bakar': 'Bensin',
        'fitur': ['Premium Interior', 'Advanced Safety', 'Entertainment System', 'Panoramic Roof'],
        'harga_lepas_kunci_12': 1800000,
        'harga_lepas_kunci_24': 1800000,
        'harga_driver_dalam': 1900000,
        'harga_driver_luar': 2000000,
        'deskripsi': 'Mobil luxury dengan fitur premium dan kenyamanan maksimal untuk perjalanan eksekutif.',
        'foto': 'mercedes_benz.jpg'
    },
    {
        'id': 17,
        'nama': 'Toyota Alphard Transformer',
        'kategori': 'MPV Luxury',
        'tahun': 2024,
        'transmisi': 'Automatic',
        'kapasitas': 7,
        'bahan_bakar': 'Bensin',
        'fitur': ['Transformer Package', 'Leather Seat', 'Entertainment System', 'Premium Audio'],
        'harga_lepas_kunci_12': 2500000,
        'harga_lepas_kunci_24': 2500000,
        'harga_driver_dalam': 2600000,
        'harga_driver_luar': 2700000,
        'deskripsi': 'MPV luxury dengan paket transformer dan kenyamanan maksimal untuk perjalanan VIP.',
        'foto': 'toyota_alphard.jpg'
    }
]

def get_foto_url(mobil):
    """Helper function to get foto URL"""
    if mobil['foto'].startswith('http'):
        return mobil['foto']
    else:
        return url_for('static', filename=f"img/{mobil['foto']}")

@app.route('/')
def index():
    mobil_populer = MOBIL_DATA[:6]
    for mobil in mobil_populer:
        mobil['foto_url'] = get_foto_url(mobil)
    return render_template('index.html', mobil_populer=mobil_populer)

@app.route('/syarat')
def syarat():
    return render_template('syarat.html')

@app.route('/katalog')
def katalog():
    mobil_list = MOBIL_DATA.copy()
    for mobil in mobil_list:
        mobil['foto_url'] = get_foto_url(mobil)
    return render_template('katalog.html', mobil_list=mobil_list)

@app.route('/cara-sewa')
def cara_sewa():
    return render_template('cara_sewa.html')

@app.route('/kontak')
def kontak():
    return render_template('kontak.html')

@app.route('/mobil/<int:mobil_id>')
def detail_mobil(mobil_id):
    mobil = next((m for m in MOBIL_DATA if m['id'] == mobil_id), None)
    if mobil:
        mobil['foto_url'] = get_foto_url(mobil)
        return render_template('detail_mobil.html', mobil=mobil)
    return "Mobil tidak ditemukan", 404

# API untuk form kontak
@app.route('/api/kontak', methods=['POST'])
def api_kontak():
    data = request.json
    # Di sini Anda bisa menambahkan logika untuk mengirim email atau menyimpan ke database
    print(f"Pesan dari: {data.get('name')} - {data.get('email')}")
    print(f"Subjek: {data.get('subject')}")
    print(f"Pesan: {data.get('message')}")
    return jsonify({'status': 'success', 'message': 'Pesan berhasil dikirim'})

@app.route('/api/mobil')
def api_mobil():
    mobil_with_full_url = []
    for mobil in MOBIL_DATA:
        mobil_copy = mobil.copy()
        mobil_copy['foto_url'] = get_foto_url(mobil)
        mobil_with_full_url.append(mobil_copy)
    return jsonify(mobil_with_full_url)

@app.route('/api/mobil/<int:mobil_id>')
def api_detail_mobil(mobil_id):
    mobil = next((m for m in MOBIL_DATA if m['id'] == mobil_id), None)
    if mobil:
        mobil_copy = mobil.copy()
        mobil_copy['foto_url'] = get_foto_url(mobil)
        return jsonify(mobil_copy)
    return jsonify({'error': 'Mobil tidak ditemukan'}), 404

if __name__ == '__main__':
    app.run(debug=True)