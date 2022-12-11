L=139.
unique_orbits = pd.DataFrame(data[data['TDC_CHANNEL'] == 139]).drop_duplicates(subset=['ORBIT_CNT'], inplace=False)
print("\nThe number of unique orbits with at least one measurement from TDC_CHANNEL == 139 is:", len(unique_orbits))