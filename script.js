// Dynamic Education Section
function addEducation() {
    const section = document.getElementById('education-section');
    const div = document.createElement('div');
    div.className = 'education-entry';
    div.innerHTML = `
        <input type="text" placeholder="Degree" class="degree" required>
        <input type="text" placeholder="Institution" class="institution" required>
        <input type="text" placeholder="Year" class="year" required>
        <button type="button" onclick="this.parentElement.remove()">Remove</button>
    `;
    section.appendChild(div);
}

// Dynamic Experience Section
function addExperience() {
    const section = document.getElementById('experience-section');
    const div = document.createElement('div');
    div.className = 'experience-entry';
    div.innerHTML = `
        <input type="text" placeholder="Job Title" class="job-title" required>
        <input type="text" placeholder="Company" class="company" required>
        <input type="text" placeholder="Years" class="years" required>
        <button type="button" onclick="this.parentElement.remove()">Remove</button>
    `;
    section.appendChild(div);
}

document.getElementById('resume-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const address = document.getElementById('address').value;
    const skills = document.getElementById('skills').value;

    // Education
    const educations = Array.from(document.querySelectorAll('.education-entry')).map(entry => ({
        degree: entry.querySelector('.degree').value,
        institution: entry.querySelector('.institution').value,
        year: entry.querySelector('.year').value
    }));

    // Experience
    const experiences = Array.from(document.querySelectorAll('.experience-entry')).map(entry => ({
        jobTitle: entry.querySelector('.job-title').value,
        company: entry.querySelector('.company').value,
        years: entry.querySelector('.years').value
    }));

    // Output Resume
    let html = `<h2>${name}</h2>`;
    html += `<p><strong>Email:</strong> ${email} | <strong>Phone:</strong> ${phone}</p>`;
    if(address) html += `<p><strong>Address:</strong> ${address}</p>`;
    if(educations.length) {
        html += '<h3>Education</h3><ul>';
        educations.forEach(ed => {
            html += `<li><strong>${ed.degree}</strong>, ${ed.institution} (${ed.year})</li>`;
        });
        html += '</ul>';
    }
    if(experiences.length) {
        html += '<h3>Experience</h3><ul>';
        experiences.forEach(ex => {
            html += `<li><strong>${ex.jobTitle}</strong>, ${ex.company} (${ex.years})</li>`;
        });
        html += '</ul>';
    }
    if(skills) {
        html += `<h3>Skills</h3><p>${skills}</p>`;
    }
    const output = document.getElementById('resume-output');
    output.innerHTML = html;
    output.style.display = 'block';
});

// Add one education and experience section by default
window.onload = function() {
    addEducation();
    addExperience();
};
