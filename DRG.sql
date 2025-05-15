CREATE DATABASE DRG;
USE DRG;

CREATE TABLE Supporter (
    id_supporter INT PRIMARY KEY,
    nama VARCHAR(50),
    email CHAR(50),
    alamat VARCHAR(75),
    tanggal_bergabung DATE
);

CREATE TABLE Struk_Langganan (
    id_supporter INT NOT NULL,
    id_tier INT NOT NULL,
    tanggal_mulai DATE,
    status VARCHAR(50),
    metode_pembayaran VARCHAR(50),
    jumlah INT NOT NULL,
    tanggal_pembayaran_terakhir DATE,
    CONSTRAINT fk_supporter FOREIGN KEY (id_supporter) REFERENCES Supporter(id_supporter)
        ON DELETE CASCADE
        ON UPDATE CASCADE
    CONSTRAINT fk_tier FOREIGN KEY (id_tier) REFERENCES tier(id_tier)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Tier (
    id_tier INT PRIMARY KEY,
     id_tier INT NOT NULL,
    nama_tier VARCHAR(75),
    deskripsi VARCHAR(75),
    harga INT NOT NULL,
    CONSTRAINT fk_creator FOREIGN KEY (id_creator) REFERENCES Creator(id_creator)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Creator (
    id_creator INT PRIMARY KEY,
    nama VARCHAR(50),
    email CHAR(50),
    bidang_kreasi VARCHAR(50),

    deskripsi VARCHAR(75),
    tanggal_bergabung DATE
);

CREATE TABLE Special_Content (
    id_supporter INT PRIMARY KEY,
    nama VARCHAR(50),
    email CHAR(50),
    alamat VARCHAR(75),
    tanggal_bergabung DATE
);

CREATE TABLE Komentar (
    id_supporter INT PRIMARY KEY,
    nama VARCHAR(50),
    email CHAR(50),
    alamat VARCHAR(75),
    tanggal_bergabung DATE
);

CREATE TABLE Konten (
    id_supporter INT PRIMARY KEY,
    nama VARCHAR(50),
    email CHAR(50),
    alamat VARCHAR(75),
    tanggal_bergabung DATE
);

CREATE TABLE Manfaat (
    id_supporter INT PRIMARY KEY,
    nama VARCHAR(50),
    email CHAR(50),
    alamat VARCHAR(75),
    tanggal_bergabung DATE
);

CREATE TABLE Publikasi (
    id_supporter INT PRIMARY KEY,
    nama VARCHAR(50),
    email CHAR(50),
    alamat VARCHAR(75),
    tanggal_bergabung DATE
);

CREATE TABLE Inspirasi(
    id_publikasi INT NOT NULL,
    id_merchandise INT NOT NULL,
    FOREIGN KEY (id_publikasi) REFERENCES Publikasi(id_publikasi)
    FOREIGN KEY (id_merchandise) REFERENCES Merchandise(id_merchandise)
);

CREATE TABLE Merchandise(
    id_merchandise INT PRIMARY KEY,
    nama VARCHAR(50),
    harga INT NOT NULL,
    stok INT NOT NULL,
    deskripsi VARCHAR(75)
);

CREATE TABLE Struk_Pembelian(
    id_supporter INT NOT NULL,
    id_merchandise INT NOT NULL,
    jumlah INT NOT NULL,
    tanggal_pembelian DATE,
    total_harga INT NOT NULL,
    metode_pembayaran VARCHAR(75),
    FOREIGN KEY (id_supporterr) REFERENCES Supporter(id_supporter)
    FOREIGN KEY (id_merchandise) REFERENCES Merchandise(id_merchandise)

);

CREATE TABLE Informasi_Hasil (
    id_gambar INT,
    id_special INT,
    status_pengerjaan VARCHAR(75),
    tanggal_penyelesaian DATE, 
    feedback VARCHAR(75)
    FOREIGN KEY (id_gambar) REFERENCES Gambar(id_gambar)
    FOREIGN KEY (id_special) REFERENCES Special_Content(id_special)
);

CREATE TABLE Gambar (
    id_gambar INT PRIMARY KEY,
    id_konten INT,
    format VARCHAR(75),
    resolusi VARCHAR(75), 
    FOREIGN KEY (id_konten) REFERENCES Konten(id_konten)
);

CREATE TABLE Teks (
    id_konten INT,
    jumlah_kata INT,
    format VARCHAR(75),
    FOREIGN KEY (id_konten) REFERENCES Konten(id_konten)
);

CREATE TABLE Video (
    id_konten INT,
    durasi TIME,
    resolusi VARCHAR(75),
    FOREIGN KEY (id_konten) REFERENCES Konten(id_konten)
);

CREATE TABLE Audio (
    id_konten INT,
    durasi TIME,
    kualitas VARCHAR(75) ,
    FOREIGN KEY (id_konten) REFERENCES Konten(id_konten)
);




