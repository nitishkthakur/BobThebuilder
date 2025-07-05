# Resume Builder

An AI-powered resume builder that helps tailor resumes to match job descriptions with three main features:

## Features

1. **Resume Formatting**: Upload a resume and get an ATS-friendly formatted version with scoring
2. **Skills Extraction**: Analyze job descriptions to identify core and nice-to-have skills
3. **Interview Questions**: Generate potential interview questions based on job descriptions

## Setup

### Backend (FastAPI)

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Run the server:
```bash
poetry run python main.py
```

The API will be available at `http://127.0.0.1:8001`

### Frontend

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Open `index.html` in a web browser or serve it with a local server:
```bash
python -m http.server 3000
```

Then visit `http://localhost:3000`

## API Endpoints

- `POST /format-resume` - Upload resume file for ATS formatting
- `POST /extract-skills` - Extract skills from job description
- `POST /generate-interview-questions` - Generate interview questions from job description

## Usage

1. Start the backend server
2. Open the frontend in your browser
3. Choose one of the three modes:
   - **Format Resume**: Upload your resume file
   - **Extract Skills**: Paste a job description
   - **Interview Questions**: Paste a job description

The application currently returns template responses. In a production environment, these would be replaced with actual LLM API calls for processing.