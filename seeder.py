import random
from faker import Faker
from datetime import datetime, timedelta

# --- START OF DDL ---
DDL_STATEMENTS = """DROP DATABASE IF EXISTS DRG;
CREATE DATABASE DRG;
USE DRG;

CREATE TABLE Supporter (
    id_supporter INT PRIMARY KEY,
    nama VARCHAR(100),
    email VARCHAR(255),
    alamat VARCHAR(255),
    tanggal_bergabung DATE
);

CREATE TABLE Creator (
    id_creator INT PRIMARY KEY,
    nama VARCHAR(100),
    email VARCHAR(255),
    bidang_kreasi VARCHAR(100),
    deskripsi TEXT,
    tanggal_bergabung DATE
);

CREATE TABLE Tier (
    id_tier INT PRIMARY KEY,
    id_creator INT NOT NULL,
    nama_tier VARCHAR(100),
    deskripsi TEXT,
    harga INT NOT NULL,
    CONSTRAINT fk_creator_tier FOREIGN KEY (id_creator) REFERENCES Creator(id_creator)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Struk_Langganan (
    id_supporter INT NOT NULL,
    id_tier INT NOT NULL,
    tanggal_mulai DATE,
    status VARCHAR(50),
    metode_pembayaran VARCHAR(50),
    jumlah INT NOT NULL,
    tanggal_pembayaran_terakhir DATE,
    FOREIGN KEY (id_supporter) REFERENCES Supporter(id_supporter)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_tier) REFERENCES Tier(id_tier)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Konten (
    id_konten INT PRIMARY KEY,
    nama_bidang VARCHAR(100),
    judul VARCHAR(255),
    deskripsi TEXT,
    tanggal_publikasi DATE,
    jenis VARCHAR(75)
);

CREATE TABLE Special_Content (
    id_spesial INT PRIMARY KEY,
    id_supporter INT NOT NULL,
    id_creator INT,
    judul VARCHAR(255),
    deskripsi TEXT,
    harga_dasar INT,
    tanggal_batas_revisi DATE,
    batas_waktu_pengerjaan DATE,
    FOREIGN KEY (id_creator) REFERENCES Creator(id_creator)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_supporter) REFERENCES Supporter(id_supporter)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Komentar (
    id_komentar INT PRIMARY KEY,
    id_supporter INT NOT NULL,
    id_konten INT NOT NULL,
    waktu TIMESTAMP,
    isi_komentar TEXT,
    FOREIGN KEY (id_supporter) REFERENCES Supporter(id_supporter)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_konten) REFERENCES Konten(id_konten)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Manfaat (
    id_tier INT NOT NULL,
    id_konten INT NOT NULL,
    FOREIGN KEY (id_tier) REFERENCES Tier(id_tier)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_konten) REFERENCES Konten(id_konten)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Publikasi (
    id_publikasi INT PRIMARY KEY,
    id_creator INT NOT NULL,
    id_konten INT NOT NULL,
    FOREIGN KEY (id_creator) REFERENCES Creator(id_creator)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_konten) REFERENCES Konten(id_konten)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Merchandise (
    id_merchandise INT PRIMARY KEY,
    nama VARCHAR(100),
    harga INT NOT NULL,
    stok INT NOT NULL,
    deskripsi TEXT
);

CREATE TABLE Inspirasi (
    id_publikasi INT NOT NULL,
    id_merchandise INT NOT NULL,
    FOREIGN KEY (id_publikasi) REFERENCES Publikasi(id_publikasi)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_merchandise) REFERENCES Merchandise(id_merchandise)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Struk_Pembelian (
    id_supporter INT NOT NULL,
    id_merchandise INT NOT NULL,
    jumlah INT NOT NULL,
    tanggal_pembelian DATE,
    total_harga INT NOT NULL,
    metode_pembayaran VARCHAR(75),
    FOREIGN KEY (id_supporter) REFERENCES Supporter(id_supporter)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_merchandise) REFERENCES Merchandise(id_merchandise)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Gambar (
    id_gambar INT PRIMARY KEY,
    id_konten INT NOT NULL,
    format VARCHAR(50),
    resolusi VARCHAR(50),
    FOREIGN KEY (id_konten) REFERENCES Konten(id_konten)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Informasi_Hasil (
    id_gambar INT NOT NULL,
    id_spesial INT NOT NULL,
    status_pengerjaan VARCHAR(75),
    tanggal_penyelesaian DATE,
    feedback TEXT,
    FOREIGN KEY (id_gambar) REFERENCES Gambar(id_gambar)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_spesial) REFERENCES Special_Content(id_spesial)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Teks (
    id_konten INT NOT NULL,
    jumlah_kata INT NOT NULL,
    format VARCHAR(50),
    FOREIGN KEY (id_konten) REFERENCES Konten(id_konten)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Video (
    id_konten INT NOT NULL,
    durasi TIME,
    resolusi VARCHAR(50),
    FOREIGN KEY (id_konten) REFERENCES Konten(id_konten)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Audio (
    id_konten INT NOT NULL,
    durasi TIME,
    kualitas VARCHAR(75),
    FOREIGN KEY (id_konten) REFERENCES Konten(id_konten)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
"""
# --- END OF DDL ---

