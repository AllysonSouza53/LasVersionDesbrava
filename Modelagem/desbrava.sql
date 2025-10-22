CREATE DATABASE IF NOT EXISTS DESBRAVA;
USE DESBRAVA;

-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 22/10/2025 às 18:07
-- Versão do servidor: 9.1.0
-- Versão do PHP: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `desbrava`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `albuns`
--

DROP TABLE IF EXISTS `albuns`;
CREATE TABLE IF NOT EXISTS `albuns` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `NOME` varchar(255) NOT NULL,
  `USUARIO` varchar(255) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID` (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Despejando dados para a tabela `albuns`
--

INSERT INTO `albuns` (`ID`, `NOME`, `USUARIO`) VALUES
(8, 'Teste1', 'Teste1');

-- --------------------------------------------------------

--
-- Estrutura para tabela `alunos`
--

DROP TABLE IF EXISTS `alunos`;
CREATE TABLE IF NOT EXISTS `alunos` (
  `RE` int NOT NULL,
  `NOME` varchar(225) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `USUARIO` varchar(225) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `ESCOLA` varchar(225) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `DATANASCIMENTO` date NOT NULL,
  `GENERO` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `TURMA` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci,
  `PROFISSIONALRESPONSAVEL` char(11) NOT NULL,
  `UF` char(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `CIDADE` varchar(225) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `DIAGNOSTICO` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `OBSERVACOES` varchar(1000) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `NIVELDELEITURA` int DEFAULT NULL,
  `NIVELDEESCRITA` int DEFAULT NULL,
  PRIMARY KEY (`RE`),
  UNIQUE KEY `USUARIO` (`USUARIO`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Despejando dados para a tabela `alunos`
--

INSERT INTO `alunos` (`RE`, `NOME`, `USUARIO`, `ESCOLA`, `DATANASCIMENTO`, `GENERO`, `TURMA`, `PROFISSIONALRESPONSAVEL`, `UF`, `CIDADE`, `DIAGNOSTICO`, `OBSERVACOES`, `NIVELDELEITURA`, `NIVELDEESCRITA`) VALUES
(12345, 'João da Silva', 'joaosilva', 'Escola Municipal ABC', '2012-05-15', 'Masculino', '5A', '46502239897', 'SP', 'Campinas', 'Dislexia Leve', 'Observações fictícias sobre o aluno', 2, 1),
(1, '1', '11', 'ESC ALTINA MAGALHAES DA SILVA', '1111-11-11', '1', '1', '49069495090', 'AC', 'Acrelândia', '1', '1', 2, 2);

-- --------------------------------------------------------

--
-- Estrutura para tabela `comentarios`
--

DROP TABLE IF EXISTS `comentarios`;
CREATE TABLE IF NOT EXISTS `comentarios` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `USUARIO` varchar(255) NOT NULL,
  `IDPOST` int NOT NULL,
  `TEXTO` varchar(500) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Despejando dados para a tabela `comentarios`
--

INSERT INTO `comentarios` (`ID`, `USUARIO`, `IDPOST`, `TEXTO`) VALUES
(1, 'AllysonSouza', 1, 'Ola Brasil!!!!!'),
(2, 'AllysonSouza', 1, 'Foi mais um');

-- --------------------------------------------------------

--
-- Estrutura para tabela `dados_jogos`
--

DROP TABLE IF EXISTS `dados_jogos`;
CREATE TABLE IF NOT EXISTS `dados_jogos` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `ID_ALUNO` varchar(11) NOT NULL,
  `USUARIO_PROFISSIONAL` varchar(11) NOT NULL,
  `NOME_JOGO` int NOT NULL,
  `ID_NIVEL` int NOT NULL,
  `PONTUACAO` int DEFAULT '0',
  `PORCENTAGEM_COMPLETADA` decimal(5,2) DEFAULT '0.00',
  `TEMPO_GASTO` time DEFAULT '00:00:00',
  `ACERTOS` int DEFAULT '0',
  `ERROS` int DEFAULT '0',
  `TENTATIVAS` int DEFAULT '0',
  `DATA_REGISTRO` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `favoritos`
--

DROP TABLE IF EXISTS `favoritos`;
CREATE TABLE IF NOT EXISTS `favoritos` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `ID_POST` int NOT NULL,
  `USUARIO` varchar(255) NOT NULL,
  `ID_ALBUM` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID` (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

--
-- Despejando dados para a tabela `favoritos`
--

INSERT INTO `favoritos` (`ID`, `ID_POST`, `USUARIO`, `ID_ALBUM`) VALUES
(14, 16, 'Teste1', NULL);

-- --------------------------------------------------------

--
-- Estrutura para tabela `post`
--

DROP TABLE IF EXISTS `post`;
CREATE TABLE IF NOT EXISTS `post` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `USUARIO` varchar(225) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `LEGENDA` varchar(300) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `DATA_POST` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

--
-- Despejando dados para a tabela `post`
--

INSERT INTO `post` (`ID`, `USUARIO`, `LEGENDA`, `DATA_POST`) VALUES
(1, 'AllysonSouza', 'Olá mundo!', '2025-10-14 20:50:50'),
(2, 'AllysonSouza', 'Foi mais um', '2025-10-14 20:50:50'),
(3, 'Teste1', 'Teste1', '2025-10-14 20:50:50'),
(5, 'Teste1', 'Sou o primeiro', '2025-10-14 20:54:55'),
(6, 'Teste1', 'Teste2', '2025-10-14 21:11:42'),
(7, 'AllysonSouza', 'Teste de Horario', '2025-10-15 00:21:30'),
(8, 'AllysonSouza', 'Teste de imagem', '2025-10-15 00:28:06'),
(9, 'Teste1', 'aaa', '2025-10-15 18:41:47'),
(10, 'Teste1', 'aaa', '2025-10-15 18:43:00'),
(11, 'Teste1', 'teste1', '2025-10-15 18:48:03'),
(12, 'Teste1', 'Teste3', '2025-10-15 18:49:47'),
(13, 'Teste1', 'Teste4', '2025-10-15 18:55:01'),
(14, 'Teste1', 'Teste5', '2025-10-15 19:00:04'),
(15, 'Teste1', 'kkkk', '2025-10-15 19:09:13'),
(16, 'Teste1', 'Teste6', '2025-10-15 19:13:53'),
(17, 'Teste1', 'teste7', '2025-10-15 19:16:54'),
(18, 'Teste1', 'Teste8', '2025-10-15 19:28:29'),
(19, 'Teste1', 'Teste9', '2025-10-15 19:29:51'),
(20, 'Teste1', 'Teste10', '2025-10-15 20:12:36'),
(21, 'Teste1', 'Teste11', '2025-10-15 20:13:19'),
(22, 'Teste1', 'Olá', '2025-10-15 21:43:04'),
(23, 'Teste1', 'Olá, eu sou Allyson. Novo integrante desta rede social. Muito prazer! Gosto mutio do assunto de Dislaxia, trabalho com crianças na escola E.E.Escola inventada. Poderian me dar algumas dicas de como lidar e ajudar crianças com dislexia na aprendizagem?', '2025-10-15 21:46:06');

-- --------------------------------------------------------

--
-- Estrutura para tabela `profissionais`
--

DROP TABLE IF EXISTS `profissionais`;
CREATE TABLE IF NOT EXISTS `profissionais` (
  `CPF` char(11) NOT NULL,
  `NOME` varchar(200) NOT NULL,
  `USUARIO` varchar(100) NOT NULL,
  `PROFISSAO` varchar(100) NOT NULL,
  `DATANASCIMENTO` date DEFAULT NULL,
  `UF` char(2) NOT NULL,
  `CIDADE` varchar(200) NOT NULL,
  `ESCOLA` varchar(200) NOT NULL,
  `SENHA` varchar(12) NOT NULL,
  `BIOGRAFIA` varchar(500) DEFAULT NULL,
  `FOTOPERFIL` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`CPF`),
  UNIQUE KEY `CPF` (`CPF`),
  UNIQUE KEY `USUARIO` (`USUARIO`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Despejando dados para a tabela `profissionais`
--

INSERT INTO `profissionais` (`CPF`, `NOME`, `USUARIO`, `PROFISSAO`, `DATANASCIMENTO`, `UF`, `CIDADE`, `ESCOLA`, `SENHA`, `BIOGRAFIA`, `FOTOPERFIL`) VALUES
('46502239897', 'Allyson Kayk de Souza', 'AllysonSouza', 'Professor', NULL, 'AC', 'Acrelândia', 'ESC ALTINA MAGALHAES DA SILVA', 'Petalas12345', 'Fale um pouco sobre você', ''),
('49069495090', 'Teste1', 'Teste1', 'Professor', NULL, 'AC', 'Acrelândia', 'ESC ALTINA MAGALHAES DA SILVA', 'Teste1', 'Fale um pouco sobre você', ''),
('02205094254', 'Rodinel SIlva', 'RoroBora', 'Psicopedagôgo', NULL, 'RO', 'Jaru', 'CEEJA DE JARU', 'Mangis22', 'Fale um pouco sobre você', '');

-- --------------------------------------------------------

--
-- Estrutura para tabela `profissoes`
--

DROP TABLE IF EXISTS `profissoes`;
CREATE TABLE IF NOT EXISTS `profissoes` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `NOME` varchar(100) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID` (`ID`),
  UNIQUE KEY `NOME` (`NOME`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Despejando dados para a tabela `profissoes`
--

INSERT INTO `profissoes` (`ID`, `NOME`) VALUES
(1, 'Professor');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
