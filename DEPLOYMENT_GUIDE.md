# 🚀 Deploy The Chamber to the Web

## Option 1: Streamlit Cloud (Easiest - Recommended)

### Step 1: Prepare Your Project
1. **Install Streamlit locally first to test:**
   ```bash
   pip install -r requirements_web.txt
   streamlit run the_chamber_web.py
   ```

2. **Test locally** - Make sure everything works in your browser at `http://localhost:8501`

### Step 2: Deploy to Streamlit Cloud
1. **Push your code to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/the_chamber2.git
   git push -u origin main
   ```

2. **Go to [share.streamlit.io](https://share.streamlit.io)**
3. **Sign in with GitHub**
4. **Click "New app"**
5. **Select your repository and branch**
6. **Set the main file path:** `the_chamber_web.py`
7. **Click "Deploy"**

**Your game will be live at:** `https://your-app-name.streamlit.app`

---

## Option 2: Heroku (Free tier discontinued, but still works)

### Step 1: Install Heroku CLI
```bash
# Ubuntu/Debian
curl https://cli-assets.heroku.com/install.sh | sh

# Or download from: https://devcenter.heroku.com/articles/heroku-cli
```

### Step 2: Create Heroku App
```bash
heroku login
heroku create your-chamber-app
```

### Step 3: Create Procfile
Create a file called `Procfile` (no extension):
```
web: streamlit run the_chamber_web.py --server.port=$PORT --server.address=0.0.0.0
```

### Step 4: Deploy
```bash
git add .
git commit -m "Add Heroku deployment files"
git push heroku main
```

---

## Option 3: Python Anywhere (Free hosting)

### Step 1: Sign up at [pythonanywhere.com](https://pythonanywhere.com)

### Step 2: Upload your files
1. Go to Files tab
2. Upload your Python files
3. Install requirements in Bash console:
   ```bash
   pip install --user streamlit pandas
   ```

### Step 3: Run the app
```bash
streamlit run the_chamber_web.py --server.port=8080 --server.address=0.0.0.0
```

---

## Option 4: Google Cloud Run (Free tier available)

### Step 1: Install Google Cloud CLI
```bash
# Download from: https://cloud.google.com/sdk/docs/install
```

### Step 2: Create Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements_web.txt .
RUN pip install -r requirements_web.txt

COPY . .
EXPOSE 8080

CMD ["streamlit", "run", "the_chamber_web.py", "--server.port=8080", "--server.address=0.0.0.0"]
```

### Step 3: Deploy
```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
gcloud run deploy --source .
```

---

## ⚠️ Important Notes

1. **Google Sheets Integration:** Make sure your `google_sheets_manager.py` is properly configured with credentials
2. **Environment Variables:** For production, use environment variables for sensitive data
3. **Data Storage:** Consider using a database instead of CSV files for production
4. **HTTPS:** All platforms above provide HTTPS by default

## 🎯 Quick Start (Streamlit Cloud)

1. **Test locally:** `streamlit run the_chamber_web.py`
2. **Push to GitHub**
3. **Deploy on Streamlit Cloud**
4. **Share the link:** `https://your-app-name.streamlit.app`

Your game will be accessible to anyone with the link, no installation required! 