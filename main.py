import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader
import base64


# Function to extract data from uploaded PDF and convert to DataFrame
def extract_data_from_pdf(uploaded_file):
    # Initialize empty lists to store extracted data
    scheme = []
    no_of_schemes = []
    no_of_folios = []
    funds_mobilized = []
    repurchase_redemption = []
    net_assets = []
    avg_net_assets = []
    no_of_portfolios = []
    segregated_assets = []

    # Read the PDF file
    pdf_reader = PdfReader(uploaded_file)

    # Iterate through each page and extract text
    for page in pdf_reader.pages:
        text = page.extract_text()
        lines = text.split('\n')

        # Iterate through each line and extract data
        for line in lines:
            # Extract data using string manipulation or regular expressions
            if 'Sr Scheme Name' in line:
                continue  # Skip the header row
            columns = line.split('\t')
            if len(columns) == 9:  # Assuming 9 columns based on provided column names
                scheme.append(columns[0])
                no_of_schemes.append(columns[1])
                no_of_folios.append(columns[2])
                funds_mobilized.append(columns[3])
                repurchase_redemption.append(columns[4])
                net_assets.append(columns[5])
                avg_net_assets.append(columns[6])
                no_of_portfolios.append(columns[7])
                segregated_assets.append(columns[8])

    # Create DataFrame from extracted data
    df = pd.DataFrame({
        'Scheme': scheme,
        'No. of Schemes as on March 31, 2022': no_of_schemes,
        'No. of Folios as on March 31, 2022': no_of_folios,
        'Funds Mobilized for the month of March 2022 (INR in crore)': funds_mobilized,
        'Repurchase/Redemption for the month of March 2022 (INR in crore)': repurchase_redemption,
        'Net Assets Under Management as on March 31, 2022 (INR in crore)': net_assets,
        'Average Net Assets Under Management for the month March 2022 (INR in crore)': avg_net_assets,
        'No. of segregated portfolios created as on March 31, 2022': no_of_portfolios,
        'Net Assets Under Management in segregated portfolio as on March 31, 2022 (INR in crore)': segregated_assets
    })

    return df


# Function to calculate derived fields
def calculate_fields(df, selected_fields):
    if 'Net Inflow or Outflow' in selected_fields:
        df['Net Inflow or Outflow'] = pd.to_numeric(
            df['Funds Mobilized for the month of March 2022 (INR in crore)']) - pd.to_numeric(
            df['Repurchase/Redemption for the month of March 2022 (INR in crore)'])
    if 'Net Asset under Management per Scheme' in selected_fields:
        df['Net Asset under Management per Scheme'] = pd.to_numeric(
            df['Net Assets Under Management as on March 31, 2022 (INR in crore)']) / pd.to_numeric(
            df['No. of Schemes as on March 31, 2022'])
    if 'Net Inflow or Outflow per Scheme' in selected_fields:
        df['Net Inflow or Outflow per Scheme'] = df['Net Inflow or Outflow'] / pd.to_numeric(
            df['No. of Schemes as on March 31, 2022'])
    return df


# Function to generate and download CSV file
def download_csv(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="mutual_fund_data.csv">Download CSV File</a>'
    return href


# Main function to run Streamlit app
def main():
    st.set_page_config(
        page_title="Mutual Fund Performance Insights Application",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    st.title("Mutual Fund Performance Insights Application")
    st.write(
        "Upload your mutual fund performance data in PDF format to analyze it."
    )

    # Upload PDF file
    uploaded_file = st.file_uploader("Upload PDF file", type="pdf")

    if uploaded_file is not None:
        st.success("File Uploaded Successfully!")

        # Extract data from PDF and convert to DataFrame
        df = extract_data_from_pdf(uploaded_file)

        # Display DataFrame
        st.write("### Mutual Fund Performance Data")
        st.dataframe(df)

        # Field Selection
        selected_fields = st.multiselect("Select Fields", df.columns)

        # Calculate derived fields
        df = calculate_fields(df, selected_fields)

        # Display DataFrame with selected fields
        st.write("### Selected Fields Data")
        st.dataframe(df[selected_fields])

        # Download CSV button
        if st.button("Download CSV"):
            st.markdown(download_csv(df), unsafe_allow_html=True)


# Main function call
if __name__ == "__main__":
    main()
