// API utilities
const API_BASE = '/api';

async function apiRequest(endpoint, options = {}) {
    const token = localStorage.getItem('accessToken');

    const defaultHeaders = {
        'Content-Type': 'application/json',
    };

    if (token) {
        defaultHeaders['Authorization'] = `Bearer ${token}`;
    }

    const config = {
        ...options,
        headers: {
            ...defaultHeaders,
            ...options.headers,
        },
    };

    try {
        const response = await fetch(`${API_BASE}${endpoint}`, config);

        if (response.status === 401) {
            // Token expired, logout
            logout();
            return null;
        }

        return response;
    } catch (error) {
        console.error('API Request Error:', error);
        throw error;
    }
}

// API Methods
const API = {
    // Transactions
    async getTransactions(filters = {}) {
        const params = new URLSearchParams(filters);
        const response = await apiRequest(`/transactions/?${params}`);
        return response ? await response.json() : [];
    },

    async createTransaction(data) {
        const response = await apiRequest('/transactions/', {
            method: 'POST',
            body: JSON.stringify(data),
        });
        if (response && !response.ok) {
            const error = await response.json();
            console.error('Transaction creation failed:', error);
            throw new Error(error.error || error.message || 'Failed to create transaction');
        }
        return response ? await response.json() : null;
    },

    async updateTransaction(id, data) {
        const response = await apiRequest(`/transactions/${id}/`, {
            method: 'PUT',
            body: JSON.stringify(data),
        });
        return response ? await response.json() : null;
    },

    async deleteTransaction(id) {
        const response = await apiRequest(`/transactions/${id}/`, {
            method: 'DELETE',
        });
        return response?.ok;
    },

    async getTransactionStats() {
        const response = await apiRequest('/transactions/stats/summary/');
        return response ? await response.json() : null;
    },

    // Categories
    async getCategories(type = null) {
        const params = type ? `?type=${type}` : '';
        const response = await apiRequest(`/categories/${params}`);
        return response ? await response.json() : [];
    },

    async createCategory(data) {
        const response = await apiRequest('/categories/', {
            method: 'POST',
            body: JSON.stringify(data),
        });
        return response ? await response.json() : null;
    },

    // Budgets
    async getBudgets() {
        const response = await apiRequest('/budgets/');
        return response ? await response.json() : [];
    },

    async createBudget(data) {
        const response = await apiRequest('/budgets/', {
            method: 'POST',
            body: JSON.stringify(data),
        });
        return response ? await response.json() : null;
    },

    async updateBudget(id, data) {
        const response = await apiRequest(`/budgets/${id}/`, {
            method: 'PUT',
            body: JSON.stringify(data),
        });
        return response ? await response.json() : null;
    },

    async deleteBudget(id) {
        const response = await apiRequest(`/budgets/${id}/`, {
            method: 'DELETE',
        });
        return response?.ok;
    },

    // Goals
    async getGoals(status = null) {
        const params = status ? `?status=${status}` : '';
        const response = await apiRequest(`/goals/${params}`);
        return response ? await response.json() : [];
    },

    async createGoal(data) {
        const response = await apiRequest('/goals/', {
            method: 'POST',
            body: JSON.stringify(data),
        });
        return response ? await response.json() : null;
    },

    async updateGoal(id, data) {
        const response = await apiRequest(`/goals/${id}/`, {
            method: 'PUT',
            body: JSON.stringify(data),
        });
        return response ? await response.json() : null;
    },

    async deleteGoal(id) {
        const response = await apiRequest(`/goals/${id}/`, {
            method: 'DELETE',
        });
        return response?.ok;
    },
};

// Format currency
function formatCurrency(amount, currency = 'USD') {
    const symbols = {
        'USD': '$',
        'EUR': '€'
    };
    return `${amount.toLocaleString('en-US')} ${symbols[currency] || ''}`;
}

// Format date
function formatDate(dateStr) {
    const date = new Date(dateStr);
    return date.toLocaleDateString('ru-RU');
}
