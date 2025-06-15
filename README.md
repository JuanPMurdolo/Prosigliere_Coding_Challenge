# Prosigliere_Coding_Challenge

Coding Challenge
You are tasked with designing and implementing a RESTful API for managing a simple blogging
platform. The core functionality of this platform includes managing blog posts and their
associated comments.
Requirements:

Data Models:
● Create two data models: BlogPost and Comment. A BlogPost has a title and
content, and each BlogPost can have multiple Comment objects associated with
it.

API Endpoints:
● Implement the following API endpoints:
● GET /api/posts: This endpoint should return a list of all blog posts,
including their titles and the number of comments associated with each
post.
● POST /api/posts: Create a new blog post.
● GET /api/posts/{id}: Retrieve a specific blog post by its ID, including its
title, content, and a list of associated comments.
● POST /api/posts/{id}/comments: Add a new comment to a specific blog
post.


Challenge Submission
Please send an email to the hiring manager including a Github link to the code you created at your earliest convenience. Bear in mind that the code should be production ready but it's ok to not complete it in full. Please don't dedicate more than 4 hours to work on this project.
Please add a README with instructions to run it, and what would be your next steps if you had more time available.

# Prosigliere Coding Challenge

This project is a RESTful API built with Django and Django REST Framework for managing blog posts and comments.
This project is really similar to a project I have in my GH, https://github.com/JuanPMurdolo/Coding_Challenge_PF, this project is similar in everything except that I used Flask in the other one.
I used the django-admin startproject tool.

---

## Tech Stack

- Python 3.x  
- Django 4.x  
- Django REST Framework

---

## Getting Started

### 1. Clone the repository

git clone https://github.com/your_username/prosigliere_blog_api.git
cd prosigliere_blog_api

### 2. Create and activate a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


### 3. Install dependencies

pip install -r requirements.txt

### 4. Apply migrations and run the server

python manage.py migrate

python manage.py runserver

# API Endpoints
GET - /api/posts - List all blog posts with the number of comments

POST - /api/posts - Create a new blog post (title, content)

GET - /api/posts/<id> - Get a post's title, content, and its comments

POST - /api/posts/<id>/comments	- Add a comment (content) to a specific blog post

# Postman
Shared in the repo there is a postman .JSON file "Prosigliere_Backend.postman_collection.json", that has a localhost endpoints requests already prepared.



