from fastapi import FastAPI, File, UploadFile, HTTPException, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
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

@app.post("/format-resume")
async def format_resume(file: UploadFile = File(...)):
    if not file.filename.endswith(('.pdf', '.doc', '.docx', '.txt')):
        return HTMLResponse(
            '<div class="bg-red-50 border border-red-200 rounded-xl p-4 text-red-800">Invalid file format. Please upload PDF, DOC, DOCX, or TXT files.</div>',
            status_code=400
        )
    
    # Template response instead of actual LLM processing
    formatted_resume = """
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
                                    """
    
    improvements = [
        "Add quantifiable metrics to achievements",
        "Include more relevant keywords for your target role",
        "Optimize section headers for ATS parsing",
        "Add a skills section with exact job description matches"
    ]
    
    improvements_html = "".join([f'<li class="flex items-start space-x-3"><svg class="w-5 h-5 text-primary-600 mt-0.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"/></svg><span class="text-primary-700">{improvement}</span></li>' for improvement in improvements])
    
    return HTMLResponse(f"""
    <div class="mt-8 space-y-6">
        <div class="bg-gradient-to-r from-green-50 to-emerald-50 border border-green-200 rounded-xl p-6">
            <div class="flex items-center space-x-3">
                <div class="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center">
                    <svg class="w-6 h-6 text-green-600" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                    </svg>
                </div>
                <div>
                    <h3 class="text-xl font-bold text-green-800">ATS Score: 87/100</h3>
                    <p class="text-green-700">Your resume is well-optimized for ATS systems</p>
                </div>
            </div>
        </div>
        
        <div class="bg-gray-50 border border-gray-200 rounded-xl p-6">
            <h3 class="text-lg font-bold text-gray-900 mb-4">Formatted Resume:</h3>
            <div class="bg-white rounded-lg p-6 border max-h-96 overflow-y-auto">
                <pre class="text-sm text-gray-700 whitespace-pre-wrap font-mono">{formatted_resume}</pre>
            </div>
        </div>
        
        <div class="bg-gradient-to-r from-blue-50 to-primary-50 border border-blue-200 rounded-xl p-6">
            <h3 class="text-lg font-bold text-primary-800 mb-4">Recommended Improvements:</h3>
            <ul class="space-y-2">
                {improvements_html}
            </ul>
        </div>
    </div>
    """)

@app.post("/extract-skills")
async def extract_skills(job_description: str = Form(...)):
    if not job_description.strip():
        return HTMLResponse(
            '<div class="bg-red-50 border border-red-200 rounded-xl p-4 text-red-800">Please provide a job description.</div>',
            status_code=400
        )
    
    core_skills = ["Python", "JavaScript", "React", "Node.js", "SQL", "Git", "Agile Development", "RESTful APIs", "Docker"]
    nice_to_have = ["AWS", "Kubernetes", "TypeScript", "GraphQL", "MongoDB", "CI/CD", "Test-Driven Development"]
    
    core_skills_html = "".join([f'<span class="px-3 py-2 bg-red-100 text-red-800 rounded-lg text-sm font-medium">{skill}</span>' for skill in core_skills])
    nice_to_have_html = "".join([f'<span class="px-3 py-2 bg-blue-100 text-primary-800 rounded-lg text-sm font-medium">{skill}</span>' for skill in nice_to_have])
    
    return HTMLResponse(f"""
    <div class="mt-8 space-y-6">
        <div class="bg-gradient-to-r from-purple-50 to-indigo-50 border border-purple-200 rounded-xl p-6">
            <div class="flex items-center space-x-3">
                <div class="w-12 h-12 bg-purple-100 rounded-full flex items-center justify-center">
                    <svg class="w-6 h-6 text-purple-600" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                    </svg>
                </div>
                <div>
                    <h3 class="text-xl font-bold text-purple-800">Analysis Complete</h3>
                    <p class="text-purple-700">Experience Level: Mid-level (3-5 years)</p>
                </div>
            </div>
        </div>
        
        <div class="bg-gradient-to-r from-red-50 to-rose-50 border border-red-200 rounded-xl p-6">
            <h3 class="text-lg font-bold text-red-800 mb-4">Core Skills (Must Have):</h3>
            <div class="flex flex-wrap gap-3">
                {core_skills_html}
            </div>
        </div>
        
        <div class="bg-gradient-to-r from-blue-50 to-primary-50 border border-blue-200 rounded-xl p-6">
            <h3 class="text-lg font-bold text-primary-800 mb-4">Nice to Have Skills:</h3>
            <div class="flex flex-wrap gap-3">
                {nice_to_have_html}
            </div>
        </div>
    </div>
    """)

