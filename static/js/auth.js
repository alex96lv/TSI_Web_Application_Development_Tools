// Authentication utilities
function isAuthenticated() {
    return localStorage.getItem('accessToken') !== null;
}

function getAccessToken() {
    return localStorage.getItem('accessToken');
}

function getUser() {
    const userStr = localStorage.getItem('user');
    return userStr ? JSON.parse(userStr) : null;
}

function logout() {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
    localStorage.removeItem('user');
    window.location.href = '/login/';
}

// Theme management
function applyTheme(theme) {
    console.log('applyTheme called with:', theme);
    if (theme === 'dark') {
        document.body.classList.add('dark-theme');
        console.log('Added dark-theme class to body');
    } else {
        document.body.classList.remove('dark-theme');
        console.log('Removed dark-theme class from body');
    }
    console.log('Body classes after applyTheme:', document.body.className);
}

// Apply theme immediately (for early loading)
function applyThemeEarly() {
    if (isAuthenticated()) {
        const user = getUser();
        if (user && user.theme) {
            // Add to html element to avoid FOUC (Flash of Unstyled Content)
            if (user.theme === 'dark') {
                document.documentElement.classList.add('dark-theme-pending');
            }
        }
    }
}

// Apply theme on DOM ready
function initTheme() {
    console.log('initTheme called');
    console.log('Current body classes BEFORE:', document.body.className);

    if (isAuthenticated()) {
        const user = getUser();
        console.log('User in initTheme:', user);
        console.log('User theme:', user?.theme);
        if (user && user.theme) {
            applyTheme(user.theme);
            document.documentElement.classList.remove('dark-theme-pending');

            // Verify application
            console.log('Current body classes AFTER:', document.body.className);
            console.log('Has dark-theme class?', document.body.classList.contains('dark-theme'));
        } else {
            console.log('No user or theme found, skipping theme application');
        }
    } else {
        console.log('User not authenticated, skipping theme');
    }
}

// Try to apply theme early
applyThemeEarly();

// Apply theme when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTheme);
} else {
    initTheme();
}

// Protect pages that require authentication
function requireAuth() {
    if (!isAuthenticated()) {
        window.location.href = '/login/';
        return false;
    }
    return true;
}

// Check if on auth page and redirect if already logged in
function checkAuthPage() {
    const currentPath = window.location.pathname;
    if ((currentPath === '/login/' || currentPath === '/register/') && isAuthenticated()) {
        window.location.href = '/dashboard/';
    }
}

// Run on page load
if (window.location.pathname !== '/' &&
    window.location.pathname !== '/login/' &&
    window.location.pathname !== '/register/') {
    requireAuth();
}

checkAuthPage();
