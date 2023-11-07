# Django_Ecommerce_Project
E-commerce project built using Django

## Features
The notable features of my E-commerce project are:
-  SEO-friendly URLs formated as `year/month/day/slug`
-  Canonical URLs for blog posts
-  Pagination that displays three posts per page
-  Post recommendations by email
-  Comment system (which the admin is able to moderate)
-  Tagging system to categorize posts by tags
-  Post recommendations based on similar tags
-  Sitemap for search engines
-  RSS feed that users can subscribe to
-  Full-text search engine.

## Demo 
https://github.com/DeLaCruzCristian/Django_Ecommerce_Project/assets/141530518/8ed0e744-a487-4960-b567-1090e401e0d0

## Installation
First clone the repository and change into the directory
```bash
$ git clone https://github.com/DeLaCruzCristian/Django_Ecommerce_Project.git
```
```bash
$ cd Django_personal_blog_site
```
Create a virtual environment
```bash
$ python -m venv .venv
```
Activate the environment
```bash
$ .venv\Scripts\Activate.ps1
```
Install requirements
```bash
$ pip install -r requirements.txt
$ pre-commit install
```

> [!IMPORTANT]
> You will need to run rabbitMQ, Celery, and Redis for the site to work properly. If you want to use Docker like I did, run these commands:
```bash
$ docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
$ celery -A django_project worker --pool solo -l info
$ docker run -it --rm --name redis -p 6379:6379 redis
```
> [!IMPORTANT]
> I used Stripe as my payment gateway. You will need to set up an account with Stripe, get a key and change these settings located in the
> main project settings.py file:
```
STRIPE_PUBLISHABLE_KEY = ""
STRIPE_SECRET_KEY = ""
STRIPE_API_VERSION = ""
STRIPE_WEBHOOK_SECRET = ""
```
> [!IMPORTANT]
> For the webhooks to work, you will need to use the Stripe cli and set it up. This is the command I used once I have already downloaded
> the Stripe cli and have logged in (note that the webhook endpoint is at /payment/webhook/ ):
```bash
$ stripe listen --forward-to localhost:8000/payment/webhook/
```

Now you can migrate:
```bash
$ python manage.py migrate
```
Create superuser for Admin Login
```bash
$ python manage.py createsuperuser
```
Once superuser has been created, you can run the server and head to the admin page to add products, coupons, and categories.
```bash
$ python manage.py runserver
```
To exit the environment
```bash
$ deactivate
```