@app.post("/generate-interview-questions")
async def generate_interview_questions(job_description: str = Form(...)):
    if not job_description.strip():
        return HTMLResponse(
            '<div class="bg-red-50 border border-red-200 rounded-xl p-4 text-red-800">Please provide a job description.</div>',
            status_code=400
        )
    
    behavioral_questions = [
        "Tell me about a time you had to learn a new technology quickly",
        "Describe a challenging project you worked on and how you overcame obstacles",
        "How do you handle tight deadlines and competing priorities?",
        "Tell me about a time you had to work with a difficult team member"
    ]
    
    technical_questions = [
        "Explain the difference between REST and GraphQL APIs",
        "How would you optimize a slow database query?",
        "What are the key principles of responsive web design?",
        "How do you handle error handling in a distributed system?",
        "Explain the concept of microservices and their benefits"
    ]
    
    company_questions = [
        "Why do you want to work for our company?",
        "How do you stay updated with the latest technology trends?",
        "What interests you most about this role?",
        "How would you contribute to our team's success?"
    ]
    
    behavioral_html = "".join([f'<div class="bg-white rounded-lg p-4 border-l-4 border-purple-400"><p class="text-gray-700">{q}</p></div>' for q in behavioral_questions])
    technical_html = "".join([f'<div class="bg-white rounded-lg p-4 border-l-4 border-orange-400"><p class="text-gray-700">{q}</p></div>' for q in technical_questions])
    company_html = "".join([f'<div class="bg-white rounded-lg p-4 border-l-4 border-emerald-400"><p class="text-gray-700">{q}</p></div>' for q in company_questions])
    
    return HTMLResponse(f"""
    <div class="mt-8 space-y-6">
        <div class="bg-gradient-to-r from-purple-50 to-indigo-50 border border-purple-200 rounded-xl p-6">
            <h3 class="text-lg font-bold text-purple-800 mb-4 flex items-center space-x-2">
                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd"/>
                </svg>
                <span>Behavioral Questions</span>
            </h3>
            <div class="space-y-3">
                {behavioral_html}
            </div>
        </div>
        
        <div class="bg-gradient-to-r from-orange-50 to-amber-50 border border-orange-200 rounded-xl p-6">
            <h3 class="text-lg font-bold text-orange-800 mb-4 flex items-center space-x-2">
                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M12.316 3.051a1 1 0 01.633 1.265l-4 12a1 1 0 11-1.898-.632l4-12a1 1 0 011.265-.633zM5.707 6.293a1 1 0 010 1.414L3.414 10l2.293 2.293a1 1 0 11-1.414 1.414l-3-3a1 1 0 010-1.414l3-3a1 1 0 011.414 0zm8.586 0a1 1 0 011.414 0l3 3a1 1 0 010 1.414l-3 3a1 1 0 11-1.414-1.414L16.586 10l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd"/>
                </svg>
                <span>Technical Questions</span>
            </h3>
            <div class="space-y-3">
                {technical_html}
            </div>
        </div>
        
        <div class="bg-gradient-to-r from-emerald-50 to-green-50 border border-emerald-200 rounded-xl p-6">
            <h3 class="text-lg font-bold text-emerald-800 mb-4 flex items-center space-x-2">
                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M4 2a2 2 0 00-2 2v11a3 3 0 106 0V4a2 2 0 00-2-2H4zM3 15a1 1 0 011-1h1a1 1 0 011 1v1a1 1 0 01-1 1H4a1 1 0 01-1-1v-1zm7-1a1 1 0 000 2h3a1 1 0 100-2h-3z" clip-rule="evenodd"/>
                </svg>
                <span>Company-Specific Questions</span>
            </h3>
            <div class="space-y-3">
                {company_html}
            </div>
        </div>
    </div>
    """)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)