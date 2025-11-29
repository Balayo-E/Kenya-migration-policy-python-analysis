import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('../data/kenya_real_2021_2024.csv')
plt.plot(data['Year'], data['Policy_Funding_BnKES'], marker='o')
plt.title('Kenya Migration Policy Funding 2021–2024')
plt.xlabel('Year')
plt.ylabel('Policy Funding (Bn KES)')
plt.grid(True)
plt.show()