# Print the DDL statements first
print(DDL_STATEMENTS)

fake = Faker('id_ID')

NUM_SUPPORTERS = 100
NUM_CREATORS = 100
NUM_TIERS = 100
NUM_KONTEN = 100
NUM_MERCHANDISE = 100
NUM_SPECIAL_CONTENT = 100
NUM_KOMENTAR_MAX_PER_KONTEN = 100
NUM_STRUK_LANGGANAN = 100
NUM_STRUK_PEMBELIAN = 100
NUM_MANFAAT_MAX_PER_TIER = 100
NUM_INSPIRASI_MAX_PER_PUBLIKASI = 100
NUM_INFORMASI_HASIL_MAX_PER_SPECIAL_CONTENT = 100

supporter_ids = list(range(1, NUM_SUPPORTERS + 1))
creator_ids = list(range(1, NUM_CREATORS + 1))
tier_ids = list(range(1, NUM_TIERS + 1))
konten_ids = list(range(1, NUM_KONTEN + 1))
merchandise_ids = list(range(1, NUM_MERCHANDISE + 1))
special_content_ids = list(range(1, NUM_SPECIAL_CONTENT + 1))

publikasi_ids_map = {}
publikasi_counter = 1
gambar_ids_map = {}
gambar_counter = 1
komentar_counter = 1
current_publikasi_ids = []
current_gambar_ids = []

def sql_date(dt_object):
    if dt_object is None:
        return "NULL"
    return f"'{dt_object.strftime('%Y-%m-%d')}'"

def sql_timestamp(dt_object):
    if dt_object is None:
        return "NULL"
    return f"'{dt_object.strftime('%Y-%m-%d %H:%M:%S')}'"

def sql_time(t_object):
    if t_object is None:
        return "NULL"
    return f"'{t_object.strftime('%H:%M:%S')}'"

def sql_string(s):
    if s is None:
        return "NULL"
    s_escaped = str(s).replace("'", "''")
    return f"'{s_escaped}'"

for i in supporter_ids:
    nama = fake.name()
    email = fake.email()
    alamat = fake.address().replace('\n', ', ')
    tanggal_bergabung = fake.date_between(start_date='-3y', end_date='-1y')
    print(f"INSERT INTO Supporter (id_supporter, nama, email, alamat, tanggal_bergabung) VALUES ({i}, {sql_string(nama)}, {sql_string(email)}, {sql_string(alamat)}, {sql_date(tanggal_bergabung)});")

bidang_kreasi_options = ['Seni Digital', 'Musik Akustik', 'Podcast Komedi', 'Tutorial Masak', 'Review Teknologi', 'Animasi Pendek']
for i in creator_ids:
    nama = fake.name()
    email = fake.unique.email()
    bidang_kreasi = random.choice(bidang_kreasi_options)
    deskripsi = fake.paragraph(nb_sentences=3)
    tanggal_bergabung = fake.date_between(start_date='-4y', end_date='-2y')
    print(f"INSERT INTO Creator (id_creator, nama, email, bidang_kreasi, deskripsi, tanggal_bergabung) VALUES ({i}, {sql_string(nama)}, {sql_string(email)}, {sql_string(bidang_kreasi)}, {sql_string(deskripsi)}, {sql_date(tanggal_bergabung)});")

