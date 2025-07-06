document.getElementById('resume-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const education = document.getElementById('education').value;
    const experience = document.getElementById('experience').value;
    const projects = document.getElementById('projects').value;

    const resumeData = {
        name,
        email,
        phone,
        education,
        experience,
        projects
    };

    // In a real application, you would send this data to your FastAPI backend
    // For now, we'll just display a simple suggestion.
    const resumeOutput = document.getElementById('resume-output');
    resumeOutput.innerHTML = `
        <h3>${name}</h3>
        <p><strong>Email:</strong> ${email} | <strong>Phone:</strong> ${phone}</p>
        <hr>
        <h4>Education</h4>
        <p>${education}</p>
        <hr>
        <h4>Work Experience</h4>
        <p>${experience}</p>
        <hr>
        <h4>Projects</h4>
        <p>${projects}</p>
    `;
});
