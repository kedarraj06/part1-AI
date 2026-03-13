export const predictHousePrice = async (formData) => {
    // Use environment variable if available, fallback to localhost
    const API_URL = import.meta.env?.VITE_API_URL
        ? `${import.meta.env.VITE_API_URL}/predict`
        : 'http://localhost:5000/predict';

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        });

        if (!response.ok) {
            let errorMessage = 'Network response was not ok';
            try {
                const errorData = await response.json();
                errorMessage = errorData.detail || errorData.message || errorMessage;
            } catch (e) {
                // Fallback if response isn't JSON
            }
            throw new Error(errorMessage);
        }

        const data = await response.json();
        return data.predicted_price;
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
};
