🔹 Project Architecture

This project follows Django’s MVT (Model–View–Template) architecture.

Model:
The Post model defines the structure of blog posts, including:

Title

Content

Author

Created Date

Updated Date

View:
Views handle the business logic:

post_list view displays all blog posts with pagination.

post_detail view displays a single blog post.

Template:
Templates render the frontend UI:

base.html for common layout

post_list.html for listing posts

post_detail.html for single post view

Admin Panel:
Django Admin is used to manage blog posts efficiently without building a custom admin interface.

🔹 Deployment Architecture

Hosted on Render

Production server: Gunicorn

Static files handled using WhiteNoise

Database: SQLite

Version control: GitHub

🔹 Design Decisions

Used SQLite for simplicity and beginner-level setup.

Used Django Admin instead of building custom CRUD UI to focus on backend fundamentals.

Implemented pagination (5 posts per page) for scalability.

Used a clean template structure for maintainability.
