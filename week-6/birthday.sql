CREATE DATABASE birthday;
USE birthday;
--
-- Database: `birthday`
--

-- --------------------------------------------------------

--
-- Table structure for table `gift`
--

CREATE TABLE `gift` (
  `gift_id` int(11) NOT NULL,
  `gift_name` varchar(50) DEFAULT NULL,
  `guest_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `gift`
--

INSERT INTO `gift` (`gift_id`, `gift_name`, `guest_id`) VALUES
(1, 'Cash', 1),
(2, 'Blender', 1),
(3, 'Cloth', 3),
(4, 'Shoe', 7),
(5, 'Shoe', 1),
(6, 'Car', 4);

-- --------------------------------------------------------

--
-- Table structure for table `guest`
--

CREATE TABLE `guest` (
  `guest_id` int(11) NOT NULL,
  `guest_fullname` varchar(100) NOT NULL,
  `guest_phone` varchar(50) NOT NULL,
  `guest_email` varchar(50) NOT NULL,
  `guest_gender` enum('Female','Male') NOT NULL,
  `guest_state` int(11) NOT NULL,
  `guest_datereg` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `guest`
--

INSERT INTO `guest` (`guest_id`, `guest_fullname`, `guest_phone`, `guest_email`, `guest_gender`, `guest_state`, `guest_datereg`) VALUES
(1, 'Adedayo Kolawole', '0804564667', 'a@b.com', 'Female', 1, '2017-03-24 14:14:30'),
(2, 'Tijani Abayomi', '0892345688', 'x@y.com', 'Male', 5, '2017-08-24 14:14:59'),
(3, 'John Smith', '0802345667', 'john@yahoo.com', 'Male', 1, '2017-01-24 14:15:59'),
(4, 'JJ Okocha', '0803456677', 'jj@y.com', 'Male', 6, '2017-05-24 14:16:54'),
(5, 'Taribo West', '', 't@x.com', 'Male', 16, '2017-08-24 14:18:02'),
(6, 'Damilola Oni', '0802345678', 'd@y.com', 'Female', 36, '2017-08-24 14:21:01'),
(7, 'Tunde Ojo', '0804556788', 'tunde@yahoo.com', 'Male', 6, '2017-08-24 14:22:14'),
(8, 'Janet Jackson', '0832345678', 'jack@y.com', 'Female', 12, '2017-08-24 14:22:51');

-- --------------------------------------------------------

--
-- Table structure for table `state`
--

CREATE TABLE `state` (
  `state_id` int(11) NOT NULL DEFAULT 0,
  `state_name` varchar(20) NOT NULL DEFAULT ''
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `state`
--

INSERT INTO `state` (`state_id`, `state_name`) VALUES
(1, 'Abia'),
(2, 'Adamawa'),
(3, 'Akwa Ibom'),
(4, 'Anambra'),
(5, 'Bauchi'),
(6, 'Bayelsa'),
(7, 'Benue'),
(8, 'Borno'),
(9, 'Cross River'),
(10, 'Delta'),
(11, 'Ebonyi'),
(12, 'Edo'),
(13, 'Ekiti'),
(14, 'Enugu'),
(15, 'Gombe'),
(16, 'Imo'),
(17, 'Jigawa'),
(18, 'Kaduna'),
(19, 'Kano'),
(20, 'Katsina'),
(21, 'Kebbi'),
(22, 'Kogi'),
(23, 'Kwara'),
(24, 'Lagos'),
(25, 'Nassarawa'),
(26, 'Niger'),
(27, 'Ogun'),
(28, 'Ondo'),
(29, 'Osun'),
(30, 'Oyo'),
(31, 'Plateau'),
(32, 'Rivers'),
(33, 'Sokoto'),
(34, 'Taraba'),
(35, 'Yobe'),
(36, 'Zamfara'),
(37, 'FCT'),
(38, 'Foreign');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `gift`
--
ALTER TABLE `gift`
  ADD PRIMARY KEY (`gift_id`);

--
-- Indexes for table `guest`
--
ALTER TABLE `guest`
  ADD PRIMARY KEY (`guest_id`);

--
-- Indexes for table `state`
--
ALTER TABLE `state`
  ADD PRIMARY KEY (`state_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `gift`
--
ALTER TABLE `gift`
  MODIFY `gift_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `guest`
--
ALTER TABLE `guest`
  MODIFY `guest_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;