-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 26-Set-2025 às 00:25
-- Versão do servidor: 5.7.40
-- versão do PHP: 8.0.26

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
-- Estrutura da tabela `profissionais`
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
  `RUA` varchar(200) DEFAULT NULL,
  `BAIRRO` varchar(200) DEFAULT NULL,
  `FOTOPERFIL` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`CPF`),
  UNIQUE KEY `CPF` (`CPF`),
  UNIQUE KEY `USUARIO` (`USUARIO`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `profissionais`
--

INSERT INTO `profissionais` (`CPF`, `NOME`, `USUARIO`, `PROFISSAO`, `DATANASCIMENTO`, `UF`, `CIDADE`, `ESCOLA`, `SENHA`, `BIOGRAFIA`, `RUA`, `BAIRRO`, `FOTOPERFIL`) VALUES
('46502239897', 'Allyson Kayk de Souza', 'AllysonSouza', 'Professor', NULL, 'AC', 'Acrelândia', 'ESC ALTINA MAGALHAES DA SILVA', 'Petalas12345', '', '', '', '');

-- --------------------------------------------------------

--
-- Estrutura da tabela `profissoes`
--

DROP TABLE IF EXISTS `profissoes`;
CREATE TABLE IF NOT EXISTS `profissoes` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `NOME` varchar(100) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID` (`ID`),
  UNIQUE KEY `NOME` (`NOME`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `profissoes`
--

INSERT INTO `profissoes` (`ID`, `NOME`) VALUES
(1, 'Professor');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
