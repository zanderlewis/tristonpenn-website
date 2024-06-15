// darkmode.js

function toggleDarkMode() {
    const body = document.body;
    body.classList.toggle('dark-mode');

    // Check if the body has the 'dark-mode' class
    if (body.classList.contains('dark-mode')) {
        // If it does, set a cookie 'darkMode=true'
        document.cookie = 'darkMode=true; expires=Fri, 31 Dec 9999 23:59:59 GMT; path=/';
    } else {
        // If it doesn't, set a cookie 'darkMode=false'
        document.cookie = 'darkMode=false; expires=Fri, 31 Dec 9999 23:59:59 GMT; path=/';
    }
}