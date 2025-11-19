CREATE DATABASE IF NOT EXISTS DESBRAVA;
USE DESBRAVA;

-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 19-Nov-2025 às 04:11
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
-- Estrutura da tabela `profissoes`
--

DROP TABLE IF EXISTS `profissoes`;
CREATE TABLE IF NOT EXISTS `profissoes` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `NOME` varchar(100) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID` (`ID`),
  UNIQUE KEY `NOME` (`NOME`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `profissoes`
--

INSERT INTO `profissoes` (`ID`, `NOME`) VALUES
(1, 'Professor'),
(2, 'Psicopedagogo'),
(3, 'Neuropsicólogo'),
(4, 'Psicólogo Infantil'),
(5, 'Psicólogo Escolar'),
(6, 'Fonoaudiólogo'),
(7, 'Terapeuta Ocupacional'),
(8, 'Pedagogo'),
(9, 'Professor de Educação Especial'),
(10, 'Professor de Atendimento Educacional Especializado (AEE)'),
(11, 'Neurologista Infantil'),
(12, 'Neurocientista Educacional'),
(13, 'Psicomotricista'),
(14, 'Terapeuta Comportamental Infantil'),
(15, 'Terapeuta Cognitivo-Comportamental'),
(16, 'Médico Psiquiatra Infantil'),
(17, 'Psicomotricista Relacional'),
(18, 'Musicoterapeuta'),
(19, 'Arteterapeuta'),
(20, 'Educador Especialista em Alfabetização'),
(21, 'Especialista em Linguagem'),
(22, 'Especialista em Dificuldades de Aprendizagem'),
(23, 'Orientador Educacional'),
(24, 'Consultor Educacional para Transtornos de Aprendizagem'),
(25, 'Instrutor de Reforço Escolar Especializado'),
(26, 'Assistente Social Escolar');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
