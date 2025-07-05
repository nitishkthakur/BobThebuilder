from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import json

app = FastAPI(title="Resume Builder API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class JobDescription(BaseModel):
    job_description: str

class ResumeResponse(BaseModel):
    formatted_resume: str
    ats_score: int
    improvements: List[str]

class SkillsResponse(BaseModel):
    core_skills: List[str]
    nice_to_have_skills: List[str]
    experience_level: str

class InterviewQuestionsResponse(BaseModel):
    behavioral_questions: List[str]
    technical_questions: List[str]
    company_specific_questions: List[str]

@app.get("/")
async def root():
    return {"message": "Resume Builder API"}

@app.post("/format-resume", response_model=ResumeResponse)
async def format_resume(file: UploadFile = File(...)):
    if not file.filename.endswith(('.pdf', '.doc', '.docx', '.txt')):
        raise HTTPException(status_code=400, detail="Invalid file format")
    
    # Template response instead of actual LLM processing
    return ResumeResponse(
        formatted_resume="""
JOHN DOE
Software Engineer
Email: john.doe@email.com | Phone: (555) 123-4567
LinkedIn: linkedin.com/in/johndoe | GitHub: github.com/johndoe

PROFESSIONAL SUMMARY
Results-driven Software Engineer with 5+ years of experience in full-stack development. 
Proven track record of delivering scalable web applications and improving system performance.

TECHNICAL SKILLS
• Languages: Python, JavaScript, TypeScript, Java
• Frameworks: React, Node.js, Django, FastAPI
• Databases: PostgreSQL, MongoDB, Redis
• Cloud: AWS, Docker, Kubernetes

PROFESSIONAL EXPERIENCE
Senior Software Engineer | Tech Company | 2021-Present
• Developed and maintained 15+ microservices handling 1M+ daily requests
• Improved application performance by 40% through code optimization
• Led a team of 3 developers in delivering critical features

Software Engineer | StartupCorp | 2019-2021
• Built responsive web applications using React and Node.js
• Implemented automated testing reducing bugs by 30%
• Collaborated with cross-functional teams to deliver projects on time

EDUCATION
Bachelor of Science in Computer Science | University Name | 2019
        """,
        ats_score=87,
        improvements=[
            "Add quantifiable metrics to achievements",
            "Include more relevant keywords for your target role",
            "Optimize section headers for ATS parsing",
            "Add a skills section with exact job description matches"
        ]
    )

@app.post("/extract-skills", response_model=SkillsResponse)
async def extract_skills(job_desc: JobDescription):
    # Template response instead of actual LLM processing
    return SkillsResponse(
        core_skills=[
            "Python", "JavaScript", "React", "Node.js", "SQL", 
            "Git", "Agile Development", "RESTful APIs", "Docker"
        ],
        nice_to_have_skills=[
            "AWS", "Kubernetes", "TypeScript", "GraphQL", 
            "MongoDB", "CI/CD", "Test-Driven Development"
        ],
        experience_level="Mid-level (3-5 years)"
    )

@app.post("/generate-interview-questions", response_model=InterviewQuestionsResponse)
async def generate_interview_questions(job_desc: JobDescription):
    # Template response instead of actual LLM processing
    return InterviewQuestionsResponse(
        behavioral_questions=[
            "Tell me about a time you had to learn a new technology quickly",
            "Describe a challenging project you worked on and how you overcame obstacles",
            "How do you handle tight deadlines and competing priorities?",
            "Tell me about a time you had to work with a difficult team member"
        ],
        technical_questions=[
            "Explain the difference between REST and GraphQL APIs",
            "How would you optimize a slow database query?",
            "What are the key principles of responsive web design?",
            "How do you handle error handling in a distributed system?",
            "Explain the concept of microservices and their benefits"
        ],
        company_specific_questions=[
            "Why do you want to work for our company?",
            "How do you stay updated with the latest technology trends?",
            "What interests you most about this role?",
            "How would you contribute to our team's success?"
        ]
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)