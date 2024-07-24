

# What is this project?
<span><img src="https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=green" /></span>
<span><img src="https://img.shields.io/badge/Docker-2CA5E0?style=flat&logo=docker&logoColor=white" /></span>

This Project Provides a Fully Functional Weblog Application Using Django, Managed With Docker For Easy Setup And Deployment.

Features:
<p>-> User Authentication</p>
<p>-> CRUD Operations For Blog Posts</p>
<p>-> Commenting System</p>


# How to use?

First Clone The Project.

```bash
git clone https://github.com/amahadnezhad/Weblog.git
```

Then Make Sure Docker Is Running.
* If You Are On Windows Click On The Docker Desktop Icon And Wait For About a Minute.

Then In The Project Directory Run This Command:

```bash
docker-compose up --build
```

It Will Create Two Containers:
One For Django And One For PostgreSql As The Database For The Project.
All The Required Packages Will Be Installed.

### Install a new package.
* Attention:
If You Want To Install a Package For Django Project You Should Run This Command:

```bash
docker-compose exec web pip install <package-name>
``` 

Don't Forget To Add The New Package To requirements.txt For Further Use:
```bash
docker-compose exec web pip freeze > requirements.txt
```
