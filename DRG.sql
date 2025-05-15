DROP DATABASE IF EXISTS DRG;
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


