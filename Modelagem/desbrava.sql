CREATE DATABASE IF NOT EXISTS DESBRAVA;
USE DESBRAVA;

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
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `alunos`
--

DROP TABLE IF EXISTS `alunos`;
CREATE TABLE IF NOT EXISTS `alunos` (
  `RE` int(11) NOT NULL,
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
  `NIVELDELEITURA` int(1) DEFAULT NULL,
  `NIVELDEESCRITA` int(1) DEFAULT NULL,
  PRIMARY KEY (`RE`),
  UNIQUE KEY `USUARIO` (`USUARIO`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `alunos`
--

INSERT INTO `alunos` (`RE`, `NOME`, `USUARIO`, `ESCOLA`, `DATANASCIMENTO`, `GENERO`, `TURMA`, `PROFISSIONALRESPONSAVEL`, `UF`, `CIDADE`, `DIAGNOSTICO`, `OBSERVACOES`, `NIVELDELEITURA`, `NIVELDEESCRITA`) VALUES
(12345, 'João da Silva', 'joaosilva', 'Escola Municipal ABC', '2012-05-15', 'Masculino', '5A', '46502239897', 'SP', 'Campinas', 'Dislexia Leve', 'Observações fictícias sobre o aluno', 2, 1);

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
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `comentarios`
--

INSERT INTO `comentarios` (`ID`, `USUARIO`, `IDPOST`, `TEXTO`) VALUES
(1, 'AllysonSouza', 1, 'Ola Brasil!!!!!'),
(2, 'AllysonSouza', 1, 'Foi mais um');

-- --------------------------------------------------------

--
-- Estrutura da tabela `favoritos`
--

DROP TABLE IF EXISTS `favoritos`;
CREATE TABLE IF NOT EXISTS `favoritos` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `ID_POST` int(11) NOT NULL,
  `USUARIO` varchar(255) NOT NULL,
  `ID_ALBUM` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID` (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `post`
--

DROP TABLE IF EXISTS `post`;
CREATE TABLE IF NOT EXISTS `post` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `USUARIO` varchar(225) CHARACTER SET utf8 NOT NULL,
  `LEGENDA` varchar(300) CHARACTER SET utf8 DEFAULT NULL,
  `DATA_POST` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `post`
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
('46502239897', 'Allyson Kayk de Souza', 'AllysonSouza', 'Professor', NULL, 'AC', 'Acrelândia', 'ESC ALTINA MAGALHAES DA SILVA', 'Petalas12345', 'Fale um pouco sobre você', ''),
('49069495090', 'Teste1', 'Teste1', 'Professor', NULL, 'AC', 'Acrelândia', 'ESC ALTINA MAGALHAES DA SILVA', 'Teste1', 'Fale um pouco sobre você', ''),
('02205094254', 'Rodinel SIlva', 'RoroBora', 'Psicopedagôgo', NULL, 'RO', 'Jaru', 'CEEJA DE JARU', 'Mangis22', 'Fale um pouco sobre você', '');

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
