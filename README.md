# Django Simple Blog

A simple **Blog Web Application** built using **Django**.

Users can view blog posts, read individual posts, and explore content in a clean interface. This project was created to practice **Django fundamentals, models, views, templates, pagination, and project architecture**.

---

## 🚀 Live Demo

Live Application  
https://your-blog-app-link.onrender.com

GitHub Repository  
https://github.com/yourusername/django-simple-blog

---

## ✨ Features

- View list of blog posts
- View individual blog post details
- Blog post model with title, content, and author
- Pagination for blog posts
- Clean template structure
- Reusable base template
- Admin panel for managing posts
- Django MVT architecture implementation

---

## 🛠 Tech Stack

- **Python**
- **Django**
- **HTML**
- **CSS**
- **Bootstrap**
- **SQLite**
- **Git & GitHub**
- **Render (Deployment)**

---

## 📂 Project Structure


django-simple-blog
│
├── simple_blog
│ ├── simple_blog
│ │ ├── settings.py
│ │ ├── urls.py
│ │ └── wsgi.py
│ │
│ ├── blog
│ │ ├── models.py
│ │ ├── views.py
│ │ ├── urls.py
│ │ └── admin.py
│ │
│ ├── templates
│ │ ├── base.html
│ │ ├── post_list.html
│ │ └── post_detail.html
│ │
│ └── manage.py
│
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### Clone the repository


git clone https://github.com/yourusername/django-simple-blog.git


### Navigate to the project folder

```
cd django-simple-blog/simple_blog
```

### Create a virtual environment

```
python -m venv venv
```

### Activate virtual environment

Windows:

```
venv\Scripts\activate
```

### Install dependencies

```
pip install -r requirements.txt
```

### Apply migrations

```
python manage.py migrate
```

### Create superuser

```
python manage.py createsuperuser
```

### Run the development server

```
python manage.py runserver
```

Open in browser:


http://127.0.0.1:8000


---

## 🧠 Challenges Faced

- Understanding Django’s MVT architecture
- Creating models and database migrations
- Connecting views with templates
- Implementing pagination for blog posts
- Managing templates and reusable layouts

---

## 📚 What I Learned

- Django project structure
- Django Models and ORM
- Django Views and URL routing
- Django Templates and template inheritance
- Pagination in Django
- Managing data through Django Admin

---

## 🔮 Future Improvements

- Add user authentication
- Allow users to create blog posts
- Add comment system
- Add search functionality
- Add categories and tags
- Improve UI design

---

## 👨‍💻 Author

Selva Kalusalingam R

GitHub  
https://github.com/selvakalusu003
