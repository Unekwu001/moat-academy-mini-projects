-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 11, 2022 at 09:21 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `agerdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `ager_local_govts`
--

CREATE TABLE `ager_local_govts` (
  `lga_id` bigint(20) NOT NULL,
  `lga_name` varchar(45) NOT NULL DEFAULT 'N/A',
  `state_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `ager_states`
--

CREATE TABLE `ager_states` (
  `state_id` bigint(20) NOT NULL,
  `state_name` varchar(25) NOT NULL DEFAULT 'N/A'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `ager_villages`
--

CREATE TABLE `ager_villages` (
  `village_id` bigint(20) NOT NULL,
  `village_name` varchar(45) NOT NULL,
  `lga_id` bigint(20) NOT NULL,
  `state_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `contract_agreement`
--

CREATE TABLE `contract_agreement` (
  `trust_group_id` bigint(20) NOT NULL,
  `farmer_id` bigint(20) NOT NULL,
  `contract_acceptance` enum('yes','no') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `crop_types`
--

CREATE TABLE `crop_types` (
  `crop_id` bigint(20) NOT NULL,
  `crop_name` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `farmers_harvest_repayment_data`
--

CREATE TABLE `farmers_harvest_repayment_data` (
  `bag_id` bigint(20) NOT NULL,
  `bag_weight(kg)` decimal(5,2) NOT NULL DEFAULT 0.00,
  `grain_neatness` enum('good','bad') DEFAULT NULL,
  `correct_grain_variety` enum('true','false') DEFAULT NULL,
  `time_of_repayment` timestamp NULL DEFAULT NULL,
  `farmer_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `farmers_input_collection_data`
--

CREATE TABLE `farmers_input_collection_data` (
  `trust_group_id` bigint(20) DEFAULT NULL,
  `farmer_id` bigint(20) NOT NULL,
  `id_of_input_collected` bigint(20) NOT NULL,
  `count_per_input_type_collected` int(11) NOT NULL,
  `distribution_officer_id` bigint(20) DEFAULT NULL,
  `distribution_center_id` bigint(20) NOT NULL,
  `time of distribution` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `input_distribution_batch_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `field_officers`
--

CREATE TABLE `field_officers` (
  `officer_id` bigint(20) NOT NULL,
  `first_name` varchar(45) NOT NULL DEFAULT 'N/A',
  `surname` varchar(45) NOT NULL DEFAULT 'N/A',
  `other_names` varchar(45) DEFAULT NULL,
  `gender` enum('Female','Male') NOT NULL,
  `phone_number` varchar(45) NOT NULL DEFAULT 'N/A',
  `village_id` bigint(20) NOT NULL,
  `highest_educational_qualification` varchar(45) NOT NULL DEFAULT 'N/A',
  `home address` varchar(45) NOT NULL DEFAULT 'N/A',
  `guarantor_name` varchar(45) NOT NULL DEFAULT 'N/A',
  `guarantor_phone_number` varchar(45) NOT NULL DEFAULT 'N/A',
  `guarantor_address` varchar(45) NOT NULL DEFAULT 'N/A'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `harvest_repayment_centers`
--

CREATE TABLE `harvest_repayment_centers` (
  `repayment_center_id` bigint(20) NOT NULL,
  `repayment_center_name` varchar(45) NOT NULL DEFAULT 'N/A',
  `repayment_center_village_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `inputs`
--

CREATE TABLE `inputs` (
  `input_id` bigint(20) UNSIGNED ZEROFILL NOT NULL,
  `input_name` varchar(45) NOT NULL DEFAULT 'N/A',
  `input_price` decimal(27,3) NOT NULL DEFAULT 0.000
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `input_distribution_batches`
--

CREATE TABLE `input_distribution_batches` (
  `batch_id` int(11) NOT NULL,
  `batch_name` varchar(45) NOT NULL DEFAULT 'N/A'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `input_distribution_centers`
--

CREATE TABLE `input_distribution_centers` (
  `input_center_id` bigint(20) NOT NULL,
  `input_center_name` varchar(45) NOT NULL DEFAULT 'N/A',
  `input_center_lga_id` bigint(20) NOT NULL,
  `input_center_state_id` bigint(20) NOT NULL,
  `input_center_officer_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `input_distribution_officers`
--

CREATE TABLE `input_distribution_officers` (
  `input_officer_id` bigint(20) NOT NULL,
  `input_officer_name` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `registered_farmers`
--

CREATE TABLE `registered_farmers` (
  `farmer_id` bigint(20) NOT NULL,
  `first_name` varchar(45) NOT NULL DEFAULT 'N/A',
  `surname` varchar(45) NOT NULL DEFAULT 'N/A',
  `other_names` varchar(45) NOT NULL DEFAULT 'N/A',
  `phone_number` varchar(45) NOT NULL DEFAULT 'N/A',
  `gender` varchar(45) NOT NULL DEFAULT 'N/A',
  `address` varchar(45) NOT NULL DEFAULT 'N/A',
  `village_id` bigint(20) NOT NULL,
  `field_officer_id` bigint(20) NOT NULL,
  `farm_size(ha)` float(3,1) NOT NULL DEFAULT 0.0,
  `crop_id` bigint(20) NOT NULL,
  `farming_season` enum('wet','dry') NOT NULL,
  `trust_group_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `verified_famers`
--

CREATE TABLE `verified_famers` (
  `trust_group_id` bigint(20) NOT NULL,
  `farmer_id` bigint(20) NOT NULL,
  `verified_farm_size` int(11) NOT NULL,
  `time_of_verification` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `input_collection_day` varchar(100) NOT NULL,
  `field_officer_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ager_local_govts`
--
ALTER TABLE `ager_local_govts`
  ADD PRIMARY KEY (`lga_id`),
  ADD KEY `fk_from_state_for_lga_table_idx` (`state_id`);

--
-- Indexes for table `ager_states`
--
ALTER TABLE `ager_states`
  ADD PRIMARY KEY (`state_id`),
  ADD UNIQUE KEY `state_name_UNIQUE` (`state_name`);

--
-- Indexes for table `ager_villages`
--
ALTER TABLE `ager_villages`
  ADD PRIMARY KEY (`village_id`),
  ADD KEY `fk_from_localgovts_for_villages_idx` (`lga_id`);

--
-- Indexes for table `contract_agreement`
--
ALTER TABLE `contract_agreement`
  ADD KEY `fk_from_verified_farmers_for_contract_agrrement_idx` (`farmer_id`);

--
-- Indexes for table `crop_types`
--
ALTER TABLE `crop_types`
  ADD PRIMARY KEY (`crop_id`),
  ADD UNIQUE KEY `crop_name_UNIQUE` (`crop_name`);

--
-- Indexes for table `farmers_harvest_repayment_data`
--
ALTER TABLE `farmers_harvest_repayment_data`
  ADD PRIMARY KEY (`bag_id`),
  ADD UNIQUE KEY `bag_id_UNIQUE` (`bag_id`),
  ADD KEY `fk_from_verified_farmers_for_farmers_harvest_repayment_data_idx` (`farmer_id`);

--
-- Indexes for table `farmers_input_collection_data`
--
ALTER TABLE `farmers_input_collection_data`
  ADD PRIMARY KEY (`farmer_id`),
  ADD KEY `fk_from_input_distribution_batch_for_input_collection_data_idx` (`input_distribution_batch_id`),
  ADD KEY `fk_from_distribution_centers_for_input_collection_data_idx` (`distribution_center_id`),
  ADD KEY `fk_from_input_distribution_officers_for_input_collection_data` (`distribution_officer_id`);

--
-- Indexes for table `field_officers`
--
ALTER TABLE `field_officers`
  ADD PRIMARY KEY (`officer_id`),
  ADD KEY `fk_from_villages_for_fieldofficers_idx` (`village_id`);

--
-- Indexes for table `harvest_repayment_centers`
--
ALTER TABLE `harvest_repayment_centers`
  ADD PRIMARY KEY (`repayment_center_id`),
  ADD KEY `fk_from_ager_villages_for_harvest_repayment_centers_idx` (`repayment_center_village_id`);

--
-- Indexes for table `inputs`
--
ALTER TABLE `inputs`
  ADD PRIMARY KEY (`input_id`);

--
-- Indexes for table `input_distribution_batches`
--
ALTER TABLE `input_distribution_batches`
  ADD PRIMARY KEY (`batch_id`);

--
-- Indexes for table `input_distribution_centers`
--
ALTER TABLE `input_distribution_centers`
  ADD PRIMARY KEY (`input_center_id`),
  ADD KEY `fk_from_input_distribution_officers_for_input_distribution__idx` (`input_center_officer_id`),
  ADD KEY `fk_from_ager_states_for_input_distribution_centers_idx` (`input_center_state_id`),
  ADD KEY `fk_from_ager_local_govts_for_input_distribution_centers_idx` (`input_center_lga_id`);

--
-- Indexes for table `input_distribution_officers`
--
ALTER TABLE `input_distribution_officers`
  ADD PRIMARY KEY (`input_officer_id`);

--
-- Indexes for table `registered_farmers`
--
ALTER TABLE `registered_farmers`
  ADD PRIMARY KEY (`farmer_id`),
  ADD UNIQUE KEY `phone_number_UNIQUE` (`phone_number`),
  ADD KEY `fk_from_field_officers_for_registered_farmers_1_idx` (`field_officer_id`),
  ADD KEY `fk_from_crop_types_for_registered_farmers_1_idx` (`crop_id`),
  ADD KEY `fk_from_villages_for_registered_farmer_idx` (`village_id`);

--
-- Indexes for table `verified_famers`
--
ALTER TABLE `verified_famers`
  ADD PRIMARY KEY (`farmer_id`),
  ADD KEY `fk_from_field_officers_ for_verified_famers_idx` (`field_officer_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `ager_states`
--
ALTER TABLE `ager_states`
  MODIFY `state_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `ager_villages`
--
ALTER TABLE `ager_villages`
  MODIFY `village_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `crop_types`
--
ALTER TABLE `crop_types`
  MODIFY `crop_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `farmers_harvest_repayment_data`
--
ALTER TABLE `farmers_harvest_repayment_data`
  MODIFY `bag_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `field_officers`
--
ALTER TABLE `field_officers`
  MODIFY `officer_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `harvest_repayment_centers`
--
ALTER TABLE `harvest_repayment_centers`
  MODIFY `repayment_center_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `input_distribution_centers`
--
ALTER TABLE `input_distribution_centers`
  MODIFY `input_center_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `registered_farmers`
--
ALTER TABLE `registered_farmers`
  MODIFY `farmer_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `ager_local_govts`
--
ALTER TABLE `ager_local_govts`
  ADD CONSTRAINT `fk_from_states_for_localgovts_table` FOREIGN KEY (`state_id`) REFERENCES `ager_states` (`state_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `ager_villages`
--
ALTER TABLE `ager_villages`
  ADD CONSTRAINT `fk_from_localgovts_for_villages` FOREIGN KEY (`lga_id`) REFERENCES `ager_local_govts` (`lga_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `contract_agreement`
--
ALTER TABLE `contract_agreement`
  ADD CONSTRAINT `fk_from_verified_farmers_for_contract_agrrement` FOREIGN KEY (`farmer_id`) REFERENCES `verified_famers` (`farmer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `farmers_harvest_repayment_data`
--
ALTER TABLE `farmers_harvest_repayment_data`
  ADD CONSTRAINT `fk_from_verified_farmers_for_farmers_harvest_repayment_data` FOREIGN KEY (`farmer_id`) REFERENCES `verified_famers` (`farmer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `farmers_input_collection_data`
--
ALTER TABLE `farmers_input_collection_data`
  ADD CONSTRAINT `fk_from_distribution_centers_for_input_collection_data` FOREIGN KEY (`distribution_center_id`) REFERENCES `input_distribution_centers` (`input_center_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_from_input_distribution_officers_for_input_collection_data` FOREIGN KEY (`distribution_officer_id`) REFERENCES `input_distribution_officers` (`input_officer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `field_officers`
--
ALTER TABLE `field_officers`
  ADD CONSTRAINT `fk_from_villages_for_fieldofficers` FOREIGN KEY (`village_id`) REFERENCES `ager_villages` (`village_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `harvest_repayment_centers`
--
ALTER TABLE `harvest_repayment_centers`
  ADD CONSTRAINT `fk_from_ager_villages_for_harvest_repayment_centers` FOREIGN KEY (`repayment_center_village_id`) REFERENCES `ager_villages` (`village_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `input_distribution_centers`
--
ALTER TABLE `input_distribution_centers`
  ADD CONSTRAINT `fk_from_ager_lga_for_input_distri_centers` FOREIGN KEY (`input_center_lga_id`) REFERENCES `ager_local_govts` (`lga_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_from_input_distri_officers_for_id_centr` FOREIGN KEY (`input_center_officer_id`) REFERENCES `input_distribution_officers` (`input_officer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_from_states_for_input_dist_centers` FOREIGN KEY (`input_center_state_id`) REFERENCES `ager_states` (`state_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `input_distribution_officers`
--
ALTER TABLE `input_distribution_officers`
  ADD CONSTRAINT `fk_from_field_officers_for_input_distribution` FOREIGN KEY (`input_officer_id`) REFERENCES `field_officers` (`officer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `registered_farmers`
--
ALTER TABLE `registered_farmers`
  ADD CONSTRAINT `fk_from_crop_types_for_registered_farmers_1` FOREIGN KEY (`crop_id`) REFERENCES `crop_types` (`crop_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_from_field_officers_for_registered_farmers_1` FOREIGN KEY (`field_officer_id`) REFERENCES `field_officers` (`officer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_from_villages_for_registered_farmer` FOREIGN KEY (`village_id`) REFERENCES `ager_villages` (`village_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `verified_famers`
--
ALTER TABLE `verified_famers`
  ADD CONSTRAINT `fk_from_field_officers_ for_verified_famers` FOREIGN KEY (`field_officer_id`) REFERENCES `field_officers` (`officer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_from_registerd_farmers_for_verified_famers` FOREIGN KEY (`farmer_id`) REFERENCES `registered_farmers` (`farmer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
