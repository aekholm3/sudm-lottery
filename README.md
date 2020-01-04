# DO NOT PUSH ATTENDEES OR TRANSACTIONS FILE TO GITHUB

**TO USE THIS CODE:**

- Clone repository onto local

- Download attendees file and transactions file and place in same directory as handler.py (this will be the directory of the cloned respository). important to make sure that the column that shows how much someone has raised is in column 13 (indexing from 0), otherwise, you need to change the variable `TOTAL_RAISED_COL`. Same thing for the referred column. A sample schema for the attendees csv is included in the repository. 

- Rename variable `ATTENDEES_FILE` in handler.py to be the name of the new attendees file

- From command line `python3 handler.py`


**TODO:**

- The process of adding a raffle ticket for a referral is a little janky, could be fixed up a bit
