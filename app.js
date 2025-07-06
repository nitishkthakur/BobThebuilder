document.getElementById('add-section').addEventListener('click', function() {
    const customSections = document.getElementById('custom-sections');
    const sectionId = 'custom-section-' + customSections.children.length;
    const newSection = document.createElement('div');
    newSection.className = 'custom-section-item mt-4';
    newSection.innerHTML = `
        <input type="text" class="shadow-sm appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500" placeholder="Section Title" required>
        <textarea rows="3" class="shadow-sm appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 mt-2" placeholder="Section Content" required></textarea>
    `;
    customSections.appendChild(newSection);
});

document.getElementById('resume-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const education = document.getElementById('education').value;
    const experience = document.getElementById('experience').value;
    const projects = document.getElementById('projects').value;

    let customSectionsHTML = '';
    const customSections = document.querySelectorAll('.custom-section-item');
    customSections.forEach(section => {
        const title = section.querySelector('input[type="text"]').value;
        const content = section.querySelector('textarea').value;
        if (title && content) {
            customSectionsHTML += `
                <hr>
                <h4>${title}</h4>
                <p>${content}</p>
            `;
        }
    });

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
        ${customSectionsHTML}
    `;
});

document.getElementById('print-resume').addEventListener('click', function() {
    const resumeContent = document.getElementById('resume-output').innerHTML;
    const printWindow = window.open('', '', 'height=600,width=800');
    printWindow.document.write('<html><head><title>Print Resume</title>');
    printWindow.document.write('<link rel="stylesheet" href="style.css">');
    printWindow.document.write('</head><body>');
    printWindow.document.write(resumeContent);
    printWindow.document.write('</body></html>');
    printWindow.document.close();
    printWindow.print();
});

