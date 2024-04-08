-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema belt_exam
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `belt_exam` ;

-- -----------------------------------------------------
-- Schema belt_exam
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `belt_exam` DEFAULT CHARACTER SET utf8 ;
USE `belt_exam` ;

-- -----------------------------------------------------
-- Table `belt_exam`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `belt_exam`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `correo` VARCHAR(45) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `belt_exam`.`appointments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `belt_exam`.`appointments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `task` VARCHAR(255) NULL,
  `date` DATE NULL,
  `status` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `usuario_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_appointments_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_appointments_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `belt_exam`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
