Mutual Fund Performance Insights Application
This is a Streamlit web application designed to analyze mutual fund performance data uploaded in PDF format. Users can upload their PDF files containing mutual fund performance data, select specific fields for analysis, and download the analyzed data in CSV format.

Features
PDF Upload: Users can upload PDF files containing mutual fund performance data.
Data Extraction: The application extracts data from the uploaded PDF and converts it into a DataFrame.
Field Selection: Users can select specific fields from the extracted data for analysis.
Derived Field Calculation: The application calculates derived fields based on the selected fields.
CSV Download: Users can download the analyzed data in CSV format for further analysis.
Usage
Upload PDF File: Click on the "Upload PDF file" button and select the PDF file containing mutual fund performance data.
Select Fields: After uploading the file, select the fields you want to analyze from the dropdown menu.
View Data: The application will display the selected fields from the uploaded data in a tabular format.
Download CSV: Click on the "Download CSV" button to download the analyzed data in CSV format.


Installation
Clone the repository:
bash
Copy code
git clone (https://github.com/Akashbabum/Mutual-Fund-Performance-Insights-Application.git)
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Run the application:
bash
Copy code
streamlit run app.py

*Requirements
Python 3.x
Streamlit
pandas
PyPDF2


Contribution
Contributions are welcome! If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.

You can customize this template according to your project's specific details and requirements.
