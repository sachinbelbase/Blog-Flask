-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 10, 2026 at 11:56 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `talkandcode`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(50) NOT NULL,
  `name` text NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime DEFAULT current_timestamp(),
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `phone_num`, `msg`, `date`, `email`) VALUES
(1, 'first post', '2123456786', 'first post', '2026-05-07 17:27:00', 'firstpost@gmail.com'),
(2, 'Ram', '4432343434', 'Hello Whats uppp', '2026-05-07 17:34:10', 'sachinbelbase818@gmail.com'),
(3, 'Hari', '34253463736', 'Ma hari ho haiii ', '2026-05-07 17:35:56', 'Hari@gmail.com'),
(4, 'Sita', '123432156', 'Ma sita ho haiii', '2026-05-07 18:12:07', 'sita@gmail.com'),
(7, 'Ram', '4432343434', 'fsdf d', '2026-05-07 18:50:58', 'wsdd@gmail.com'),
(8, 'fdsfsd', '4432343434', 'sdfsdgvsdz dfadfv ', '2026-05-07 18:53:52', 'sffdf@gmil.ocm');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `tagline` text NOT NULL,
  `slug` varchar(50) NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(80) NOT NULL,
  `date` datetime(5) NOT NULL DEFAULT current_timestamp(5)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `tagline`, `slug`, `content`, `img_file`, `date`) VALUES
(1, 'First Post', 'This is first post where we learn coding with coffee.', 'first-post', 'I am excited to share you guys about flask and we will do some project as our learning..', 'assets/img/home-bg.jpg', '2026-05-09 16:02:05.19166'),
(4, 'Variables', 'Variables are containers for storing data values. In Python, you don\'t need to declare the type explicitly.', 'fourth-post', 'Rules for naming variables:\r\n\r\nMust start with a letter or underscore (_)\r\nCannot start with a number\r\nCase-sensitive (age ≠ Age)\r\nCannot use reserved keywords (if, for, class, etc.)', 'assets/img/post-bg.jpg', '2026-05-08 16:07:06.00000'),
(5, 'Data Types', 'Primitive Types and Collection Types', 'five-post', 'Primitive Types\r\nTypeExampleDescriptionint42Whole numbersfloat3.14Decimal numbersstr\"hello\"TextboolTrue / FalseBoolean valuesNoneTypeNoneAbsence of value\r\n\r\nCollection Types\r\npython# List – ordered, mutable\r\nfruits = [\"apple\", \"banana\", \"cherry\"]\r\n\r\n# Tuple – ordered, immutable\r\ncoordinates = (10.5, 20.3)\r\n\r\n# Dictionary – key-value pairs\r\nperson = {\"name\": \"Alice\", \"age\": 25}\r\n\r\n# Set – unordered, unique values\r\nunique_nums = {1, 2, 3, 3}  # → {1, 2, 3}', 'assets/img/post-bg.jpg', '2026-05-08 16:07:58.00000');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
