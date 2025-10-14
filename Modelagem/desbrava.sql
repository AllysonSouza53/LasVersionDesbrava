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
-- Estrutura da tabela `alunos`
--

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
-- Estrutura da tabela `post`
--
CREATE TABLE IF NOT EXISTS `post` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `USUARIO` varchar(225) CHARACTER SET utf8 NOT NULL,
  `ARQUIVO` varchar(225) CHARACTER SET utf8 DEFAULT NULL,
  `LEGENDA` varchar(300) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `profissionais`
--

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

CREATE TABLE IF NOT EXISTS FAVORITOS(
	ID INT AUTO_INCREMENT UNIQUE,
    ID_POST INT UNIQUE,
    ID_USUARIO INT,
    ID_ALBUM INT,
    PRIMARY KEY(ID)
);


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
