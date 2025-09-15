# src/analyze.py
import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("outputs", exist_ok=True)

df = pd.read_csv("data/prison_escapes.csv", parse_dates=["Date"])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month_name()
df['Weekday'] = df['Date'].dt.day_name()
df['Success_bool'] = df['Success'].astype(str).str.strip().str.lower() == 'yes'

by_year = df.groupby('Year').size().reset_index(name='Count').sort_values('Year')
by_country = df.groupby('Country').size().reset_index(name='Count').sort_values('Count', ascending=False)
success_rate_country = df.groupby('Country')['Success_bool'].mean().reset_index(name='SuccessRate').sort_values('SuccessRate', ascending=False)

by_year.to_csv("outputs/summary_by_year.csv", index=False)
by_country.to_csv("outputs/summary_by_country.csv", index=False)
success_rate_country.to_csv("outputs/success_rate_by_country.csv", index=False)

# Plot 1: Escapes per year
plt.figure(figsize=(8,4))
plt.plot(by_year['Year'], by_year['Count'], marker='o')
plt.title('Escapes per Year (sample)')
plt.xlabel('Year')
plt.ylabel('Number of Recorded Incidents')
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/escapes_per_year.png")
plt.close()

# Plot 2: Escapes per Country (bar)
plt.figure(figsize=(8,4))
plt.bar(by_country['Country'], by_country['Count'])
plt.title('Escapes per Country (sample)')
plt.xlabel('Country')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("outputs/escapes_per_country.png")
plt.close()

print("Analysis done. Output files written to outputs/")
