CREATE TRIGGER `member_of_AFTER_INSERT` AFTER INSERT ON `member_of` FOR EACH ROW BEGIN
IF (new.Group_ID) THEN
UPDATE `groups` SET Size= Size + 1  Where Group_ID = new.Group_ID ;
END IF; 
END

CREATE TRIGGER `member_of_BEFORE_DELETE` BEFORE DELETE ON `member_of` FOR EACH ROW BEGIN
UPDATE `groups` SET Size= Size - 1  Where Group_ID=old.Group_ID;
END

CREATE TRIGGER `users_AFTER_UPDATE` AFTER UPDATE ON `users` FOR EACH ROW BEGIN
IF (new.TrustRating < 50) THEN
Insert into blocks Values (old.ID, 'General', date_add(now(), INTERVAL +  1 month));
END IF;
END