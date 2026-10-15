# BookNest – Online Bookstore

BookNest is a web-based online bookstore developed using Django, MySQL, and Django REST Framework. Users can browse books, search by title or author, manage their shopping cart, place orders, and view their order history.

## Features

- **Book Catalog:** Browse books and view individual book details.
- **Search and Categories:** Search by book title, author, or publisher and filter by category.
- **User Authentication:** Register and log in using email-based authentication.
- **Shopping Cart:** Add books, update quantities, and remove items.
- **Checkout and Orders:** Manage delivery addresses, place orders, and view order history and order status.
- **REST API:** Access book data through Django REST Framework.
- **JWT Authentication:** Authenticate API requests using access and refresh tokens.
- **Role-Based Permissions:** Restrict API write operations to authorized staff and administrators.
- **Admin Panel:** Manage books, categories, inventory, and orders.

## Technologies Used

- **Backend:** Python, Django
- **API:** Django REST Framework, Simple JWT
- **Database:** MySQL
- **Frontend:** HTML, CSS, JavaScript, Bootstrap 5
- **Tools:** VS Code, Git, GitHub, Postman

## REST API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/books/` | Retrieve the book list |
| GET | `/api/books/<id>/` | Retrieve book details |
| GET | `/api/books/?search=python` | Search books |
| GET | `/api/books/?category=1` | Filter by category |
| POST | `/api/token/` | Obtain JWT tokens |
| POST | `/api/token/refresh/` | Refresh an access token |

Book API access requires authentication. Write operations are restricted to staff and administrators.

## Installation and Setup

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd BookNest-Django-Online-Bookstore
```

Replace the placeholder with your repository's HTTPS URL.

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

On Windows:

```powershell
.\venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root, alongside `manage.py`:

```env
SECRET_KEY="your-django-secret-key"
DB_NAME=booknest_db
DB_USER=your-mysql-username
DB_PASSWORD="your-mysql-password"
DB_HOST=localhost
DB_PORT=3306
```

Create the `booknest_db` database in MySQL before proceeding. Use your own credentials and keep `.env` private.

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Create an administrator account

```bash
python manage.py createsuperuser
```

Follow the prompts to create the account.

### 7. Start the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Project Purpose

BookNest was developed as a portfolio project to demonstrate practical skills in Django web development, relational database integration, REST API development, authentication, permissions, and e-commerce order workflows.

## Future Improvements

- Online payment gateway integration
- Automated testing
- Deployment to a production hosting platform