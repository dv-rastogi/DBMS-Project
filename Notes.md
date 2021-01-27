# Notes

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
	
===

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
	
===

## Meeting 3 | *Jan 26*

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

	PARAMETERS & QUERIES:
		User:
			* Parameters:
				- Identity !!
				- Premium / Non premium
					If premium
					- Check profile visits
					- Check blog reads
					- Notification for contests ??
					- User comparison
				- Codeforces ID, Leetcode ID
					- Rating 
					- Problems Solved !!
					- Languages (User inputs)
					- Tags
					- Difficulties of problems
				- Blogs !!
				- Comments / Likes ??
				- Groups
				- Trust rating
				- User experience (Strength & Weakness)
				- Following people & followers
			* Queries:

		Group Admin:
			* Parameters:
			
			* Queries:

		Recruiter:
			* Parameters:
			
			* Queries:

		Programming Organization:
			* Parameters:
			
			* Queries:

		Admin:
			* Parameters:
			
			* Queries:

	UTILITIES:
		Problems:
			- Rating
			- Tag
			- Solves
			- Name
			- Codeforces/Leetcode
		Identity
			- ID NO
			- Username
			- Name
			- Location
			- School/College
		Repo
			- Templates
				- Name
				- Language
			- TodoList
				- Problems !!
			- Favourites
				- Problems !!
				- Solutions (User inputs)
		Blogs
			- Name
			- Date
			- User !!
			- Tag
			- Content
			- Comments / Likes ?? 
		Group
			- Group Name
			- Group size
			- Date of formation
			- Group admin !!
			- Group members (Users !!)
			- Average rating
			- Blogs

#### Tasks
* Anoushka, Ritik & Divyansh : Flask, Create utilities to call a python fn and print its contents
* Ritik, Divyansh: How to utilize API of leetcode and codeforces from code, retrieve a JSON
* Ramit, Divyansh: MySQL

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
