import pandas as pd
import numpy as np

# Load datasets
orig = pd.read_csv("FloodPrediction (1).csv")
punjab = pd.read_csv("punjab_flood_data.csv")

# ---------- CLEAN ORIGINAL ----------
orig['Flood?'] = orig['Flood?'].fillna(0).astype(int)

# ---------- FIX PUNJAB ----------
if 'Flood_Risk' in punjab.columns:
    mapping = {"Low":0, "Medium":1, "High":2}
    punjab['Flood?'] = punjab['Flood_Risk'].map(mapping)
    punjab.drop(columns=['Flood_Risk'], inplace=True)

# ---------- ADD MISSING COLUMNS ----------
for col in ['Sl','Station_Number','X_COR','Y_COR']:
    if col not in punjab.columns:
        if col == 'Sl':
            punjab[col] = range(len(punjab))
        else:
            punjab[col] = np.random.randint(10000,99999,len(punjab))

# ---------- MATCH COLUMNS ----------
all_cols = list(set(orig.columns).union(set(punjab.columns)))

for col in all_cols:
    if col not in orig.columns:
        orig[col] = 0
    if col not in punjab.columns:
        punjab[col] = 0

# Reorder columns same
orig = orig[all_cols]
punjab = punjab[all_cols]

# ---------- COMBINE ----------
final_df = pd.concat([orig, punjab], ignore_index=True)

# ---------- SAVE ----------
final_df.to_csv("final_combined_dataset.csv", index=False)

print("✅ Final combined dataset created successfully!")