# Django Project Setup Guide

This guide provides step-by-step instructions to set up and run the Django project locally.

## **Prerequisites**

Before you start, ensure you have the following installed:

- Python (>= 3.8)
- Pipenv
- Git

## **Installation Steps**

### **1. Clone the Repository**

Run the following command to clone the project from GitHub:

```bash
git clone https://github.com/DEBI-2025/Backend.git
```

### **2. Switch to the Correct Branch**

Navigate to the project directory and switch to the `auth` branch:

```bash
cd Backend

git checkout auth
```

### **3. Activate the Virtual Environment**

Use `pipenv` to activate the virtual environment:

```bash
pipenv shell
```

### **4. Install Dependencies**

Install all required dependencies:

```bash
pipenv install
```

### **5. Navigate to the Django Project Directory**

Move into the Django project directory:

```bash
cd innerview
```

### **6. Apply Database Migrations**

Run the following command to apply database migrations:

```bash
python manage.py migrate
```

### **7. Start the Development Server**

Run the Django development server:

```bash
python manage.py runserver
```

The server should now be running at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


### **Deactivating the Virtual Environment**

To exit the Pipenv shell:

```bash
exit
```

## **Troubleshooting**

If you encounter any issues:

- Ensure you are using the correct Python version (`python --version`)
- Ensure Pipenv is installed (`pip install pipenv`)
- If dependencies fail to install, try running `pipenv install --skip-lock`

---


