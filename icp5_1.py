import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

plt.style.use(style='ggplot')

train = pd.read_csv(Path('C:/Users/Hari/Downloads/Python_Lesson5/train.csv'))
plt.scatter(train.GarageArea, train.SalePrice, alpha=.5, color='r')
plt.show()

filter_data = train[(train.GarageArea > 160) & (train.GarageArea < 950) & (train.SalePrice < 500000)]
plt.scatter(filter_data.GarageArea, filter_data.SalePrice, alpha=.5, color='b')
plt.show()