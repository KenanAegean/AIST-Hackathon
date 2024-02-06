// dark-theme-toggle.js

document.addEventListener('DOMContentLoaded', () => {
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    const themeStyle = document.getElementById('theme-style');

    darkModeToggle.addEventListener('click', () => {
        // Toggle the dark mode class on the body
        document.body.classList.toggle('dark-mode');

        // Toggle the CSS file between light and dark
        const currentTheme = themeStyle.getAttribute('href');
        const newTheme = currentTheme.includes('light') ? 'dark.css' : 'light.css';
        themeStyle.setAttribute('href', `/static/css/${newTheme}`);

        // Save the user's preference in a cookie
        document.cookie = `darkMode=${document.body.classList.contains('dark-mode')}; path=/`;
    });

    // Check for dark mode preference in cookie on page load
    const darkModeCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('darkMode='));
    if (darkModeCookie) {
        const isDarkMode = darkModeCookie.split('=')[1] === 'true';
        document.body.classList.toggle('dark-mode', isDarkMode);
        const defaultTheme = isDarkMode ? 'dark.css' : 'light.css';
        themeStyle.setAttribute('href', `/static/css/${defaultTheme}`);
    }
});
