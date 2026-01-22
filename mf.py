import requests
import pandas as pd
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from tqdm import tqdm

# -----------------------------
# STEP 1: Create HTTP session with retries
# -----------------------------
session = requests.Session()
retries = Retry(
    total=5,
    backoff_factor=0.5,
    status_forcelist=[429, 500, 502, 503, 504]
)
session.mount("https://", HTTPAdapter(max_retries=retries))

# -----------------------------
# STEP 2: Fetch MF catalog (THIS WAS MISSING)
# -----------------------------
catalog_url = "https://api.mfapi.in/mf"
catalog_response = session.get(catalog_url, timeout=20)
catalog_response.raise_for_status()

funds_list = catalog_response.json()
funds_df = pd.DataFrame(funds_list)

# Safety check
if 'schemeCode' not in funds_df.columns:
    raise ValueError("schemeCode column not found in catalog response")

codes = funds_df['schemeCode'].dropna().unique().tolist()

print(f"Total schemes found: {len(codes)}")

# -----------------------------
# STEP 3: Fetch NAV history
# -----------------------------
all_nav_data = []

for code in tqdm(codes, desc="Fetching NAV data"):
    try:
        r = session.get(f"https://api.mfapi.in/mf/{code}", timeout=10)
        r.raise_for_status()
        fund_data = r.json()

        if 'meta' not in fund_data or 'data' not in fund_data:
            continue

        meta = fund_data['meta']
        history = fund_data['data']

        for day in history:
            day['scheme_code'] = str(code)
            day['scheme_name'] = meta.get('scheme_name', 'Unknown')
            day['category'] = meta.get('scheme_category', 'Unknown')
            day['scheme_type'] = meta.get('scheme_type', 'Unknown')
            all_nav_data.append(day)

    except Exception as e:
        print(f"Skipped {code}: {e}")
        continue

# -----------------------------
# STEP 4: Create DataFrame
# -----------------------------
nav_df = pd.DataFrame(all_nav_data)

print("Data fetch completed")
print(nav_df.head())
print(f"Total rows collected: {len(nav_df)}")

# OPTIONAL: save intermediate data
nav_df.to_csv("raw_nav_data.csv", index=False)
