🎓 Secondary School Management System

A role-based Django + PostgreSQL application for managing secondary school operations.
It supports Academic Masters, Teachers, Students, Parents, and the Principal, each with a separate set of features.

🚀 Features
📚 Academic Master Panel

👨‍🎓 Register new students into the system.

📖 Assign subjects and classes to teachers.

📊 Manage subject allocations per class.

📈 Generate reports on student registrations.

👨‍🏫 Teacher Panel

📝 Upload student results for assigned subjects.

⏰ Submit leave permission requests to the principal.

📊 View subject-wise student performance reports.

👨‍👩‍👦 Student & Parent Panel

📝 Request leave permissions (students/parents).

📊 View results uploaded by teachers.

📈 Track academic performance progress over time.

🏫 Principal Panel

📊 View registration reports of students.

👥 Register and manage staff members.

🔑 Manage permissions for staff, academic masters, and teachers.

✅ Approve/reject leave requests from teachers and students.

📈 Generate school-wide performance and attendance reports.

🔄 Workflow

Student Registration: Academic Master registers students.

Teacher Assignment: Academic Master assigns teachers subjects & classes.

Result Upload: Teachers upload results → Students & Parents can view.

Leave Requests:

Teachers request leave → Principal approves/rejects.

Students/Parents request leave → Principal approves/rejects.

Reports:

Academic Master generates registration reports.

Principal generates academic & performance reports.

🛠 Tech Stack

Backend: Python Django

Database: PostgreSQL

Frontend: Django Templates + Bootstrap

Authentication: Role-based access (Principal, Academic Master, Teacher, Student or Parent)
# Screenshots
<img width="1357" height="633" alt="School login" src="https://github.com/user-attachments/assets/59a2e7be-fc7c-43e1-b9aa-386b481a6f94" />
<img width="1328" height="630" alt="school admin side" src="https://github.com/user-attachments/assets/208a497c-09d9-4eb4-b7a7-db192db6453c" />
<img width="1355" height="645" alt="student registration" src="https://github.com/user-attachments/assets/e857a17c-9a8c-4d8a-acc3-424e1c2ba6d3" />
<img width="1343" height="633" alt="school subjects" src="https://github.com/user-attachments/assets/7a71b0dd-8a3d-4c0b-a15c-55a86329ea1f" />
<img width="1353" height="614" alt="SCHOOL RESULTS" src="https://github.com/user-attachments/assets/5e42e9b4-0848-4686-b0e7-f61604bf2d28" />
<img width="1077" height="496" alt="School results upload" src="https://github.com/user-attachments/assets/a0af5f2e-8c7e-4fb7-9344-7ae519ae5747" />
<img width="1098" height="540" alt="assign subject" src="https://github.com/user-attachments/assets/22d02197-b414-4e33-b622-3de804297a94" />
<img width="1111" height="544" alt="school class" src="https://github.com/user-attachments/assets/1bf4ef4e-dcc2-4f38-a344-2e336855fc0f" />
⚡ Installation
# Clone repo
git clone git@github.com:simumba-23/school.git
cd school

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup database
python manage.py migrate
python manage.py createsuperuser

# Run server
python manage.py runserver

📊 Future Improvements

📱 Mobile app for parents and students to track results.

📧 Email/SMS notifications for results and leave approvals.

📈 Advanced analytics for performance tracking.

👨‍💻 Author

Built by Emansi Simumba
