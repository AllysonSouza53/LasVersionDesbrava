CREATE DATABASE IF NOT EXISTS DESBRAVA;
USE DESBRAVA;

-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 19-Nov-2025 às 11:46
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
-- Estrutura da tabela `albuns`
--

DROP TABLE IF EXISTS `albuns`;
CREATE TABLE IF NOT EXISTS `albuns` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `NOME` varchar(255) NOT NULL,
  `USUARIO` varchar(255) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID` (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `albuns`
--

INSERT INTO `albuns` (`ID`, `NOME`, `USUARIO`) VALUES
(15, 'teste1', 'Teste'),
(14, 'Atividades', 'Teste1'),
(16, 'Album Teste', 'Teste1'),
(18, 'AT', 'roberta');

-- --------------------------------------------------------

--
-- Estrutura da tabela `alunos`
--

DROP TABLE IF EXISTS `alunos`;
CREATE TABLE IF NOT EXISTS `alunos` (
  `RE` bigint(10) NOT NULL,
  `NOME` varchar(225) CHARACTER SET utf8 NOT NULL,
  `USUARIO` varchar(225) CHARACTER SET utf8 NOT NULL,
  `ESCOLA` varchar(225) CHARACTER SET utf8 NOT NULL,
  `DATANASCIMENTO` date NOT NULL,
  `GENERO` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `TURMA` text CHARACTER SET utf8,
  `PROFISSIONALRESPONSAVEL` char(11) NOT NULL,
  `UF` char(2) CHARACTER SET utf8 NOT NULL,
  `CIDADE` varchar(225) CHARACTER SET utf8 NOT NULL,
  `DIAGNOSTICO` varchar(255) CHARACTER SET utf8 NOT NULL,
  `OBSERVACOES` varchar(1000) CHARACTER SET utf8 DEFAULT NULL,
  `NIVELDELEITURA` int(11) DEFAULT NULL,
  `NIVELDEESCRITA` int(11) DEFAULT NULL,
  `FASETRILHA` int(11) DEFAULT NULL,
  PRIMARY KEY (`RE`),
  UNIQUE KEY `USUARIO` (`USUARIO`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `alunos`
--

INSERT INTO `alunos` (`RE`, `NOME`, `USUARIO`, `ESCOLA`, `DATANASCIMENTO`, `GENERO`, `TURMA`, `PROFISSIONALRESPONSAVEL`, `UF`, `CIDADE`, `DIAGNOSTICO`, `OBSERVACOES`, `NIVELDELEITURA`, `NIVELDEESCRITA`, `FASETRILHA`) VALUES
(12345, 'João da Silva', 'joaosilva', 'Escola Municipal ABC', '2012-05-15', 'Masculino', '5A', '46502239897', 'SP', 'Campinas', 'Dislexia Leve', 'Observações fictícias sobre o aluno', 2, 1, 4),
(11, '11', '11', 'ESC XVII DE NOVEMBRO', '2022-11-11', 'Masculino', '3A', '49069495090', 'AC', 'Assis Brasil', 'Dislexia', '', 1, 1, 0),
(1111111111, '2', '2', 'ARVENSE C EDUCACIONAL', '1111-11-22', 'Masculino', '2', '31456328255', 'DF', 'Brasília', '2', '2', 3, 2, NULL),
(2222222222, '3', '3', 'ESC ALTINA MAGALHAES DA SILVA', '1111-11-11', 'Masculino', '1', '31456328255', 'AC', 'Acrelândia', '1', '1', 1, 1, NULL);

-- --------------------------------------------------------

--
-- Estrutura da tabela `comentarios`
--

DROP TABLE IF EXISTS `comentarios`;
CREATE TABLE IF NOT EXISTS `comentarios` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `USUARIO` varchar(255) NOT NULL,
  `IDPOST` int(11) NOT NULL,
  `TEXTO` varchar(500) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `dados_jogos`
--

DROP TABLE IF EXISTS `dados_jogos`;
CREATE TABLE IF NOT EXISTS `dados_jogos` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `ID_ALUNO` varchar(11) NOT NULL,
  `USUARIO_PROFISSIONAL` varchar(11) NOT NULL,
  `NOME_JOGO` varchar(50) NOT NULL,
  `ID_FASE` int(11) NOT NULL,
  `ID_NIVEL` int(11) NOT NULL,
  `PONTUACAO` int(11) DEFAULT '0',
  `PORCENTAGEM_COMPLETADA` decimal(5,2) DEFAULT '0.00',
  `TEMPO_GASTO` time DEFAULT '00:00:00',
  `ACERTOS` int(11) DEFAULT '0',
  `ERROS` int(11) DEFAULT '0',
  `TENTATIVAS` int(11) DEFAULT '0',
  `DATA_REGISTRO` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=164 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `dados_jogos`
--

INSERT INTO `dados_jogos` (`ID`, `ID_ALUNO`, `USUARIO_PROFISSIONAL`, `NOME_JOGO`, `ID_FASE`, `ID_NIVEL`, `PONTUACAO`, `PORCENTAGEM_COMPLETADA`, `TEMPO_GASTO`, `ACERTOS`, `ERROS`, `TENTATIVAS`, `DATA_REGISTRO`) VALUES
(138, '1', '49069495090', 'silabamix', 28, 1, 10, '120.83', '00:00:01', 1, 0, 2, '2025-11-13 22:26:49'),
(137, '1', '49069495090', 'silabamix', 27, 1, 10, '116.67', '00:00:01', 1, 0, 2, '2025-11-13 22:26:45'),
(136, '1', '49069495090', 'silabamix', 26, 1, 10, '112.50', '00:00:01', 1, 0, 2, '2025-11-13 22:26:42'),
(135, '1', '49069495090', 'silabamix', 25, 1, 10, '108.33', '00:00:01', 1, 0, 2, '2025-11-13 22:26:37'),
(134, '1', '49069495090', 'silabamix', 25, 1, 10, '108.33', '00:00:02', 1, 0, 2, '2025-11-13 22:23:20'),
(132, '1', '49069495090', 'organizar cores', 23, 1, 8, '100.00', '00:00:16', 8, 0, 1, '2025-11-13 22:22:53'),
(133, '1', '49069495090', 'organizar cores', 24, 1, 8, '100.00', '00:00:18', 8, 0, 2, '2025-11-13 22:23:15'),
(131, '1', '49069495090', 'silabamix', 25, 1, 10, '108.33', '00:00:01', 1, 0, 2, '2025-11-13 22:19:01'),
(129, '1', '49069495090', 'silabamix', 25, 1, 10, '108.33', '00:00:01', 1, 0, 2, '2025-11-13 22:18:53'),
(130, '1', '49069495090', 'silabamix', 25, 1, 10, '108.33', '00:00:02', 1, 0, 2, '2025-11-13 22:18:58'),
(128, '1', '49069495090', 'silabamix', 25, 1, 10, '108.33', '00:00:02', 1, 0, 2, '2025-11-13 22:18:49'),
(126, '1', '49069495090', 'silabamix', 25, 1, 10, '108.33', '00:00:01', 1, 0, 2, '2025-11-13 22:16:27'),
(127, '1', '49069495090', 'silabamix', 25, 1, 10, '108.33', '00:00:01', 1, 0, 2, '2025-11-13 22:16:34'),
(125, '1', '49069495090', 'silabamix', 25, 1, 10, '108.33', '00:00:01', 1, 0, 2, '2025-11-13 22:16:24'),
(123, '1', '49069495090', 'silabamix', 25, 1, 10, '108.33', '00:00:02', 1, 0, 2, '2025-11-13 22:16:15'),
(124, '1', '49069495090', 'silabamix', 25, 1, 10, '108.33', '00:00:02', 1, 0, 2, '2025-11-13 22:16:20'),
(121, '1', '49069495090', 'organizar cores', 23, 1, 8, '100.00', '00:00:21', 8, 0, 21, '2025-11-13 22:11:03'),
(122, '1', '49069495090', 'organizar cores', 24, 1, 8, '100.00', '00:00:20', 8, 0, 22, '2025-11-13 22:11:26'),
(120, '1', '49069495090', 'organizar cores', 22, 1, 8, '100.00', '00:00:14', 8, 0, 20, '2025-11-13 22:10:35'),
(119, '1', '49069495090', 'organizar cores', 21, 1, 8, '100.00', '00:00:15', 8, 0, 19, '2025-11-13 22:10:17'),
(118, '1', '49069495090', 'organizar cores', 20, 1, 8, '100.00', '00:00:15', 8, 0, 18, '2025-11-13 22:09:58'),
(117, '1', '49069495090', 'organizar cores', 19, 1, 8, '100.00', '00:00:20', 8, 0, 17, '2025-11-13 22:09:38'),
(115, '1', '49069495090', 'organizar cores', 17, 1, 8, '100.00', '00:00:29', 8, 0, 15, '2025-11-13 22:08:44'),
(116, '1', '49069495090', 'organizar cores', 18, 1, 8, '100.00', '00:00:19', 8, 0, 16, '2025-11-13 22:09:15'),
(113, '1', '49069495090', 'organizar cores', 15, 1, 6, '100.00', '00:00:09', 6, 0, 13, '2025-11-13 22:07:58'),
(114, '1', '49069495090', 'organizar cores', 16, 1, 6, '100.00', '00:00:09', 6, 0, 14, '2025-11-13 22:08:11'),
(111, '1', '49069495090', 'organizar cores', 13, 1, 6, '100.00', '00:00:11', 6, 0, 11, '2025-11-13 22:07:10'),
(112, '1', '49069495090', 'organizar cores', 14, 1, 6, '100.00', '00:00:11', 6, 0, 12, '2025-11-13 22:07:45'),
(109, '1', '49069495090', 'organizar cores', 11, 1, 6, '100.00', '00:00:07', 6, 0, 9, '2025-11-13 22:06:24'),
(110, '1', '49069495090', 'organizar cores', 12, 1, 6, '100.00', '00:00:10', 6, 0, 10, '2025-11-13 22:06:38'),
(107, '1', '49069495090', 'organizar cores', 9, 1, 6, '100.00', '00:00:13', 6, 0, 6, '2025-11-13 22:05:52'),
(108, '1', '49069495090', 'organizar cores', 10, 1, 6, '100.00', '00:00:11', 6, 0, 7, '2025-11-13 22:06:06'),
(106, '1', '49069495090', 'organizar cores', 8, 1, 4, '100.00', '00:00:09', 4, 0, 5, '2025-11-13 22:05:35'),
(105, '1', '49069495090', 'organizar cores', 7, 1, 4, '100.00', '00:00:06', 4, 0, 4, '2025-11-13 22:05:22'),
(104, '1', '49069495090', 'organizar cores', 6, 1, 4, '100.00', '00:00:06', 4, 0, 3, '2025-11-13 22:05:12'),
(103, '1', '49069495090', 'organizar cores', 5, 1, 4, '100.00', '00:00:05', 4, 0, 2, '2025-11-13 22:05:02'),
(102, '1', '49069495090', 'organizar cores', 4, 1, 4, '100.00', '00:00:06', 4, 0, 1, '2025-11-13 22:04:45'),
(101, '12345', '46502239897', 'organizar cores', 3, 1, 8, '100.00', '00:00:24', 8, 0, 3, '2025-11-13 21:32:37'),
(100, '12345', '46502239897', 'organizar cores', 2, 1, 6, '100.00', '00:00:13', 6, 0, 2, '2025-11-13 21:32:07'),
(99, '12345', '46502239897', 'organizar cores', 1, 1, 4, '100.00', '00:00:08', 4, 0, 1, '2025-11-13 21:31:33'),
(98, '1', '49069495090', 'organizar cores', 3, 1, 8, '100.00', '00:00:13', 8, 0, 4, '2025-11-13 21:28:55'),
(97, '1', '49069495090', 'organizar cores', 2, 1, 6, '100.00', '00:00:15', 6, 0, 3, '2025-11-13 21:28:38'),
(96, '1', '49069495090', 'organizar cores', 1, 1, 4, '100.00', '00:00:05', 4, 0, 2, '2025-11-13 21:28:15'),
(95, '1', '49069495090', 'organizar cores', 1, 1, 4, '100.00', '00:00:06', 4, 0, 1, '2025-11-13 20:53:00'),
(139, '1', '49069495090', 'silabamix', 29, 1, 10, '125.00', '00:00:05', 1, 0, 6, '2025-11-13 22:26:57'),
(140, '1', '49069495090', 'silabamix', 30, 1, 10, '129.17', '00:00:01', 1, 0, 2, '2025-11-13 22:27:01'),
(141, '1', '49069495090', 'silabamix', 31, 1, 10, '133.33', '00:00:01', 1, 0, 2, '2025-11-13 22:27:05'),
(142, '1', '49069495090', 'silabamix', 32, 1, 10, '137.50', '00:00:02', 1, 0, 3, '2025-11-13 22:27:10'),
(143, '1', '49069495090', 'silabamix', 33, 1, 10, '141.67', '00:00:08', 1, 0, 9, '2025-11-13 22:27:20'),
(144, '1', '49069495090', 'silabamix', 34, 1, 10, '145.83', '00:00:02', 1, 0, 3, '2025-11-13 22:27:24'),
(145, '1', '49069495090', 'silabamix', 35, 1, 10, '150.00', '00:00:02', 1, 0, 3, '2025-11-13 22:27:29'),
(146, '1', '49069495090', 'silabamix', 36, 1, 10, '154.17', '00:00:02', 1, 0, 3, '2025-11-13 22:27:34'),
(147, '1', '49069495090', 'silabamix', 37, 1, 10, '158.33', '00:00:02', 1, 0, 3, '2025-11-13 22:27:38'),
(148, '1', '49069495090', 'silabamix', 38, 1, 10, '162.50', '00:00:02', 1, 0, 3, '2025-11-13 22:27:43'),
(149, '1', '49069495090', 'silabamix', 39, 1, 10, '166.67', '00:00:03', 1, 0, 3, '2025-11-13 22:27:48'),
(150, '1', '49069495090', 'silabamix', 40, 1, 10, '170.83', '00:00:04', 1, 0, 6, '2025-11-13 22:27:54'),
(151, '1', '49069495090', 'silabamix', 41, 1, 10, '175.00', '00:00:03', 1, 0, 4, '2025-11-13 22:28:00'),
(152, '1', '49069495090', 'silabamix', 42, 1, 10, '179.17', '00:00:03', 1, 0, 4, '2025-11-13 22:28:05'),
(153, '1', '49069495090', 'silabamix', 43, 1, 10, '183.33', '00:00:12', 1, 0, 4, '2025-11-13 22:28:19'),
(154, '1', '49069495090', 'silabamix', 44, 1, 10, '187.50', '00:00:03', 1, 0, 4, '2025-11-13 22:28:24'),
(155, '1', '49069495090', 'silabamix', 45, 1, 10, '191.67', '00:00:03', 1, 0, 4, '2025-11-13 22:28:30'),
(156, '1', '49069495090', 'silabamix', 46, 1, 10, '195.83', '00:00:03', 1, 0, 4, '2025-11-13 22:28:37'),
(157, '1', '49069495090', 'silabamix', 47, 1, 10, '200.00', '00:00:04', 1, 0, 4, '2025-11-13 22:28:44'),
(158, '1', '49069495090', 'somsilaba', 1, 1, 10, '100.00', '00:00:04', 1, 0, 1, '2025-11-13 22:32:21'),
(159, '1', '49069495090', 'organizar cores', 1, 1, 4, '100.00', '00:00:35', 4, 0, 1, '2025-11-17 20:59:15'),
(160, '1', '49069495090', 'organizar cores', 2, 1, 4, '100.00', '00:00:10', 4, 0, 2, '2025-11-17 20:59:32'),
(161, '1', '49069495090', 'organizar cores', 3, 1, 4, '100.00', '00:00:09', 4, 0, 3, '2025-11-17 20:59:51'),
(162, '1', '49069495090', 'organizar cores', 4, 1, 4, '100.00', '00:00:11', 4, 0, 4, '2025-11-17 21:00:06'),
(163, '1', '49069495090', 'organizar cores', 5, 1, 4, '100.00', '00:00:08', 4, 0, 5, '2025-11-17 21:00:18');

-- --------------------------------------------------------

--
-- Estrutura da tabela `favoritos`
--

DROP TABLE IF EXISTS `favoritos`;
CREATE TABLE IF NOT EXISTS `favoritos` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `ID_POST` int(11) NOT NULL,
  `USUARIO` varchar(255) NOT NULL,
  `NOME_ALBUM` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID` (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `favoritos`
--

INSERT INTO `favoritos` (`ID`, `ID_POST`, `USUARIO`, `NOME_ALBUM`) VALUES
(18, 8, 'Teste1', NULL),
(19, 12, 'Teste1', 'Atividades'),
(20, 15, 'Teste', NULL),
(21, 5, 'Teste', 'teste1'),
(22, 26, 'roberta', 'Atividades'),
(26, 3, 'roberta', 'AT');

-- --------------------------------------------------------

--
-- Estrutura da tabela `post`
--

DROP TABLE IF EXISTS `post`;
CREATE TABLE IF NOT EXISTS `post` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `USUARIO` varchar(225) CHARACTER SET utf8 NOT NULL,
  `LEGENDA` varchar(2000) CHARACTER SET utf8 DEFAULT NULL,
  `DATA_POST` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `post`
--

INSERT INTO `post` (`ID`, `USUARIO`, `LEGENDA`, `DATA_POST`) VALUES
(30, 'roberta', 'ESTRATÉGIAS PEDAGÓGICAS INCLUSIVAS\n\nA criança com dislexia sofre com baixa autoestima, e nós, como profissionais que lidamos diariamente com esses alunos, podemos ajudar a melhorar a forma como ele se vê e como ele lida com o seu transtorno. O medo e a sensação de estar atrasado reflete diretamente na motivação da criança, influenciando no seu aprendizado. Com o objetivo de ajudar, trouxe aqui algumas estratégias que aprendi com a Associação Internacional de Dislexia. São elas: \n\n•Dar tempo extra para completar as tarefas; \n•Oferecer ao estudante ajuda para fazer suas anotações; \n•Modificar trabalhos e pesquisas, segundo a necessidade do aluno; \n•Esclarecer ou simplificar instruções escritas, sublinhando ou destacando os aspectos importantes para o aluno; \n•Reduzir a quantidade de texto a ser lido; \n•Bloquear estímulos externos, caso o estudante se distraia com facilidade; \n•Proporcionar atividades práticas adicionais, uma vez que os materiais não oferecem em número suficiente para crianças com dificuldade de aprendizagem; \n•Fornecer glossários dos conteúdos e guia para auxiliar o aluno a compreender a leitura; \n•Repetir as orientações e recomendações, pois alguns estudantes possuem dificuldade em seguir instruções. Sendo assim, pode-se pedir que o mesmo repita com suas próprias palavras; \n•Variar os modos de avaliação, ou seja, apresentações orais, participação em discussões, avaliações escritas e provas com múltipla escolha; \n•Estimular o uso de agendas, calendários e organizadores; \n•Graduar os conteúdos a serem abordados, em um nível crescente de dificuldade.\n', '2025-11-17 20:43:14');

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
  `FOTOPERFIL` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`CPF`),
  UNIQUE KEY `CPF` (`CPF`),
  UNIQUE KEY `USUARIO` (`USUARIO`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `profissionais`
--

INSERT INTO `profissionais` (`CPF`, `NOME`, `USUARIO`, `PROFISSAO`, `DATANASCIMENTO`, `UF`, `CIDADE`, `ESCOLA`, `SENHA`, `BIOGRAFIA`, `FOTOPERFIL`) VALUES
('31456328255', 'Roberta Gonçalves', 'roberta', 'Professor', NULL, 'AC', 'Acrelândia', 'ESC ALTINA MAGALHAES DA SILVA', 'roberta', 'Apaixonada por ensinar e inspirar cada aluno a descobrir seu potencial. Educação com carinho e dedicação.', '');

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