nama_tier_options = ['Pemula', 'Pendukung', 'Loyalis', 'Sponsor', 'Patron Utama']
generated_tiers_data = []
for i in tier_ids:
    id_creator = random.choice(creator_ids)
    nama_tier = f"{random.choice(nama_tier_options)} {fake.word().capitalize()}"
    deskripsi = fake.sentence(nb_words=10)
    harga = random.randint(1, 200) * 5000
    generated_tiers_data.append({'id_tier': i, 'harga': harga})
    print(f"INSERT INTO Tier (id_tier, id_creator, nama_tier, deskripsi, harga) VALUES ({i}, {id_creator}, {sql_string(nama_tier)}, {sql_string(deskripsi)}, {harga});")

jenis_konten_options = ['Teks', 'Video', 'Audio', 'Gambar']
for i in konten_ids:
    nama_bidang = fake.bs()
    judul = fake.sentence(nb_words=6)[:-1]
    deskripsi_konten = fake.paragraph(nb_sentences=2)
    tanggal_publikasi = fake.date_between(start_date='-2y', end_date='today')
    jenis = random.choice(jenis_konten_options)
    print(f"INSERT INTO Konten (id_konten, nama_bidang, judul, deskripsi, tanggal_publikasi, jenis) VALUES ({i}, {sql_string(nama_bidang)}, {sql_string(judul)}, {sql_string(deskripsi_konten)}, {sql_date(tanggal_publikasi)}, {sql_string(jenis)});")

    if jenis == 'Teks':
        jumlah_kata = random.randint(300, 2000)
        format_teks = random.choice(['.txt', '.md', '.pdf'])
        print(f"INSERT INTO Teks (id_konten, jumlah_kata, format) VALUES ({i}, {jumlah_kata}, {sql_string(format_teks)});")
    elif jenis == 'Video':
        durasi_video_seconds = random.randint(60, 3600)
        durasi_video_str = str(timedelta(seconds=durasi_video_seconds))
        resolusi_video = random.choice(['720p', '1080p', '4K'])
        print(f"INSERT INTO Video (id_konten, durasi, resolusi) VALUES ({i}, {sql_time(datetime.strptime(durasi_video_str, '%H:%M:%S').time())}, {sql_string(resolusi_video)});")
    elif jenis == 'Audio':
        durasi_audio_seconds = random.randint(60, 7200)
        durasi_audio_str = str(timedelta(seconds=durasi_audio_seconds))
        kualitas_audio = random.choice(['128kbps', '256kbps', '320kbps', 'Lossless'])
        print(f"INSERT INTO Audio (id_konten, durasi, kualitas) VALUES ({i}, {sql_time(datetime.strptime(durasi_audio_str, '%H:%M:%S').time())}, {sql_string(kualitas_audio)});")

generated_merchandise_data = []
for i in merchandise_ids:
    nama_merch = f"{fake.word().capitalize()} {random.choice(['T-Shirt', 'Mug', 'Sticker Pack', 'Poster', 'Keychain'])}"
    harga_merch = random.randint(5, 50) * 10000
    stok = random.randint(0, 150)
    deskripsi_merch = fake.sentence(nb_words=8)
    generated_merchandise_data.append({'id_merchandise': i, 'harga': harga_merch})
    print(f"INSERT INTO Merchandise (id_merchandise, nama, harga, stok, deskripsi) VALUES ({i}, {sql_string(nama_merch)}, {harga_merch}, {stok}, {sql_string(deskripsi_merch)});")

for id_konten in konten_ids:
    if random.random() < 0.9:
        id_creator_publikasi = random.choice(creator_ids)
        print(f"INSERT INTO Publikasi (id_publikasi, id_creator, id_konten) VALUES ({publikasi_counter}, {id_creator_publikasi}, {id_konten});")
        publikasi_ids_map[id_konten] = publikasi_counter
        current_publikasi_ids.append(publikasi_counter)
        publikasi_counter += 1

