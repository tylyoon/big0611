import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
df.head()

sns.scatterplot(x=df['total_bill'],y=df['tip'])
plt.show()

sns.scatterplot(x=df['total_bill'],y=df['tip'], hue=df['sex'])
plt.show()
sns.scatterplot(x=df['total_bill'], y=df['tip'], hue=df['sex'], size=df['size'])
plt.show()
sns.scatterplot(x=df['total_bill'], y=df['tip'], 
                hue=df['sex'],      
                size=df['size'],    
                style=df['time'],  
                alpha=0.7)        