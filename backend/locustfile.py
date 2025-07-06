from locust import HttpUser, task, between
"""
This module defines a Locust performance test for a resume formatting API endpoint.
Classes:
    ResumeBuilderUser(HttpUser): Simulates a user interacting with the '/format-resume' endpoint by uploading a sample resume file.
ResumeBuilderUser:
    - wait_time: Simulates user wait time between requests (1 to 3 seconds).
    - on_start(): Ensures a sample resume file exists before tests begin, creating one if necessary.
    - test_format_resume(): Sends a POST request to '/format-resume' with the sample resume file. If the file is missing, uses in-memory content as a fallback.
"""
import os
import io

class ResumeBuilderUser(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        # Create sample resume content if file doesn't exist
        if not os.path.exists("sample_resume.txt"):
            sample_content = """John Doe
Software Engineer
Email: john.doe@example.com
Phone: (555) 123-4567

EXPERIENCE
Software Developer at Tech Corp (2020-2023)
- Developed web applications using Python and JavaScript
- Collaborated with cross-functional teams

EDUCATION
Bachelor of Science in Computer Science
University of Technology (2016-2020)

SKILLS
- Python, JavaScript, React
- Database management
- Problem solving"""
            with open("sample_resume.txt", "w") as f:
                f.write(sample_content)

    @task
    def test_format_resume(self):
        try:
            with open("sample_resume.txt", "rb") as f:
                files = {"file": ("sample_resume.txt", f, "text/plain")}
                self.client.post("/format-resume", files=files)
        except FileNotFoundError:
            # Fallback: use in-memory content
            sample_content = "John Doe\nSoftware Engineer\ntest@example.com"
            files = {"file": ("sample_resume.txt", io.BytesIO(sample_content.encode()), "text/plain")}
            self.client.post("/format-resume", files=files)
