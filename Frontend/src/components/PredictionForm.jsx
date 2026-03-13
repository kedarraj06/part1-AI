import React, { useState } from 'react';

const PredictionForm = ({ onSubmit, disabled }) => {
    const [formData, setFormData] = useState({
        city: 'Pune',
        locality_tier: 'Mid',
        bhk: 3,
        bathrooms: 2,
        super_area_sqft: 1200,
        property_age_years: 5,
        parking: 1,
        furnishing: 'Semi-Furnished',
        gated_society: 1,
        floor_no: 4,
        total_floors: 10
    });

    const handleChange = (e) => {
        const { name, value, type } = e.target;
        let parsedValue = value;
        // Ensure numeric fields are cast to Number
        const numericFields = ['bhk', 'bathrooms', 'super_area_sqft', 'property_age_years', 'parking', 'gated_society', 'floor_no', 'total_floors'];
        if (numericFields.includes(name)) {
            parsedValue = value !== '' ? Number(value) : '';
        }
        setFormData((prev) => ({ ...prev, [name]: parsedValue }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit(formData);
    };

    return (
        <form className="prediction-form" onSubmit={handleSubmit}>
            <div className="form-sections-container">
                {/* Location Section */}
                <div className="form-section-group">
                    <h4>Location</h4>
                    <div className="form-group-grid">
                        <div className="form-group">
                            <label>City</label>
                            <select name="city" value={formData.city} onChange={handleChange} disabled={disabled}>
                                <option value="Pune">Pune</option>
                                <option value="Mumbai">Mumbai</option>
                                <option value="Hyderabad">Hyderabad</option>
                                <option value="Nagpur">Nagpur</option>
                            </select>
                        </div>
                        <div className="form-group">
                            <label>Locality Tier</label>
                            <select name="locality_tier" value={formData.locality_tier} onChange={handleChange} disabled={disabled}>
                                <option value="Mid">Mid</option>
                                <option value="Premium">Premium</option>
                            </select>
                        </div>
                    </div>
                </div>

                {/* Property Section */}
                <div className="form-section-group">
                    <h4>Property Details</h4>
                    <div className="form-group-grid">
                        <div className="form-group">
                            <label>BHK</label>
                            <input type="number" name="bhk" value={formData.bhk} onChange={handleChange} disabled={disabled} required min="1"/>
                        </div>
                        <div className="form-group">
                            <label>Bathrooms</label>
                            <input type="number" name="bathrooms" value={formData.bathrooms} onChange={handleChange} disabled={disabled} required min="1"/>
                        </div>
                        <div className="form-group">
                            <label>Super Area (sqft)</label>
                            <input type="number" name="super_area_sqft" value={formData.super_area_sqft} onChange={handleChange} disabled={disabled} required min="100"/>
                        </div>
                        <div className="form-group">
                            <label>Age (Years)</label>
                            <input type="number" name="property_age_years" value={formData.property_age_years} onChange={handleChange} disabled={disabled} required min="0"/>
                        </div>
                    </div>
                </div>

                {/* Building Section */}
                <div className="form-section-group">
                    <h4>Building</h4>
                    <div className="form-group-grid">
                        <div className="form-group">
                            <label>Floor No</label>
                            <input type="number" name="floor_no" value={formData.floor_no} onChange={handleChange} disabled={disabled} required min="0"/>
                        </div>
                        <div className="form-group">
                            <label>Total Floors</label>
                            <input type="number" name="total_floors" value={formData.total_floors} onChange={handleChange} disabled={disabled} required min="1"/>
                        </div>
                        <div className="form-group">
                            <label>Parking</label>
                            <input type="number" name="parking" value={formData.parking} onChange={handleChange} disabled={disabled} required min="0"/>
                        </div>
                    </div>
                </div>

                {/* Amenities Section */}
                <div className="form-section-group">
                    <h4>Amenities</h4>
                    <div className="form-group-grid">
                        <div className="form-group">
                            <label>Furnishing</label>
                            <select name="furnishing" value={formData.furnishing} onChange={handleChange} disabled={disabled}>
                                <option value="Semi-Furnished">Semi-Furnished</option>
                                <option value="Unfurnished">Unfurnished</option>
                                <option value="Fully Furnished">Fully Furnished</option>
                            </select>
                        </div>
                        <div className="form-group">
                            <label>Gated Society</label>
                            <select name="gated_society" value={formData.gated_society} onChange={handleChange} disabled={disabled}>
                                <option value={1}>Yes</option>
                                <option value={0}>No</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>

            <button type="submit" className="submit-btn" disabled={disabled}>
                {disabled ? 'Processing...' : 'Predict Price'}
            </button>
        </form>
    );
};

export default PredictionForm;
