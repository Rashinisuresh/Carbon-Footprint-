PROJECT TITLE:
Carbon Footprint Tracker using OCR on Utility Bills

DOMAIN:
Optical Character Recognition (OCR) / NLP / Climate Action

DESCRIPTION:
This project extracts electricity usage details from utility bill images
using Tesseract OCR. The extracted text is processed using Python and
Regular Expressions to identify electricity consumption (kWh). The usage
data is converted into carbon emissions using standard emission factors.

TECHNOLOGIES USED:
- Python
- Tesseract OCR
- PIL (Image Processing)
- Regular Expressions (NLP)

WORKFLOW:
1. User provides an electricity bill image
2. OCR extracts text from the image
3. Electricity usage is detected using Regex
4. Carbon footprint is calculated
5. Result is displayed

FORMULA USED:
Carbon Footprint (kg CO2) = Electricity Usage (kWh) × 0.82

SAMPLE OUTPUT:
Electricity Usage: 245 kWh
Carbon Footprint: 200.9 kg CO2

FUTURE ENHANCEMENTS:
- Mobile App Integration
- Database Storage
- Monthly Tracking
- Visualization Dashboard
