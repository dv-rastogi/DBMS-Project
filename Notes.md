# Meetings & Notes

## Meeting 1 | *Jan 14*

#### Points to cover
* ~~Requirements~~
* Ideas | Done - Codeforces, Restaurant, Shopping Cart
* ~~Repo~~
* ~~TechStack~~
* Distribution Kinda?? | Done
	- Layout
	- ER Diagram
	- Web Dev
	- SQL 
* TechStack for project | **TODO Django for now https://www.youtube.com/watch?v=F5mRW0jo-U4, SQL**
	
### Questions:
> When should we be done with the sql part?
	
### Ideas:
	CODEFORCES | CP Platform
		>> Stakeholders : 
			Participants, Admin, Contest Organizer, Testers, Third-party recruiters
		> Participants
			- ID, institution
			- Rating
			- Friends
			- Past contests
			- Upcoming contests
			- Problems solved
			- Contribution
		> Contest Organizer ; extends Participant
			- Date of contest
			- Maximum language used
			- Questions attributes
			- Submission stats
				- Test cases pass/failed
				- Difficulty of the problem
			- In contest queries
			- Plag check
			- Registrations
		> Testers ; extends Participant
			- Question attributes
			- Submission stats
				- Test cases pass/failed
				- Difficulty of the problem
		> Admin ; extends everything
			- ID
			- Contest Organizers
			- Total participants, total contest .., total testers, total contests, ....
			- Revenue generated
		> Third-party recruiters
			- Prizes
			- Winners
			- Registrations
			- Ads revenue
			- Attraction
	
	
---
<br>

## Meeting 2 | *Jan 23*

#### Points to cover
* Refining Idea
* Decide attributes & entities..?

> Talked to archit bhaiya, need a *lot* of refinement on idea

### Ideas:
	General Programming Platform, Codeforces and Leetcode
		- Codeforces and leetcode data
		- Premium Users
		- Friends
		- Comparator between users
		- a todo list
	
#### Resources
	https://meet.google.com/linkredirect?authuser=0&dest=https%3A%2F%2Fleetcode.com%2Fapi%2Fproblems%2Falgorithms%2F
	https://github.com/nomikura/atcoder-api (api for atcoder)
	
---
<br>

## Meeting 3 | *Jan 26, 27, Feb 3*

### Ideas (Refined)
	NAME OF WEBSITE: C0deb00k

	MAIN IDEA:
	If you sign in as user:
	Programming Statistics (One stop for all cp stats) and Discussion Platform, Stats from Codeforces and Leetcode, See how people code / custom repo (setups, saving questions and solutions) (Blog oriented and code oriented) & meeting like minded people, report people, forming groups, premium users (?? benifits, notifications for contests, profile visits), we can show user experience like he has done graphs a lot like basically stats. Search like github. Like minded people form groups together, Give a contest in a group, tasks, LOCKOUT. Followers and following people, so like github follow.
	
	If you sign in as a recruiter you can see strenghts and language of users, do user comparison, location of users. 

	If you sign in as an org., org. can post contests, can see their users, sort users on ratings, location of users, premium organization (surveys, oranization standings, ads of organization).

	If you sign in as admin, revenue, ban users, do user comparison, show ads, how many users have joined, have left, inactive, add contests, add blogs, see premium users, see groups

	KEY:
	!! means its a utility / class
	?? means its optional
	^^ means its an action
	[[]] denotes the visibility scope
	&C means its composite attribute
	&D means its a derived attribute
	&Co means its a complex attribute
	// its a general comment

	PARAMETERS & QUERIES:
		User:
			* Parameters:
				- Identity !!
				- Premium / Non premium ?? (Boolean value)
					If premium
					- Check profile visits
					- Check blog reads
					- Notification for contests ??
					- User comparison
				- Codeforces ID, Leetcode ID (A seperate table)
					- Rating 
					- Problems Solved !!
					- Tags
					- Difficulties of problems
					- Past contests ??
				- Language (User inputs)
				- Blogs !!
				- Comments / Likes ??
				- Groups
				- Trust rating [[ Admin ]]
				- User experience (Strength & Weakness) (&D from problems)
				- Following people & followers
				- Repo(s) !!
			* Queries:
				- What are my strenghts & weaknesses
				- How many problems have I solved
				- Difficulties of the problems I have solved
				- Give me repos of certain tag
				- User comparison (premium)
				- Check my profile visits (premium)

		Group Admin "extends" User:
			* Parameters:
				- Group !! [[group admin, group members, admin]]
				- Pending Requests !! (User) [[group admin, admin]]
			* Queries:
				- Remove Users ^^

		Recruiter:
			* Parameters:
				- Identity !!
				- list of preferred User !!
			* Queries:
				- Location
				- Query for preferred users
		// access to database

		Programming Organization:
			* Parameters:
				- Identity !!
				- Contests !!
				- Premium / Non Premium ?? 
					If premium
						- Ads
						- Surveys ?? 
			* Queries:
		// don't keep a copy of Users here
		Admin:
			* Parameters:
				- Identity !!
				- Revenue
			* Queries:
				- Who all are premium users

	UTILITIES:
		Problems:
			- Problem ID
			- Rating
			- Tag
			- Solves
			- Name
			- Codeforces/Leetcode (&D from Problem ID)
		Identity &C
			- ID NO [[admin, self]]
			- Username
			- Password
			- Name &C
				- FirstName, LastName
			- DOB &C
				- Date, Month, Year
			- Location &Co ??
			- School/College/Company Name
			- Email [[self, recruiter, admin]]
		Repo
			- User !!
			- Name like graphs
			- Date
			- Templates
				- Name
				- Language
			- TodoList
				- Problems !!
			- Favourites
				- Problems !!
				- Solutions
					- Author
					- Language (User inputs)
		Blogs
			- Name
			- Date
			- User !!
			- Tag
			- Content
			- Comments / Likes ?? 
		Contest
			- Programming Organization name
			- Name 
			- Date
			- Date of contest
			- Content
		Group
			- Group Name
			- Group size
			- Date of formation
			- Group admin !!
			- Group members (Users !!)
			- Average rating ??
			- Blogs

