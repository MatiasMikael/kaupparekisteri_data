import requests
import pandas as pd

# YTJ API base URL
base_url = "https://avoindata.prh.fi/opendata-ytj-api/v3"

# Mapping for Osakeyhtiö (OY)
company_form_map = {
    "16": "Osakeyhtiö (OY)"  # Only fetch OY
}

def format_address(address):
    """Formats the address into a readable string."""
    if not address:
        return "Ei osoitetietoja saatavilla"  # No address available
    post_office = ""
    if 'postOffices' in address and len(address['postOffices']) > 0:
        post_office = address['postOffices'][0].get('city', '')
    parts = [
        address.get('street', ''),
        address.get('buildingNumber', ''),
        address.get('postCode', ''),
        post_office
    ]
    return ', '.join(filter(None, parts))

# Data storage
data_to_save = []

# Pagination settings
page = 1
max_pages = 40  # Fetch up to 40 pages
max_rows = 1000  # Limit rows to 1000
current_rows = 0  # Track the number of rows collected
more_data = True

print("Fetching Osakeyhtiöt (OY) in Helsinki (registered from 2020)...")

while more_data and page <= max_pages and current_rows < max_rows:
    params = {
        'location': 'Helsinki',
        'page': page,
        'registrationDateStart': '2020-01-01'  # Companies registered from 2020
    }
    url = f"{base_url}/companies"
    headers = {'Accept': 'application/json'}

    # Make the API GET request
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        companies = data.get('companies', [])
        print(f"Page {page}: {len(companies)} companies found.")

        for company in companies:
            if current_rows >= max_rows:
                more_data = False
                break

            company_name = "N/A"
            if 'names' in company and len(company['names']) > 0:
                company_name = company['names'][0].get('name', 'N/A')

            business_id = company.get('businessId', {}).get('value', 'N/A')
            company_form_code = company.get('companyForms', [{}])[0].get('type', 'N/A')
            registration_date = company.get('registrationDate', 'N/A')  # Get registration date

            if company_form_code in company_form_map:
                company_form_description = company_form_map[company_form_code]
                address = format_address(company.get('addresses', [{}])[0])
                data_to_save.append([
                    company_name,
                    business_id,
                    "Helsinki",
                    company_form_description,
                    address,
                    registration_date  # Add registration date
                ])
                current_rows += 1  # Increment row count

        more_data = len(companies) > 0
        page += 1
    else:
        print(f"Error fetching data: {response.status_code} - {response.text}")
        break

# Save data to CSV
csv_file = 'helsinki_osakeyhtiot_limited_1000.csv'
df = pd.DataFrame(data_to_save, columns=[
    'CompanyName', 'BusinessId', 'City', 'CompanyForm', 'Address', 'RegistrationDate'
])
df.to_csv(csv_file, index=False, encoding='utf-8-sig')

print(f"Data saved to {csv_file} with {current_rows} rows.")