for id_konten_gambar in konten_ids:
    if random.random() < 0.8:
        format_gambar = random.choice(['.jpg', '.png', '.gif', '.webp'])
        resolusi_gambar = random.choice(['640x480', '1280x720', '1920x1080', '2560x1440'])
        print(f"INSERT INTO Gambar (id_gambar, id_konten, format, resolusi) VALUES ({gambar_counter}, {id_konten_gambar}, {sql_string(format_gambar)}, {sql_string(resolusi_gambar)});")
        gambar_ids_map[id_konten_gambar] = gambar_counter
        current_gambar_ids.append(gambar_counter)
        gambar_counter += 1

for i in special_content_ids:
    id_supporter_sc = random.choice(supporter_ids)
    id_creator_sc = random.choice([None] + creator_ids)
    judul_sc = f"Request Khusus: {fake.catch_phrase()}"
    deskripsi_sc = fake.paragraph(nb_sentences=4)
    harga_dasar_sc = random.randint(10, 100) * 10000
    tgl_order = fake.date_between(start_date='-1y', end_date='-1m')
    tanggal_batas_revisi = tgl_order + timedelta(days=random.randint(14, 30))
    batas_waktu_pengerjaan = tgl_order + timedelta(days=random.randint(30, 90))
    print(f"INSERT INTO Special_Content (id_spesial, id_supporter, id_creator, judul, deskripsi, harga_dasar, tanggal_batas_revisi, batas_waktu_pengerjaan) VALUES ({i}, {id_supporter_sc}, {id_creator_sc if id_creator_sc else 'NULL'}, {sql_string(judul_sc)}, {sql_string(deskripsi_sc)}, {harga_dasar_sc}, {sql_date(tanggal_batas_revisi)}, {sql_date(batas_waktu_pengerjaan)});")

status_langganan_options = ['Aktif', 'Berakhir', 'Dibatalkan']
metode_pembayaran_options = ['Transfer Bank', 'Kartu Kredit', 'GoPay', 'OVO', 'Dana']
for _ in range(NUM_STRUK_LANGGANAN):
    if not supporter_ids or not tier_ids: continue
    id_supporter_sl = random.choice(supporter_ids)
    id_tier_sl = random.choice(tier_ids)
    tanggal_mulai = fake.date_between(start_date='-2y', end_date='-1m')
    status = random.choice(status_langganan_options)
    metode_pembayaran = random.choice(metode_pembayaran_options)
    
    harga_tier_dipilih = 0
    for tier_data in generated_tiers_data:
        if tier_data['id_tier'] == id_tier_sl:
            harga_tier_dipilih = tier_data['harga']
            break
    if harga_tier_dipilih == 0 : # Fallback jika tidak ketemu
        harga_tier_dipilih = random.randint(20000,1000000)

    tanggal_pembayaran_terakhir = None
    if status == 'Aktif':
        tanggal_pembayaran_terakhir = tanggal_mulai + timedelta(days=random.randint(0, 30))
    elif status == 'Berakhir':
         tanggal_pembayaran_terakhir = tanggal_mulai + timedelta(days=random.randint(0,25))

    print(f"INSERT INTO Struk_Langganan (id_supporter, id_tier, tanggal_mulai, status, metode_pembayaran, jumlah, tanggal_pembayaran_terakhir) VALUES ({id_supporter_sl}, {id_tier_sl}, {sql_date(tanggal_mulai)}, {sql_string(status)}, {sql_string(metode_pembayaran)}, {harga_tier_dipilih}, {sql_date(tanggal_pembayaran_terakhir)});")

