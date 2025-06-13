# Flask Login Demo

This is a basic Flask app using PostgreSQL with login functionality.

## Features
- User login
- PostgreSQL database connection
- Linked to OrganisationMaster table

## Deployment

### 1. Deploy to Render

1. Fork this repository to your GitHub.
2. Go to https://render.com, create an account and click "New Web Service".
3. Select your repo.
4. Use the following settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
5. Add environment variables:
   - `DATABASE_URL` → Your PostgreSQL connection string
   - `SECRET_KEY` → Any secret string

### 2. Local Setup

```bash
pip install -r requirements.txt
python app.py
```