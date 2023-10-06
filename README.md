# Nick-II

Nick-II is a web application designed to assist Chinese users in generating English nicknames. 
It leverages user-provided information such as Chinese name, gender, and birth year to help users come up with suitable English names. 
The application uses the ChatGPT API to recommend five English names that are phonetically similar to the user's Chinese name, 
appropriate for the user's gender, and aligned with the user's birth decade. 
Additionally, Nick-II employs web scraping to retrieve data from the United States Social Security Administration, 
allowing users to search for the top 200 most popular male and female baby names in the United States since 1880.

## Screenshot


<img src='https://github.com/Bojun-Wu/Nick-II/assets/87135678/70be02fe-2c9f-44bb-9c86-867a06dbcb03.jpg' align='left' width='45%'>
<img src='https://github.com/Bojun-Wu/Nick-II/assets/87135678/516a0aaf-91c3-47c4-8e36-e65bd9239161.jpg' width='45%'>

## Getting Started
To get started, follow the following steps:
- Input the necessary settings in the .env file (you can refer to .env.example for guidance)

Then run the following commands to run your app:
```bash
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py collectSSA
```

## Tech Used
- Bootstrap
- Django
- jQuery
- OpenAI
- SQLite
- BeautifulSoup
- HTML, CSS, JavaScript