for id_konten_komen in konten_ids:
    for _ in range(random.randint(0, NUM_KOMENTAR_MAX_PER_KONTEN)):
        if not supporter_ids: continue
        id_supporter_komen = random.choice(supporter_ids)
        waktu_komen = fake.date_time_between(start_date= (datetime.now() - timedelta(days=365)) , end_date='now')
        isi_komentar = fake.paragraph(nb_sentences=random.randint(1,3))
        print(f"INSERT INTO Komentar (id_komentar, id_supporter, id_konten, waktu, isi_komentar) VALUES ({komentar_counter}, {id_supporter_komen}, {id_konten_komen}, {sql_timestamp(waktu_komen)}, {sql_string(isi_komentar)});")
        komentar_counter += 1

manfaat_generated = set()
for id_tier_manfaat in tier_ids:
    for _ in range(random.randint(1, NUM_MANFAAT_MAX_PER_TIER)):
        if not konten_ids: continue
        id_konten_manfaat = random.choice(konten_ids)
        if (id_tier_manfaat, id_konten_manfaat) not in manfaat_generated:
            print(f"INSERT INTO Manfaat (id_tier, id_konten) VALUES ({id_tier_manfaat}, {id_konten_manfaat});")
            manfaat_generated.add((id_tier_manfaat, id_konten_manfaat))

inspirasi_generated = set()
if current_publikasi_ids and merchandise_ids:
    for id_publikasi_inspirasi in current_publikasi_ids:
        for _ in range(random.randint(0, NUM_INSPIRASI_MAX_PER_PUBLIKASI)):
            id_merch_inspirasi = random.choice(merchandise_ids)
            if (id_publikasi_inspirasi, id_merch_inspirasi) not in inspirasi_generated:
                print(f"INSERT INTO Inspirasi (id_publikasi, id_merchandise) VALUES ({id_publikasi_inspirasi}, {id_merch_inspirasi});")
                inspirasi_generated.add((id_publikasi_inspirasi, id_merch_inspirasi))

for _ in range(NUM_STRUK_PEMBELIAN):
    if not supporter_ids or not merchandise_ids: continue
    id_supporter_sp = random.choice(supporter_ids)
    id_merch_sp = random.choice(merchandise_ids)
    jumlah_beli = random.randint(1, 5)
    
    harga_merch_dipilih = 0
    for merch_data in generated_merchandise_data:
        if merch_data['id_merchandise'] == id_merch_sp:
            harga_merch_dipilih = merch_data['harga']
            break
    if harga_merch_dipilih == 0: # Fallback
        harga_merch_dipilih = random.randint(50000,200000)
    
    total_harga = jumlah_beli * harga_merch_dipilih
    tanggal_pembelian = fake.date_between(start_date='-1y', end_date='today')
    metode_pembayaran_sp = random.choice(metode_pembayaran_options)
    print(f"INSERT INTO Struk_Pembelian (id_supporter, id_merchandise, jumlah, tanggal_pembelian, total_harga, metode_pembayaran) VALUES ({id_supporter_sp}, {id_merch_sp}, {jumlah_beli}, {sql_date(tanggal_pembelian)}, {total_harga}, {sql_string(metode_pembayaran_sp)});")

status_pengerjaan_options = ['Dalam Proses', 'Revisi Diminta', 'Selesai', 'Menunggu Feedback']
if current_gambar_ids and special_content_ids:
    for id_sc_ih in special_content_ids:
        for _ in range(random.randint(0, NUM_INFORMASI_HASIL_MAX_PER_SPECIAL_CONTENT)):
            if not current_gambar_ids: break 
            id_gambar_ih = random.choice(current_gambar_ids)
            status_pengerjaan = random.choice(status_pengerjaan_options)
            tanggal_penyelesaian_ih = None
            if status_pengerjaan == 'Selesai':
                 tanggal_penyelesaian_ih = fake.date_between(start_date= (datetime.now() - timedelta(days=180)) , end_date='today')
            
            feedback = None
            if status_pengerjaan in ['Selesai', 'Revisi Diminta']:
                feedback = fake.sentence()
            
            print(f"INSERT INTO Informasi_Hasil (id_gambar, id_spesial, status_pengerjaan, tanggal_penyelesaian, feedback) VALUES ({id_gambar_ih}, {id_sc_ih}, {sql_string(status_pengerjaan)}, {sql_date(tanggal_penyelesaian_ih)}, {sql_string(feedback)});")
