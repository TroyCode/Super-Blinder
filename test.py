import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--test', default='ghdgdf')
args = parser.parse_args()
print args.test

CREATE TABLE `SuperBlinder`.`youtube_channel` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '',
  `type_id` INT NULL COMMENT '',
  `name` VARCHAR(45) NOT NULL COMMENT '',
  `description` TEXT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  UNIQUE INDEX `id_UNIQUE` (`id` ASC)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;
