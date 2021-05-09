# Cowin-keep-alive
Keep Cowin Logged In and Refreshed for immediate scheduling with the help of Selenium! 

Use case: You are already using exisiting Cowin notification bots, but you are unable to login on time for scheduling your vaccine. 

# Requirements:

1. Make sure you have one of the latest versions of [Python](https://www.python.org/downloads/) installed
2. Install Selenium: `pip install selenium`


# Configuration (Make the necessary changes in the app.py file):

```
phone = xxxxxxxxxx      -> 10 Digits, no zeros and no +91
age_grp = '18'          -> Type either '18' or '45' or 'Both'
vaccine = 'Both'        -> 'Covishield' or 'Covaxin' or 'Both'
state = 'Karnataka'     -> Make sure the spelling is right
district = 'BBMP'       -> Make sure the spelling & casing is right
dose = 2                -> 1 or 2
pos = 1                 -> Position: 1, 2, 3 or 4 according to the order of the benefitiaries registered in your account 
refresh_delay = 120     -> in seconds
```

