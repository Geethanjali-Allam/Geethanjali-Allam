## SQL QUERIES
- Retrieve All Employees:
    - QUERY - ```SELECT * FROM Management_employee; ```
    - RESULTS - ```<p>sqlite> SELECT * FROM Management_employee;
        1|Tushar Kasana|tusharguys@gmail.com|Tushar@123|Manager|65000
        2|Parth Sharma|rapstar907@gmail.com|Parth@123|J. Manager|9000
        3|Rishabh Sen|rishabhsen987@gmail.com|Rishabh@123|Manager|10000
        4|Prateek|prateek.pr29@gmail.com|Prateek@123|S. Manager|12000
        6|Django|yoyoyoyo@gmail.com|Django@123|CEO|50000
        7|Ritik Kumar|ritikkumar20511@gmail.com|Ritik@123|Manager|10000
        8|Prateek Sharma|prateeksharma@gmail.com|PrateekS@123|J. Manager|9000
        9|Prateek Sharma|prateeksharma2@gmail.com|PrateekS1@123|S. Manager|12000
        10|Tushar Singh|tusharsingh@gmail.com|TusharS@123|Manager|10000
        11|Anshul Kumar|anshulsingh@gmail.com|Anshul@123|Accountant|7000
        15|Garvit Joshi|garvitjoshi9@gmail.com|Garvit@123|Developer|5000000
        16|YO|yoyo@lpu.in|yoyo@123|Accountant|123
        17|Geethanjali|Geetha@123.com|Geetha@123|Senior Manager|150000
        18|John Doe|john.doe@example.com|password123|Manager|60000
        19|John Doe|john.doe@example.com|hashed_password|Manager|60000
        20|Jane Smith|jane.smith@example.com|hashed_password|Developer|50000 </p>```
- Retrieve Specific Employee
  - QUERY - ```SELECT * FROM Management_employee WHERE id = 1;```
  - RESULT-```1|Tushar Kasana|tusharguys@gmail.com|Tushar@123|Manager|65000```
- Retrieve Employees with a Certain Position
  - QUERY - `` SELECT * FROM Management_employee WHERE Position = 'Developer'; ``
    - RESULT- `` 15|Garvit Joshi|garvitjoshi9@gmail.com|Garvit@123|Developer|5000000
                20|Jane Smith|jane.smith@example.com|hashed_password|Developer|50000``
- Retrieve Employees with Salary Greater Than a Value
    - QUERY- ``SELECT * FROM Management_employee WHERE Salary > 50000;``
    - RESULT- ``1|Tushar Kasana|tusharguys@gmail.com|Tushar@123|Manager|65000
                  15|Garvit Joshi|garvitjoshi9@gmail.com|Garvit@123|Developer|5000000
                  17|Geethanjali|Geetha@123.com|Geetha@123|Senior Manager|150000
                  18|John Doe|john.doe@example.com|password123|Manager|60000
                  19|John Doe|john.doe@example.com|hashed_password|Manager|60000``
- Retrieve Latest N Records from the Admin Log
  - QUERY- ``SELECT * FROM django_admin_log ORDER BY action_time DESC LIMIT 10;``
    - RESULT-``16|2023-01-02 14:30:00||Jane Smith|Modified user Jane Smith||1|2
                15|2023-01-01 12:00:00||John Doe|Created user John Doe||1|1
                14|2022-09-12 05:25:58.755337|6|6: Django is CEO with salary of 50000. Email:yoyoyoyo@gmail.com and Password:Django@123|[{"changed": {"fields": ["Name", "Email", "Password"]}}]|7|1|2
                13|2022-09-12 05:25:15.627658|15|15: Garvit Joshi is Developer with salary of 5000000. Email:garvitjoshi9@gmail.com and Password:Garvit@123|[{"changed": {"fields": ["Position", "Salary"]}}]|7|1|2
                12|2022-09-12 05:24:47.048760|16|16: YO is Accountant with salary of 123. Email:yoyo@lpu.in and Password:yoyo@123|[{"changed": {"fields": ["Name", "Email"]}}]|7|1|2
                11|2022-09-12 05:24:26.168489|16|16: Garvit Joshi is Accountant with salary of 123. Email:garvit.11808472@lpu.in and Password:yoyo@123|[{"changed": {"fields": ["Password"]}}]|7|1|2
                5|2020-11-07 12:06:31.903474|9|9: Prateek Sharma is S. Manager with salary of 12000. Email:prateeksharma2@gmail.com and Password:PrateekS1@123|[{"added": {}}]|7|1|1
                4|2020-11-07 12:05:45.036294|8|8: Prateek Sharma is J. Manager with salary of 9000. Email:prateeksharma@gmail.com and Password:PrateekS@123|[{"added": {}}]|7|1|1
                3|2020-11-07 11:34:04.247563|7|7: Ritik Kumar is Manager with salary of 10000. Email:ritikkumar20511@gmail.com and Password:Ritik@123|[{"added": {}}]|7|1|1
                2|2020-11-07 11:33:21.204619|5|5: Ritik Kumar is Manager with salary of 10000. Email:ritikkumar24511@gmail.com and Password:Ritik@123||7|1|3``

        
