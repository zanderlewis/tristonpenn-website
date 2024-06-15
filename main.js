// main.js

function calculateAge(birthDate) {
    let today = new Date();
    let birth = new Date(birthDate);
    let age = today.getFullYear() - birth.getFullYear();
    let m = today.getMonth() - birth.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < birth.getDate())) {
        age--;
    }
    return age;
}

window.onload = function () {
    // Try to find the 'darkMode' cookie
    const darkModeCookie = document.cookie.split('; ').find(row => row.startsWith('darkMode='));

    if (darkModeCookie) {
        // If the cookie exists, check if it's set to 'true'
        if (darkModeCookie.split('=')[1] === 'true') {
            // If it is, add the 'dark-mode' class to the body
            document.body.classList.add('dark-mode');
        }
    } else {
        // If the cookie doesn't exist, create it and set it to 'false'
        document.cookie = 'darkMode=false; expires=Fri, 31 Dec 9999 23:59:59 GMT; path=/';
    }

    let age = calculateAge('2008-06-06'); // replace with the specific birth date
    let text = document.querySelector('.header p').innerHTML;
    document.querySelector('.header p').innerHTML = text.replace('{{{}}}', age);
};