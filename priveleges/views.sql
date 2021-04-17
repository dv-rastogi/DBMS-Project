USE `cp-stats`;

DROP VIEW IF EXISTS USER_STRENGTH ;
CREATE VIEW USER_STRENGTH AS 
SELECT User_ID, Tag, IF(COUNT(*) > 50, "Strength", IF(COUNT(*) < 10, "Weakness", "Ok")) AS Category FROM solved, problems_tags WHERE solved.Problem_ID=problems_tags.Problem_ID GROUP BY User_ID, Tag;

DROP VIEW IF EXISTS FOLLOWERS;
CREATE VIEW FOLLOWERS AS
SELECT Following_ID, COUNT(*) AS Followers FROM following GROUP BY Following_ID ORDER BY Following_ID ASC;

DROP VIEW IF EXISTS PREMIUM_AMOUNT_PAID;
CREATE VIEW PREMIUM_AMOUNT_PAID AS
SELECT Premium_User_ID, SUM(AmountPaid) AS total_amount_paid FROM premium_users_paysto GROUP BY Premium_User_ID ORDER BY Premium_User_ID;

DROP VIEW IF EXISTS PROBLEM_SOLVED_COUNT;
CREATE VIEW PROBLEM_SOLVED_COUNT AS
SELECT res.Problem_ID as ID, Name, Rating_Difficulty, no_of_solves  FROM problems, (SELECT Problem_ID, COUNT(*) AS no_of_solves FROM solved GROUP BY Problem_ID ORDER BY Problem_ID ASC) res WHERE res.Problem_ID=problems.Problem_ID;

DROP VIEW IF EXISTS ADMIN_ROLE_REVENUE;
CREATE VIEW ADMIN_ROLE_REVENUE AS
SELECT Admin_Role, SUM(AmountPaid) AS Revenue_Generated FROM premium_users_paysto GROUP BY Admin_Role ORDER BY Revenue_Generated ASC;

DROP VIEW IF EXISTS UPCOMING_CONTESTS;
CREATE VIEW UPCOMING_CONTESTS AS
SELECT * FROM CONTESTS WHERE DateOfContest > NOW() AND DateOfContest < DATE_ADD(NOW(), INTERVAL 10 DAY);

DROP VIEW IF EXISTS INCREASE_IN_PREMIUM_USERS;
CREATE VIEW INCREASE_IN_PREMIUM_USERS AS
SELECT r1.INCREASE / r2.INCREASE as INCREASE FROM
(SELECT COUNT(*) AS INCREASE FROM premium_users WHERE Subscription_Time_Start > DATE_ADD(NOW(), INTERVAL -1 YEAR)) r1, 
(SELECT COUNT(*) AS INCREASE FROM premium_users WHERE Subscription_Time_Start < DATE_ADD(NOW(), INTERVAL -1 YEAR)) r2;

DROP VIEW IF EXISTS INCREASE_IN_REGISTERED;
CREATE VIEW INCREASE_IN_REGISTERED AS
SELECT r1.Programming_Organisation_ID, r1.AF / r2.BEF as INCREASE FROM
(SELECT Programming_Organisation_ID, COUNT(*) AS AF FROM registered WHERE DateOfJoining > DATE_ADD(NOW(), INTERVAL -1 YEAR) GROUP BY Programming_Organisation_ID) r1,
(SELECT Programming_Organisation_ID, COUNT(*) AS BEF FROM registered WHERE DateOfJoining < DATE_ADD(NOW(), INTERVAL -1 YEAR) GROUP BY Programming_Organisation_ID) r2
WHERE r1.Programming_Organisation_ID = r2.Programming_Organisation_ID;
