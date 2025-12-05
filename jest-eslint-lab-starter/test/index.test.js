// index.js - Utility functions implementation
/**
 * Capitalizes the first letter of each word in a string
 * @param {string} input - The string to capitalize
 * @returns {string} The capitalized string
 */
function capitalizeWords(input) {
    if (typeof input !== 'string') {
        return '';
    }
    
    if (!input.trim()) {
        return input;
    }
    
    return input
        .split(' ')
        .map(word => {
            if (word.length === 0) return word;
            return word.charAt(0).toUpperCase() + word.slice(1);
        })
        .join(' ');
}

/**
 * Filters active users from an array of user objects
 * @param {Array} users - Array of user objects
 * @returns {Array} Array of active users
 */
function filterActiveUsers(users) {
    if (!Array.isArray(users)) {
        return [];
    }
    
    return users.filter(user => {
        return user && typeof user === 'object' && user.isActive === true;
    });
}

/**
 * Logs an action performed by a user with a timestamp
 * @param {string} action - The action performed
 * @param {string} username - The username who performed the action
 * @returns {string} Formatted log string
 */
function logAction(action, username) {
    const actionStr = typeof action === 'string' ? action : '';
    const usernameStr = typeof username === 'string' ? username : '';
    
    const now = new Date();
    const timestamp = now.toISOString().split('.')[0];
    
    return `User ${usernameStr} performed ${actionStr} at ${timestamp}`;
}

// Export the functions
module.exports = {
    capitalizeWords,
    filterActiveUsers,
    logAction
};