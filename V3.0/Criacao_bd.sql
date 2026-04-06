CREATE DATABASE IF NOT EXISTS agenda_db;

USE agenda_db;


-- Criar a tabela de tarefas

CREATE TABLE IF NOT EXISTS tarefas(
	id INT AUTO_INCREMENT PRIMARY KEY,
    acao VARCHAR(100) NOT NULL,
    data_tarefa VARCHAR(10) NOT NULL,
    hora_tarefa VARCHAR(5) NOT NULL,
    status ENUM('Pendente', 'Em andamento','Concluída') DEFAULT 'Pendente',
	data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);
show tables;
select * from tarefas;

