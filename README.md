# Nick-II

Nick-II is a web application designed to assist Chinese users in generating English nicknames. 
It leverages user-provided information such as Chinese name, gender, and birth year to help users come up with suitable English names. 
The application uses the ChatGPT API to recommend five English names that are phonetically similar to the user's Chinese name, 
appropriate for the user's gender, and aligned with the user's birth decade. 
Additionally, Nick-II employs web scraping to retrieve data from the United States Social Security Administration, 
allowing users to search for the top 200 most popular male and female baby names in the United States since 1880.

## Screenshot
<img src='https://user-images.githubusercontent.com/87135678/273277508-00fbf2bc-1170-4821-8ca7-f364476fdeaf.png' align='left' width='45%'>
<img src='https://user-images.githubusercontent.com/87135678/273277755-d46fbfd8-34c0-47e4-a9db-6754bbf39db6.png' width='45%'>

## Getting Started
To get started, follow the following steps:
- Input the necessary settings in the .env file (you can refer to .env.example for guidance)

Then run the following commands to run your app:
```bash
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py collectSSA
  python manage.py runserver
```

## Tech Used
- Bootstrap
- Django
- jQuery
- OpenAI
- SQLite
- BeautifulSoup
- HTML, CSS, JavaScript
