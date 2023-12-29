CREATE DATABASE IF NOT EXISTS mydatabase;
USE mydatabase;

CREATE TABLE IF NOT EXISTS mytable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS usuarios (
    nome VARCHAR(20) NOT NULL PRIMARY KEY,
    senha VARCHAR(8) NOT NULL
);

CREATE TABLE IF NOT EXISTS jogos (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    console VARCHAR(50) NOT NULL
);

INSERT INTO usuarios (nome, senha) VALUES
    ('gabriel','123'),
    ('bubiz','1234');

INSERT INTO jogos (nome, categoria, console) VALUES
('Tetris','Puzzle', 'SNES'),
('Dota2','MMORPG', 'Desktop'),
('God of War','Aventura', 'PS2');