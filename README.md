
# iCloud-Lite

Welcome to **iCloud-Lite**, which is a cloud drive application built using the Django framework and integrated with various AWS services such as S3, EC2, Elastic IP, and Load Balancer. The application allows users to upload, view, download, and delete files, with secure user authentication and scalable cloud storage.

## Table of Contents
- Features
- Technology Stack
- Installation
- Configuration
- Usage
- Deployment
- AWS Integration
## Features

- **User Authentication:**
    * Secure user registration, login, and logout.
    - Password encryption and session management using Django’s built-in authentication.

- **File Management:**
     - Users can upload files to the cloud drive.
     - Ability to view, download, and delete files stored on Amazon S3.
    - Supports multiple file types (e.g., PDF, JPG, TXT).

- **Cloud Storage (AWS S3):**
    - All user files are securely stored on Amazon S3 with access policies and CORS configuration.
    - Efficient and scalable cloud storage solution for user files.

- **Web Hosting (AWS EC2):**
    - The application is hosted on AWS EC2 with an Elastic IP and load balancing for high availability.

## Technology Stack
- **Frontend:** HTML, CSS
- **Backend:** Django (Python Framework)
- **Database:** MySQL (or SQLite for local development)
- **Cloud Storage:** Amazon S3
- **Web Hosting:** Amazon EC2
- **Load Balancer:** AWS Elastic Application Load Balancer (ELB)
- **Other AWS Services:** Elastic IP, IAM for secure access management
## Installation

**Prerequisites**
- Python 3.x
- pip
- MySQL or SQLite (for database)
- AWS account for S3, EC2, and other services

**Clone the Repository**
```
git clone https://github.com/hrdikshrma/iCloud-Lite.git
```

**Set Up Virtual Environment**
```
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

**Install Dependencies**
```
pip install -r requirements.txt
```
## Configuration

**Database Setup (MySQL)**
- In your MySQL instance, create a new database:
```
CREATE DATABASE cloud_drive_db;
```
- Update the `DATABASES` settings in `settings.py`:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cloud_drive_db',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',  # Or your MySQL host
        'PORT': '3306',
    }
}
```
- Run migrations:
```
python manage.py migrate
```

**AWS S3 Configuration**
- Set up an **S3 bucket** for file storage.
- Add your **AWS credentials** and **S3 bucket** name to `settings.py`:
```
AWS_ACCESS_KEY_ID = 'your-access-key'
AWS_SECRET_ACCESS_KEY = 'your-secret-access-key'
AWS_STORAGE_BUCKET_NAME = 'your-s3-bucket-name'
AWS_S3_REGION_NAME = 'your-region'  # e.g., us-east-1
```
- Ensure that CORS and bucket policies are set up in your S3 console to allow file uploads from your app.

**Other Settings** 

Update any other necessary settings in `settings.py`, such as `ALLOWED_HOSTS`, static file storage, and security settings.
## Usage

**Running the Development Server**
```
python manage.py runserver
```
Navigate to `http://127.0.0.1:8000` to access the application locally. 

**NOTE: Please make additional changes if you are running this on the EC2 instance.**

## Deployment

**Deploying on AWS EC2**
- Launch an EC2 instance from the AWS Console.
- SSH into the EC2 instance and install dependencies.
- Set up your project on EC2 and configure it with your Elastic - IP and Load Balancer.
- Deploy your Django application using *Gunicorn* or *Nginx* for production.
## AWS Integration


- **Amazon S3:** Used to store user-uploaded files. Configured with proper bucket policies and CORS settings to allow secure uploads and downloads.
- **Amazon EC2:** The application is hosted on an EC2 instance. Deployed using *Elastic IP* to ensure a stable, fixed IP address.

- **Application Load Balancer:** AWS Elastic Load Balancer (ELB) is used to ensure high availability by distributing traffic across multiple EC2 instances.
## Contributing

Contributions are welcome! If you have a bug fix, improvement, or a new feature to add, please follow these steps:
- Fork the repository
- Create a new branch
- Make your changes and commit them
- Push to the branch
- Open a Pull Request
## Contacts

If you have any questions or suggestions, feel free to reach out to me:
- Email: hardik.sharma@temple.edu
- GitHub: hrdikshrma
Thank you for visiting iCloud-Lite! Happy coding!