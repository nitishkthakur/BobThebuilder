import io
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Resume Builder API"}

def test_format_resume_invalid_extension():
    data = {"file": ("resume.exe", io.BytesIO(b"dummy"), "application/octet-stream")}
    resp = client.post("/format-resume", files=data)
    assert resp.status_code == 400
    assert "Invalid file format" in resp.text

def test_format_resume_txt_success():
    data = {"file": ("resume.txt", io.BytesIO(b"Hello"), "text/plain")}
    resp = client.post("/format-resume", files=data)
    assert resp.status_code == 200
    # check for ATS Score section and formatted resume
    assert "ATS Score: 87/100" in resp.text
    assert "JOHN DOE" in resp.text

@pytest.mark.parametrize("payload, endpoint, error_msg", [
    ({}, "/extract-skills", "Please provide a job description"),
    ({}, "/generate-interview-questions", "Please provide a job description"),
])
def test_missing_job_description(payload, endpoint, error_msg):
    """
    Tests the API endpoint for handling missing job description in the payload.

    Args:
        payload (dict): The data to be sent in the POST request, expected to be missing the job description.
        endpoint (str): The API endpoint URL to which the request is sent.
        error_msg (str): The expected error message to be present in the response.

    Asserts:
        - The response status code is 400 (Bad Request).
        - The expected error message is present in the response text.
    """
    resp = client.post(endpoint, data=payload)
    assert resp.status_code == 400
    assert error_msg in resp.text

def test_extract_skills_success():
    resp = client.post("/extract-skills", data={"job_description": "some JD"})
    assert resp.status_code == 200
    # check core and nice-to-have sections
    assert "Core Skills" in resp.text
    assert "Nice to Have Skills" in resp.text
    assert "Python" in resp.text
    assert "AWS" in resp.text

def test_generate_interview_questions_success():
    resp = client.post("/generate-interview-questions", data={"job_description": "some JD"})
    assert resp.status_code == 200
    # check for each section title
    assert "Behavioral Questions" in resp.text
    assert "Technical Questions" in resp.text
    assert "Company-Specific Questions" in resp.text
    # sample question check
    assert "Tell me about a time you had to learn a new technology" in resp.text
