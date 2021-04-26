

<h1 align="center">
  <br>
  <a href="#"><img src="Project\media\Images\Hocus Focus logo.png" alt="Markdownify" width="200"></a>
  <br>
Hocus-Focus
  <br>
</h1>

<p align="center">
  <a href="#"><img alt="GitHub issues" src="https://img.shields.io/badge/URL-website-blueviolet?logo=Python=for-the-badge" title="Live Demo"></a>
  </p>


## Project Description
The user needs to sign up a valid email id , followed by creating cards where the user can upload files(images, pdf, doc) and retrieve. Anyone who have an account can access the notes and make use of it.

This app is developed especially for students, where teachers can upload the notes and the students can access them .

### Key Features   
* Multiple Rooms - Make changes, See changes
  - Create multiple rooms for different courses/subjects
* Upload media
  - Upload required files to the particular rooms

## Technologies used 
1. Backend Framework: **Django** 
2. Front-end Framework: **Bootstrap**
3. Database used: **Sqlite**



## Installation

1. Fork and Clone
    <ol>
    <li>Fork Urja-SCL-maxo Repo</li>
    <li>Clone the repo to your local system.</li>
    </ol>

2. Create a Virtual Environment for the Project

    In Windows
    ```bash
    pip install virtualenv
    ```
    ```bash
    virtualenv -p python venv
    ```
    ```bash
    venv\Scripts\activate
    ```

    In Ubuntu/MacOS
    ```bash
    python -m virtualenv venv

    source venv/bin/activate
    ```

   If you are giving a different name other than `venv`, then please mention it in `.gitigonre` first

3. Install all the requirements

    ```bash
    pip install -r requirements.txt
    ```
## Development

4. Checkout to different branch
     ```git
    git status
    git pull
    git branch
    git checkout -b < your-branch-here >
    ```

5. Make migrations/ Create db.sqlite3

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Run server
    ```bash
    python manage.py runserver
    ```

7. Do the changes and send a PR referencing the changes.

## Contributing/ Adding Features

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change in the project.
