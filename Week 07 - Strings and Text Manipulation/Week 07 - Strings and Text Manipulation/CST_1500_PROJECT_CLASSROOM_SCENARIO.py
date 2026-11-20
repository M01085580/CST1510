#Classroom Scenario: Campus IT Helpdesk Ticket Analyzer
#The Problem: Students and faculty submit support tickets to the IT department, 
# but the raw data arriving from the web portal is messy. It contains random whitespace, 
# inconsistent capitalization, square brackets around priorities, and uneven comma-separated 
# details.
 
#Write a Python script that integrates all parts of our string manipulation 
# curriculum into a single automated pipeline.
 


support_tickets = [
   " i miss my MOMMY   ",
   "how do I reset my password?   ",
   "   I can't LOG in to my account.   ",
   "   my cOMPUTER is overheating!   ",
   "   library printER is jammed.   ",
   "I WILL BE ARRIVING LATE TO CLASS   ",
   "   my monITOR is flickering.   ",
   "  I need hELP with my email account.        ",
    ]


for s in support_tickets:
   s = s.strip().lower().title()
   print(s)


   

 


