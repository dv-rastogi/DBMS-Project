-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: cp-stats
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `organisation_paysto`
--

DROP TABLE IF EXISTS `organisation_paysto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `organisation_paysto` (
  `Organization_ID` varchar(20) NOT NULL,
  `Admin_Role` varchar(50) NOT NULL DEFAULT 'Organization',
  `DateOfPayment` datetime NOT NULL,
  `AmountPaid` int NOT NULL,
  `Ads` text,
  PRIMARY KEY (`Organization_ID`,`Admin_Role`,`DateOfPayment`),
  KEY `FK_Organization_paysTo_Role_idx` (`Admin_Role`),
  CONSTRAINT `FK_Organization_PaysTo_ID` FOREIGN KEY (`Organization_ID`) REFERENCES `programming_organisation` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_Organization_paysTo_Role` FOREIGN KEY (`Admin_Role`) REFERENCES `admin` (`Role`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `organisation_paysto`
--

LOCK TABLES `organisation_paysto` WRITE;
/*!40000 ALTER TABLE `organisation_paysto` DISABLE KEYS */;
INSERT INTO `organisation_paysto` VALUES ('P-1','Advertisement','2020-05-16 00:00:00',9764,'plasticize contumacy recherche quackers pee-pee hegira famosity deepens piddly limpish benign reapplying yeoman moth-eaten Bastille alluvium half-breed proponents perturbate growling viewly oogamous extrane larboard nonflat goodlich swarming forequoted Phocaea henlike wages-man spawners disunions citrate pulsates adherer popcraft simpleness subfusk hurling umbrello covenantee inventions vulcanist pump-gear Lansing timeline storms abland Ætolia'),('P-1','Global','2020-09-04 00:00:00',3623,'cabinet dotest limitative kumiss swindling argol theomaniac soiree cushiest dashpot stumbled ploughmen waiver crotched middleman ruliest brunt Henry VI war-drum lyonnaise instructed maistow roomlike tricksier chalona loggings sea-beaver gusher opposing trumpeter nonabused gamesome inworking bassarisk through awsome satinwoods window audiometer partygoer splendour Kurdistan bone-meal consisting tufaceous apposition thine protractor rain-stone parovarium'),('P-1','Organisation','2020-03-11 00:00:00',4871,'testoon sailing modded ruffing bitchfest tenoroon Omolon prides excrements metathorax schmutz thumbholes unsyllabic outbidder alacritous bogging saginas Cupid paperbound wafters pronto coagulates assoyle justified gaffsail southwest extending torpidly Langtry propries camisoles Blimp unedible red-string slakeless chickera systemise dogmas dizzy ignavus should trophied areaway juiceheads boobie bifenthrin noddy bekah blogettes mellows'),('P-1','Technical','2020-02-22 00:00:00',7253,'bradawl ballerina rindle metropolis sidepiece lambdoidal omnivora Anastacia planula spasmodist rustics kennings Damietta PHOSITA humankind azurn hydrophane rewalked hard-port armories virgule hares berceuse unsymmetry grayfish dogheads subsenses gourdlike Low Latin proofreads BOHICA intricate acceptants put-downs Oldsmobile yeanling preciosity drillcore nonobscene tone-poet similarity makiotoshi detecter sapient paradoxic unemulated maximax debriefing granitas paynimry'),('P-1','User','2020-06-08 00:00:00',9490,'Mosby sargasso clozes outwake atomized brightness fulfilled Eyemouth adductions rustily unsafely ingrowths shorten thinkers uppishly cameleon trodden ice-line rollers carbonara lustiness hailstone wiggly trampish tone-poem Bombes nasalized tailwinds nacking conversers pledges trustors new-to-us jadelike defamatory fox-goose drowsihed exornate acanthine wabbly necklines moon-dog morion caravaned froglet Bromberg lightened blash asaphus Russki'),('P-2','Advertisement','2020-12-05 00:00:00',5691,'réchauffé hand-lever grassiest Thucydides clientside divining sluicegate pretrials scourging ulnas nonsexual gambol mappable wrister chilam radionics arguidos dredged Goosnargh medallists lee-clue readout marketised greedy-gut depucelate middler night-tide cycads bipedalism chamar parishes raptness cabins anisogamy theoline bootlaces midwive zoöphites nonethical manicurist senocular satirical pit-head biathlon deglazing bitchen ferrules swamplands appliance majordomo'),('P-2','Organisation','2020-09-10 00:00:00',8042,'hawfinch cavort Priestley trenchant esterify tenuious chancels whirs unrolls gnomology cashless monorhyme wrest-pin crawdad Englanders acutely refining peepshows shoplifter linenette nepheline Klansman verdea peptone bow-legged faldage eldrich culms fusee Aliakbar megilp two-leafed lamp-fly perilymph fastuous tannest bitchwad coppas slackens spy-fi misgraft balzan smegging proponents plantaris fatigable comper scraich cosigning reassuring'),('P-2','Premium','2020-06-29 00:00:00',9616,'taffeta workrooms encomiums gaolers hummum expletives anabiosis beasted bowse vicereine zip-code remated port-bar magnified tabiyas patenter toughener problemo cordectomy cribriform encoffined islets condiment coarsest trading sea-tang hand-dye lither disquietly stammers father-god fiancé coverable techily bluffs marrows hairy-back backlifts harlock unwisely yeast raught pegma cosmids Humvees claustral tuppenny drosera cymose rejoiceth'),('P-2','Support','2020-03-24 00:00:00',4056,'juked spadix multisets course cowardice bound unawakened half-pike hookum concertise ruffle teaches librpc barless bhistee tailwhip honeybees housecats festino corals reblock blousy gossippers needled silicones foreshores sheened gatherers crustæ mimicries domelike monoculous comporting Demetrius antiphonic specified activism heralding bourne lightened Saguenay medidural fuzzless genitival marrows seizings paring knowingly plywood obispo'),('P-2','User','2020-08-15 00:00:00',5381,'scran hubcap armorial simplexes cowherd brimless sweatsuit wood-elf gosport whose rhodanine leg-bail valkyria Gorbachev annoyed Mickey D sand-devil costay taigs thirstless soapmaking unbusied hilarious blowtube tawpies skywards encounters Leone spackled suckling incognitum getups henches delegees sarsenet Tánaiste standover reffo WheelTrans supergeek mammee nephoscope three-out crabgrass zymogen mogul pillowlike rundlet perversive javan');
/*!40000 ALTER TABLE `organisation_paysto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-16 20:07:06
