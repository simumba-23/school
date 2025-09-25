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

Authentication: Role-based access (Principal, Academic Master, Teacher, Student, Parent)

⚡ Installation
# Clone repo
git clone https://github.com/yourusername/school-management-system.git
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
