# InnerView APIs

This project is a Django-based backend application designed to handle user authentication, quizzes, and related functionalities. It includes features such as user activation, JWT authentication, quiz management (fields, levels, topics, and questions), and API documentation using Swagger.

## Prerequisites

Before you start, ensure you have the following installed:

- Python (>= 3.8)
- Pipenv
- Git

---

## Installation Steps

1. **Clone the Repository**  
   Run the following command to clone the project from GitHub:

   ```bash
   git clone https://github.com/DEBI-2025/Backend.git
   ```

2. **Switch to the Correct Branch**  
   Navigate to the project directory:

   ```bash
   cd Backend
   ```

3. **Activate the Virtual Environment**  
   Use Pipenv to activate the virtual environment:

   ```bash
   pipenv shell
   ```

4. **Install Dependencies**  
   Install all required dependencies:

   ```bash
   pipenv install
   ```

5. **Navigate to the Django Project Directory**  
   Move into the Django project directory:

   ```bash
   cd innerview
   ```

6. **Apply Database Migrations**  
   Run the following command to apply database migrations:

   ```bash
   python manage.py migrate
   ```

7. **Start the Development Server**  
   Run the Django development server:
   ```bash
   python manage.py runserver
   ```
   The server should now be running at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Running the Project

To run the project, ensure you have completed the installation steps above. Once the server is running, you can access the following:

- **API Documentation**: Visit [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) to explore the API endpoints.
- **Authentication**: Use the provided JWT authentication endpoints for user registration, login, and activation.
- **Quiz Management**: Access the quiz-related APIs to manage fields, levels, topics, and questions.

---

## Features

### Authentication

- User registration and activation.
- JWT-based authentication with customizable token lifetimes.
- Custom user model with a `level` field.

### Quiz Management

- **Models**: Fields, levels, topics, and questions.
- **Serializers**: For handling quiz-related data.
- **Views**: API views with authentication permissions.
- **URLs**: Endpoints for quiz management.

### Additional Features

- CORS middleware for cross-origin requests.
- Swagger documentation for API endpoints.
- Refactored settings and URL configurations.

---

## API Documentation

The project includes Swagger documentation for all API endpoints. To access the documentation:

1. Start the development server:

   ```bash
   python manage.py runserver
   ```

2. Visit the Swagger UI at:  
   [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

---

## Troubleshooting

If you encounter any issues:

- Ensure you are using the correct Python version (`python --version`).
- Ensure Pipenv is installed (`pip install pipenv`).
- If dependencies fail to install, try running:
  ```bash
  pipenv install --skip-lock
  ```
