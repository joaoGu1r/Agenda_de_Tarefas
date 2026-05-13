

CREATE TABLE Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    -- Definindo o papel do usuário
    perfil ENUM('aluno', 'professor', 'admin') DEFAULT 'aluno',
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);