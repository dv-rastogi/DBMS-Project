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
	

