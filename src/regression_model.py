import pandas as pd
import statsmodels.api as sm
data = pd.read_csv('../data/kenya_real_2021_2024.csv')
X = sm.add_constant(data['Policy_Funding_BnKES'])
y = data['Refugee_Population']
model = sm.OLS(y, X).fit(cov_type='HC3')
print(model.summary())