#### Tasks
* Anoushka, Ritik & Divyansh : Flask, Create utilities to call a python fn and print its contents
* Ritik, Divyansh: How to utilize API of leetcode and codeforces from code, retrieve a JSON
* Ramit, Divyansh, Gurjot: MySQL
* Gurjot : UI
#### Motivation
* https://cfviz.netlify.app/
* https://www.stopstalk.com/
* Codeforces blogs ...

#### Resources
	Flask : https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
	API: https://www.dataquest.io/blog/python-api-tutorial/
	Codeforces API: https://codeforces.com/blog/entry/12520
	Lockout bot: https://github.com/pseudocoder10/Lockout-Bot

#### TODO
	Complete PARAMETERS AND QUERIES


---
<br>

## Meeting 4 | *Feb 7*

#### Points to cover & todo
* Decide entities and relationships
* Refer week 2 slides, look for concepts

#### Material
* https://www.tutorialspoint.com/dbms/dbms_indexing.htm 
* https://github.com/rhythm-3099/Codehorses-database-system
* Sample projects
- https://github.com/shash42/Online-University-Database/blob/main/phase_docs/phase1.pdf (Read relationships)
- https://github.com/Groverkss/Dota2-Analyzer/blob/main/Phases/Project_Phase_-_I.pdf
- https://github.com/rhythm-3099/Codehorses-database-system

#### Key points noticed
* Derived attributes on the basis, that if it's frequently queried, we shoudn't keep it derived.
* Codeforces & Leetcode will be kept as seperate tables which are visible to coding organizations and they will be kept as a seperate relation table (https://stackoverflow.com/questions/163434/are-nulls-in-a-relational-database-okay/246621#:~:text=33%20Answers&text=Nulls%20are%20negatively%20viewed%20from,data%20is%20valid%20and%20valued.). Relation from user to a programming platform.
* User to Repo is one to many relationship. Repo has user's primary key.
* Search queries based on language (C++, Java ..)
* Groups and user have many to many relationships. (relationship table with attribute as admin)
* Group admin specializes from User
* 'Roles' followers and following
* Blog tables consists of primary key writer, primary key: User id + Blog id
* Tags tablee would be linked with Codeforces and Leetcode table ?? (Indexing)
* A blog would have a tag and problem would have a tag
* Solves would be a relation between Problems and User with verdicts, Language as attributes
* Premium & Non premium would be a seperate table (Indexing)
* Pending relationships is a one to many relationship from group admin to user
* list of preferred User is a one to many relationship from recruiter to user

#### Entities

* STRONG ENTITIES:
- User
- Group admin (specializes User)
- Programming organization
- Problem ?? (Maybe a weak entity)
- Recruiter
- Admin

* WEAK ENTITES:
- Group (User)
- Blog (User)
- Repos (User)
- Contest (Programming organization) (Specializes from blog)
- Tag (Blog, Problem, Strenghts and weaknesses, Repos)

* RELATIONSHIPS:
User - Programming Organization (Many to many)
Tags - Problems (Many to Many)
