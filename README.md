# Cowin-keep-alive
Keep Cowin Logged In and Refreshed for immediate scheduling with the help of Selenium! 

# Use case
You are already using exisiting Cowin notification bots, but you are unable to login on time for scheduling your vaccine. 

## Contents
<!--ts-->
   * [Cowin-keep-alive](#Cowin-keep-alive)
   * [Use case](#use-case)
   * [Contents](#contents)
   * [Requirements](#requirements)
   * [Configuration](#configuration)
   * [Run](#run)
   * [What to do when you find a slot open?](#what-to-do-when-you-find-a-slot-open?)
   * [Caution](#caution)
<!--te-->



# Requirements:

1. Make sure you have one of the latest versions of [Python](https://www.python.org/downloads/) installed
2. Install Selenium: `pip install selenium`
3. Chrome browser installed
4. Tested only on Windows in v1. For mac/linux, change the path of the chromedriver accordingly.


# Configuration:
Make the necessary changes in the app.py file
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

## Run

1. Clone this repository or download the zip file and extract.
2. Run `python app.py` in Windows Powershell or Mac/Linux terminals
3. Enter the OTP in the Windows Powershell window or Mac/Linux terminals when prompted
4. Sit back and watch the bot keep your cowin alive till a slot opens up.

## What to do when you find a slot open?
1. Terminate the bot immediately so that it does not refresh when you are selecting your vaccine slot.

## Caution

1. Do not minimize the chrome window, the process will fail and you would have to start over again.
2. Make sure you enter the OTP in the Windows Powershell window or Mac/Linux terminals when prompted, otherwise there is no point in using the bot.
