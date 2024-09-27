# FASTAPI
Run using the following two methods:
1. Using uvicorn command:
```bash
uvicorn main:app
uvicorn main:app --reload
```

2. Using fastapi command to get both Api and Api docs link:

```bash
# Development
fastapi dev main.py
#Production
fastapi run main.py
```