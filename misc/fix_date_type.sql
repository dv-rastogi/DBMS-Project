use cp-stats;
alter table users modify DateOfBirth datetime;
alter table users modify DateOfJoining datetime;
alter table premium_users modify Subscription_Time_Start datetime;
alter table premium_users modify Subscription_Time_End datetime;
alter table repository modify `Date` datetime;
alter table contests modify DateOfContest datetime;
alter table `groups` modify DateOfFormation datetime; 
alter table recruiters modify DateOfJoining datetime;
alter table member_of modify DateOfJoining datetime;
alter table solved modify `Date` datetime;
alter table registered modify DateOfJoining datetime;
alter table recruited modify DateOfRecruitment datetime;
alter table premium_users_paysto modify DateOfPayment datetime;
alter table organisation_paysto modify DateOfPayment datetime;
alter table blocks modify Date_Unblock datetime;

-- Need to perform at the end (Drop constraint first)
alter table blogs modify `Date` datetime;
alter table blogs_tags modify `Date` datetime;
alter table contests modify `Date` datetime;
alter table contest_tags modify `Date` datetime;
