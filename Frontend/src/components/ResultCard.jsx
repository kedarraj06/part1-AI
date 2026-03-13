import React from 'react';

const ResultCard = ({ price, isLoading, error }) => {
    return (
        <div className="result-card">
            {isLoading && (
                <div className="loading-state">
                    <p>Running AI prediction...</p>
                </div>
            )}

            {error && !isLoading && (
                <div className="error-message">
                    <p><strong>Error:</strong> {error}</p>
                </div>
            )}

            {!isLoading && !error && price !== null && (
                <div className="price-display">
                    <h3>Estimated House Price</h3>
                    <h2>
                        {new Intl.NumberFormat('en-IN', {
                            style: 'currency',
                            currency: 'INR',
                            maximumFractionDigits: 0
                        }).format(price)}
                    </h2>
                </div>
            )}

            {!isLoading && !error && price === null && (
                <div className="idle-state">
                    <p>Enter property details to generate an AI price prediction.</p>
                </div>
            )}
        </div>
    );
};

export default ResultCard;
