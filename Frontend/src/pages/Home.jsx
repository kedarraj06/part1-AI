import React, { useState } from 'react';
import PredictionForm from '../components/PredictionForm';
import ResultCard from '../components/ResultCard';
import { predictHousePrice } from '../services/api';

function Home() {
    const [price, setPrice] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handlePredictionSubmit = async (formData) => {
        setLoading(true);
        setError(null);
        try {
            const predictedPrice = await predictHousePrice(formData);
            setPrice(predictedPrice);
        } catch (err) {
            setError(err.message || "An error occurred");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="home-container">
            <h2>House Price Estimator</h2>

            {error && <div className="error-message">{error}</div>}

            <div className="content-grid">
                <div className="form-section">
                    <PredictionForm onSubmit={handlePredictionSubmit} disabled={loading} />
                </div>

                <div className="result-section">
                    <ResultCard price={price} isLoading={loading} error={error} />
                </div>
            </div>
        </div>
    );
}

export default Home;
