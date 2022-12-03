!wget https://www.dropbox.com/s/3uqleyc3wyz52tr/residuals_261.pkl -P ./data/ 
import seaborn as sb
import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = np.load('data/residuals_261.pkl', allow_pickle=True).item()
dataset = pd.DataFrame(data) 
dataset = dataset[abs(dataset['residuals'])<2]

corr = dataset[['residuals','distances']].corr()
print(corr)
# residuals and distances are not correlated!

plot1 = sb.jointplot(x='distances', y='residuals', data=dataset, kind="reg", joint_kws={'line_kws':{'color':'b', 'label':'Regression'}})
plot1.ax_joint.legend()
plot1.fig.set_size_inches(8,8)
plt.show()

bin = 25
(n, bins, patches) = plt.hist(dataset['distances'], bins=bin, alpha=0.5, edgecolor='white', range=(0,20))
plt.title("Distances")
plt.show()


x=(bins[1:]+bins[:-1])*0.5
print(f"x:\n{x}")

y = [dataset["residuals"][(dataset['distances'] >=bins[i]) & (dataset['distances'] <=bins[i+1])].mean() for i in range(bin)]
print(f"\ny:\n{y}")

err_y = [dataset["residuals"][(dataset['distances'] >bins[i]) & (dataset['distances'] <bins[i+1])].std() for i in range(bin)]
print(f"\nerr_y:\n{err_y}")


#plot2 = sb.jointplot(x='distances', y='residuals', data=data, kind="reg", joint_kws={'line_kws':{'color':'b', 'label':'Regression'}}) #scatter
plot2.fig.set_size_inches(10,10)
plt.sca(plot2.ax_joint)
plt.errorbar(x=x, y=y , yerr=err_y, marker = 'o', color = 'r', xlolims=22, label="Profile") #profile
plt.legend()
plt.show()