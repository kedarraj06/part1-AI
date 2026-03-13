import React from 'react';
import Home from './pages/Home';

function App() {
    return (
        <div className="app-container">
            <header>
                <h1>AI House Price <span>Predictor</span></h1>
            </header>
            <main>
                <Home />
            </main>
        </div>
    );
}

export default App;
