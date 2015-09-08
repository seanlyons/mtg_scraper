USE seandb;

CREATE TABLE IF NOT EXISTS `mtg_card_lookup` (
    `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(50) DEFAULT "",
    `edition` INT,
    `foreign_id` INT,
    `rarity` TINYINT DEFAULT 0,
    PRIMARY KEY `id` (`id`)
) ENGINE=InnoDB;


CREATE TABLE IF NOT EXISTS `mtg_editions` (
    `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
    `acronym` VARCHAR(10) DEFAULT "",
    `full_name` VARCHAR(200) DEFAULT "",
    PRIMARY KEY `id` (`id`)
) ENGINE=InnoDB;