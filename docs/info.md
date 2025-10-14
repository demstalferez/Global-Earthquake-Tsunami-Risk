Global Earthquake-Tsunami Risk Assessment Dataset

Overview

The Global Earthquake-Tsunami Risk Assessment Dataset is a comprehensive, machine learning-ready dataset containing seismic characteristics and tsunami potential indicators for 782 significant earthquakes recorded globally from 2001 to 2022. This dataset is specifically designed for tsunami risk prediction, earthquake analysis, and seismic hazard assessment applications.

Dataset Information

Total Records: 782 earthquakes
Time Period: January 1, 2001 to December 31, 2022 (22 years)
Geographic Coverage: Global (Latitude: -61.85° to 71.63°, Longitude: -179.97° to 179.66°)
File Format: CSV
File Size: ~41KB
Missing Values: None (100% complete dataset)
Target Variable: Tsunami potential indicator (binary classification)
Key Features

🌊 Tsunami Classification

Non-Tsunami Events: 478 records (61.1%)
Tsunami-Potential Events: 304 records (38.9%)
Balanced Dataset: Suitable for binary classification tasks
Seismic Magnitude Distribution

Range: 6.5 - 9.1 Richter scale
Mean Magnitude: 6.94
Major Earthquakes (≥8.0): 28 events including the 2004 (9.1) and 2011 (9.1) mega-earthquakes
Feature Description

Feature	Type	Description	Range/Values	Tsunami Relevance
magnitude	Float	Earthquake magnitude (Richter scale)	6.5 - 9.1	High - Primary tsunami predictor
cdi	Integer	Community Decimal Intensity (felt intensity)	0 - 9	Medium - Population impact measure
mmi	Integer	Modified Mercalli Intensity (instrumental)	1 - 9	Medium - Structural damage indicator
sig	Integer	Event significance score	650 - 2910	High - Overall hazard assessment
nst	Integer	Number of seismic monitoring stations	0 - 934	Low - Data quality indicator
dmin	Float	Distance to nearest seismic station (degrees)	0.0 - 17.7	Low - Location precision
gap	Float	Azimuthal gap between stations (degrees)	0.0 - 239.0	Low - Location reliability
depth	Float	Earthquake focal depth (km)	2.7 - 670.8	High - Shallow = higher tsunami risk
latitude	Float	Epicenter latitude (WGS84)	-61.85° to 71.63°	High - Ocean proximity indicator
longitude	Float	Epicenter longitude (WGS84)	-179.97° to 179.66°	High - Ocean proximity indicator
Year	Integer	Year of occurrence	2001 - 2022	Medium - Temporal patterns
Month	Integer	Month of occurrence	1 - 12	Low - Seasonal analysis
tsunami	Binary	Tsunami potential (TARGET)	0, 1	TARGET VARIABLE
Data Quality Assessment

Zero missing values across all 782 records and 13 features
100% data completeness ensures robust model training
38.9% positive cases (tsunami events) provides good balance for binary classification
Global representation of major seismic zones
22-year temporal span captures diverse seismic patterns
Major earthquake events included (28 earthquakes ≥8.0 magnitude)
Machine Learning Applications

Tsunami Risk Prediction: Binary classification using seismic parameters
Early Warning Systems: Real-time tsunami threat assessment
Hazard Mapping: Geographic risk zone identification
Magnitude Estimation: Earthquake strength prediction from network data
Citation

Original Source: Earthquake Dataset on Kaggle