# Zolfa Online Learning Platform

This is a Django and Django Rest Framework-based online learning platform that allows students to enroll in different intakes and levels, take exams, and learn from various subjects and lessons. The platform also includes a supervisor module, where supervisors are assigned specific permissions based on their roles.


# Features

The online learning platform includes the following features:

* __Intakes and Levels__ : Students are enrolled in different intakes and levels based on their academic progress. The platform allows administrators to create and manage intakes and levels.
* __Subjects and Lessons__ : The platform offers various subjects and lessons for students to learn. Each subject includes multiple lessons, and students can track their progress.
* __Exams__ : Each subject has its own exams that students can take to test their knowledge and skills. Students can view their exam results and receive feedback.
* __Supervisors__ : The platform includes a supervisor module that allows supervisors to manage students, exams, and lessons. Supervisors are assigned specific permissions based on their roles.




# Setup

To set up the online learning platform, follow these steps:

1.Clone the repository and navigate to the project directory:

git clone https://github.com/husseinhn7/Zolfa.git
cd Zolfa 

2.Create a virtual environment and activate it: 

python -m venv env
source env/bin/activate

3.Install the required packages: 

pip install -r requirements.txt

4.Create the database tables:

python manage.py migrate




# Supervisor Permissions 

The following permissions are available for supervisors:

* __View Students__ : Supervisors can view students' profiles, including their intake, level, and exam results.

* __Manage Students__: Supervisors can create, update, and delete students' profiles.

* __Manage Exams__: Supervisors can create, update, and delete exams.

* __Manage Lessons__: Supervisors can create, update, and delete lessons.











