# FASTAPI
This is basic social media backend API made using FastApi and using PostgreSQL as the database.
## Features:
### Authenticate:
- JWT Token Authentication.
### User:
- Create User.
- Login User.
### Post:
- Get all Posts.
- Get Post using id.
- Update Post.
- Delete Post.
### Vote:
- Vote on the Post (upvote)
## File Structure:
```bash
alembic/
│
├── versions/
├── README.md
├── script.py.mako        
└── env.py                  
app/
│
├── routers/               
│       │
│       ├── __init__.py
│       ├── auth.py
│       ├── post.py
│       ├── user.py
│       └── vote.py       
├── __init__.py
├── config.py
├── database.py
├── main.py
├── models.py  
├── oauth2.py
├── schemas.py           
└── utils.py
alembic.ini
README.md
requirements.txt            
```
## Getting started:
### Prerequisites:
Install python normally or through Anaconda.
### Packages used:
Use the requirements.txt file and run the command below:
```bash
pip install -r reqiurements.txt
```
### Installation:
Run using the following steps:
1. Clone the repository:
```bash
git clone https://github.com/usman619/fast_api
cd fast_api
```
2. Using uvicorn command:
```bash
uvicorn app.main:app
uvicorn app.main:app --reload
```

3. Using fastapi command to get both Api and Api docs link:

```bash
# Development
fastapi dev app/main.py
# Production
fastapi run app/main.py
```