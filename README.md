# CS50W Project 1 - Wiki
Project 2/6 for CS50w
> Status: completed & submitted (Pass)
  
### Description:
* Source code for an imitation of [Wikipedia](https://www.wikipedia.org/)
* Languages used are HTML, CSS and Python. Django is used as web framework.
* Uses [markdown syntax](https://www.markdownguide.org/basic-syntax/) for creating an entry.
  
### Contents:
* Visiting  [ /wiki/TITLE ] where TITLE is the name of an entry will redirect you to the contents of that entry. 
    * If the entry doesn't exist, you'll be redirected to an error info page.
* An Index page (home page) where all of the entries are listed (ordered alphabetically).
* Searchbar which can:
    * Redirect you to an entry that you have typed (case insensitive),
    * Redirect you to a page showing similar results to what you typed,
    * Redirect you to an error info page telling you that the entry you searched for doesn't exist.
* Ability to create an entry (using markdown).
    * If an entry with the same title exists, your process of creating a new entry will be cancelled.
    * Otherwise, you will be redirected to the entry that you have created.
* Ability to edit an entry.
* Random entry button which can redirect you to a random entry.
* Markdown to HTML conversion for displaying the contents of an entry.
  
### About CS50W
CS50W is a continuation of [CS50](https://cs50.harvard.edu/), diving more deeply into the design and implementaion of web apps with Python, JavaScript, and SQL using frameworks like Django, React, and Bootstrap. Topics include database design, scalability, security, and user experience.  
> Want to learn CS50W for **free**? You can check out their OpenCourseWare [here](https://cs50.harvard.edu/web/).
  
### Note on academic honesty
If you're taking CS50W, either through [Harvard Extension School](https://courses.extension.harvard.edu/course-catalog/courses/subject/CSCI/33A), [Harvard Summer School](https://courses.summer.harvard.edu/course-catalog/courses/subject/CSCI/33A) or [OpenCourseWare](https://cs50.harvard.edu/web/), please do not blindly copy paste my code. You are putting yourself at a huge risk for getting excluded from the course by the staff themselves as they grade each project thoroughly.
