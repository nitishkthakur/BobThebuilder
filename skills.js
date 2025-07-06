document.getElementById('skills-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const jobDescription = document.getElementById('job-description').value;

    // In a real application, you would send this to your backend for processing.
    // For now, we'll just use a simple keyword-based extraction.
    const keywords = ['JavaScript', 'Python', 'React', 'Node.js', 'SQL', 'MongoDB', 'Communication', 'Teamwork', 'Problem-solving'];
    const foundSkills = keywords.filter(skill => new RegExp('\b' + skill + '\b', 'i').test(jobDescription));

    const skillsOutput = document.getElementById('skills-output');
    if (foundSkills.length > 0) {
        let skillsHtml = '<ul class="list-group">';
        foundSkills.forEach(skill => {
            skillsHtml += `<li class="list-group-item">${skill}</li>`;
        });
        skillsHtml += '</ul>';
        skillsOutput.innerHTML = skillsHtml;
    } else {
        skillsOutput.innerHTML = '<p class="text-muted">No specific skills found. Try a different job description.</p>';
    }
});
