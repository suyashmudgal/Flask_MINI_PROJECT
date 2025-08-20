# 📋 TaskFlow - Task Management Application

![TaskFlow Banner](https://img.shields.io/badge/TaskFlow-Task%20Management-blue?style=for-the-badge&logo=flask)

**TaskFlow** is a modern, intuitive task management web application built with Flask. It helps you organize, prioritize, and track your daily tasks efficiently with a clean and responsive user interface.

## ✨ Features

### 🎯 Core Functionality
- **User Authentication** - Secure signup, login, and logout
- **Task Management** - Create, edit, delete, and organize tasks
- **Priority System** - Set task priorities and due dates
- **Status Tracking** - Mark tasks as completed or pending
- **Dashboard** - Clean overview of all your tasks

### 🎨 User Experience
- **Responsive Design** - Works seamlessly on desktop, tablet, and mobile
- **Modern UI** - Clean and intuitive interface with professional styling
- **Flash Messages** - User-friendly feedback for all actions
- **Dynamic Homepage** - Different experience for guests vs authenticated users

### 🔒 Security
- **Password Hashing** - Secure password storage using Werkzeug
- **Session Management** - Flask-Login for secure user sessions
- **CSRF Protection** - Built-in protection against cross-site request forgery
- **Input Validation** - Form validation using Flask-WTF

## 🛠️ Technology Stack

- **Backend**: Python 3.x, Flask
- **Database**: SQLAlchemy (SQLite for development)
- **Frontend**: HTML5, CSS3, Jinja2 Templates
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF, WTForms
- **Styling**: Custom CSS with gradient backgrounds and animations

## 📁 Project Structure

```
FLASK_BACKEND/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── models.py             # Database models
├── forms.py              # WTForms definitions
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
├── routes/              # Application routes
│   ├── __init__.py
│   ├── auth.py          # Authentication routes
│   └── tasks.py         # Task management routes
├── templates/           # Jinja2 templates
│   ├── base.html        # Base template
│   ├── homepage.html    # Landing page
│   ├── login.html       # Login form
│   ├── signup.html      # Registration form
│   ├── dashboard.html   # Task dashboard
│   ├── task_form.html   # Task creation/editing
│   └── view_task.html   # Task details
└── static/             # Static assets
    └── styles.css      # Application styles
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### 1. Clone or Download the Project
```bash
# If using Git
git clone <repository-url>
cd FLASK_BACKEND

# Or download and extract the ZIP file
```

### 2. Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables (Optional)
Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///taskflow.db
```

### 5. Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 📖 Usage Guide

### Getting Started
1. **Visit the Homepage** - Navigate to `http://localhost:5000`
2. **Create Account** - Click "Get Started" or "Signup" to create a new account
3. **Login** - Use your credentials to access your dashboard
4. **Create Tasks** - Start adding your tasks with descriptions and priorities

### Task Management
- **Add Task**: Click the "Add New Task" button on your dashboard
- **Edit Task**: Click "Edit" on any task to modify its details
- **Complete Task**: Mark tasks as done to track your progress
- **Delete Task**: Remove tasks you no longer need
- **View Details**: Click "View" to see full task information

### Navigation
- **Home**: Return to the homepage
- **Dashboard**: View all your tasks (authenticated users only)
- **Logout**: Securely end your session

## 🔧 Configuration

### Database Configuration
The application uses SQLite by default. To use a different database:

1. Update `config.py`:
```python
SQLALCHEMY_DATABASE_URI = 'your-database-uri'
```

2. Install appropriate database driver:
```bash
# For PostgreSQL
pip install psycopg2-binary

# For MySQL
pip install PyMySQL
```

### Security Settings
- Change the `SECRET_KEY` in `config.py` for production
- Enable CSRF protection by uncommenting the line in `app.py`
- Consider using environment variables for sensitive configuration

## 🎨 Customization

### Styling
- Modify `static/styles.css` to customize the appearance
- The CSS includes:
  - Responsive grid layouts
  - Gradient backgrounds
  - Hover animations
  - Mobile-friendly design

### Templates
- Edit templates in the `templates/` directory
- Base template (`base.html`) contains the common layout
- All templates extend the base template using Jinja2

## 🚀 Deployment

### Development
```bash
python app.py
```

### Production Considerations
1. **Disable Debug Mode**: Set `debug=False` in production
2. **Use Production WSGI Server**: Deploy with Gunicorn, uWSGI, or similar
3. **Environment Variables**: Use environment variables for configuration
4. **Database**: Use a production database (PostgreSQL, MySQL)
5. **Static Files**: Serve static files through a web server (Nginx, Apache)

### Example Production Deployment
```bash
# Install production dependencies
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🆘 Support

If you encounter any issues or have questions:

1. Check the existing issues in the repository
2. Create a new issue with detailed information
3. Contact the maintainer

## 🙏 Acknowledgments

- Flask community for the excellent framework
- Bootstrap inspiration for responsive design
- Icons and emojis from various open source projects

---

**Happy Task Managing! 🎉**

*Built with ❤️ using Flask*
