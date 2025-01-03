CREATE DATABASE IF NOT EXISTS chess_db;
-- GRANT ALL PRIVILEGES ON chess_db.* TO 'miquel'@'localhost';

USE chess_db;
-- Drop TABLE boards;
CREATE TABLE IF NOT EXISTS boards (
    id VARCHAR(64) PRIMARY KEY, -- hash de la pos, guardamos tablero como string?
    pos_value FLOAT,    -- el valor calculado en la pos actual
    best_move TEXT,     -- mejor movimiento desde el estado actual
    board_state TEXT,   -- estado actual representado en string
    turn INT            -- jugador que tiene que mover, 0=blanco, 1=negro
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;