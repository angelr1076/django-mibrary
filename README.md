# django-mibrary

### CS50 - final project

[View Mibrary](https://web-production-60f9.up.railway.app/)

Django Mibrary is my final assignment/project to complete CS50.

Mibrary allows users to register, login, create a user profile, view/edit user settings and update their password. The app also allows users to create and edit books as well as viewing other user profiles, books and leaving reviews of their own or other user's books. Mibrary uses function based views as well as class based views and uses the built in message system in conjunction with Bootstrap's message alerts. The app uses some custom forms, as well as class mixins and decorators for page security.

The app also uses static content for a minimal amount of images along with all user uploaded images being saved and loaded from Cloudinary SDK for storage. Mibrary gives users the ability to create book summaries with rich text using ckeditor.

The app also uses static content for a minimal amount of images along with all user uploaded images being saved and loaded from Cloudinary for offsite storage.

### To clone the repository and run the project:

- Open your terminal.
- Navigate to the directory where you want to clone the repository.
- Run the following command: `git clone https://github.com/angelr1076/django-mibrary.git`
- Navigate to the cloned directory: `cd django-mibrary`
- Install the required dependencies: `pip install -r requirements.txt`
- Run the server: `python manage.py runserver`

[YouTube Submission](https://www.youtube.com/watch?v=pUkKkPVrXMQ)

#### Login

![Login page](https://res.cloudinary.com/angelrodriguez/image/upload/v1603973486/Mibrary%20Images/loginpage.png)

#### Register

![Registration page](https://res.cloudinary.com/angelrodriguez/image/upload/v1603973486/Mibrary%20Images/register.png)

#### Home Page

![Home page](https://res.cloudinary.com/angelrodriguez/image/upload/v1603973486/Mibrary%20Images/homepage.png)

#### Book Lists by Status

![Book Lists page](https://res.cloudinary.com/angelrodriguez/image/upload/v1603973486/Mibrary%20Images/nobooks.png)

#### No Books Added

![No books](https://res.cloudinary.com/angelrodriguez/image/upload/v1603973490/Mibrary%20Images/wanttoread.png)

#### Add/Edit Books

![Create book](https://res.cloudinary.com/angelrodriguez/image/upload/v1603973491/Mibrary%20Images/createbook.png)

#### Profile Page

![Profile page](https://res.cloudinary.com/angelrodriguez/image/upload/v1603973490/Mibrary%20Images/profile.png)

#### Add Reviews

![Reviews](https://res.cloudinary.com/angelrodriguez/image/upload/v1603990043/Mibrary%20Images/reviews.png)
