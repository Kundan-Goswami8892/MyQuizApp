This project is purely made by the students of <b>SARASWATI VIDYA MANDIR SENIOR SECONDARY SCHOOL, D-1 KAMLA NAGAR, AGRA</b>.
This project is also the first and fresh from <b>"Team Radium"<b>.

Staffs of TEAM RADIUM:
- Kundan Goswami  (Head Developer, Backend developer, Student of class 12th C)
- Divyanshu Jaiswal (Database Manager, Student of class 12th C)
- Gurupreet Singh (Frontend developer, Interface developer, Student of class 12th C)

# About the project
In this project, we TEAM RADIUM, presenting you a quiz app with a login interface. This app is accessible to 3 different types of users (Students, Admins, Moderators).
## Students
They just simply log in and submit there quiz. everytime they log in, system checks for any new updates by the morderators or Admins. Exams and Test can be held by any mods or admins. They can report any suspecious activity.
## Teacher
They can add new quizes, push quizes for the next test or exams to mods. Have power to ban, unban, mute, add, delete any student's ID if they have to.
## Moderators
They can promote any student account to an admin account and vice-versa. they have every moderation right. they define new test/exam format with the help of quizes pushed by admins. They can send private messages to any admin/students while being annonymous.

# What's missing?
1. <b>Server connectivity</b> :-  Even though this app is capable of storing user data though SQL, this app is not capable of connecting those data thougher in a server.
- Why?
creating a server port may not be that hard. But, it comes up with high risk of getting server data leaked, high load on the main host, and might easily crash as this app does not consist multiple threads running in the background. 
2. <b>Crash protection</b> :- If your system crashesh while using the app, your data might corrupt, or get lost.
- Why?
It's possible to debug crashesh, but it makes the code more complex and takes time to create such a debugger. Since we are creating this app purely though human intelligence, using AI is <b>NOT</b> an option here.
3. <b>Global OS approach</b> :- This app may not be able to run on mac or linux, as the codes are ment to run on Windows, and is not excpected to run on other platforms.
- Why?
Fixing this problem is one another of an advance problem. It is also fixable, but it also means "writing the code for the same task more that one times". which might make this project complex and harder to maintain. New updates and bug fixes can become much more expensive than usual on time.
===
# Project info
- <b>AIM :- </b> To create a quiz app with a login interface.
- <b>Requirement :- </b> (Minimum requirements)
1. Operating system :- Windows 7, 32xbits
2. Free space :- 10MB (including 8MBs of processing area and uploadable files.)
3. RAM :- 1GB
4. Software :- Python.exe 3.13, Pip.exe 3.13, MySQL.
5. Launcher :- VS Code, IDLE 3.13