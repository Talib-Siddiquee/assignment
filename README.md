# Hospital Management API

This is a Django-based API for managing hospital records, including patients, doctors, and patient records.

## Setup Instructions

1. **Create and activate a virtual environment:**

   ```
   venv\Scripts\activate`
   ```

2. **Install the required packages:**

   ```
   pip install django
   pip install djangorestframework
   pip install djangorestframework-simplejwt
   ```

3. **Set up the database:**

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```


4. **Run the server:**

   ```
   python manage.py runserver
   ```

5. **Create a superuser**

   ```
   python manage.py createsuperuser
   username=talib_siddiquee
   password=Talib123@
   ```



- Doctors and patients are associated with departments.
- Patients can only fetch their own records.
- Doctors can fetch and modify their own patients' records but not others.
- Superusers can access any endpoint.
