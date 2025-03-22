import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\Smpl Data Pd\Ice Cream Ratings.csv")
print(df)
print("---------------------------------------------------")
df.set_index('Date',inplace=True)
print(df)

# it gives the various styles of graphs
print(plt.style.available)
'''  Styles Available are:

'Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 
'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 
'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 
'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 
'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 
'tableau-colorblind10' ]

'''

plt.style.use('seaborn-v0_8-darkgrid')

# *******************************
# line chart
df.plot(figsize=[10,8])  # by default, it gives line plot
df.plot(kind='line',title='ICE CREAM RATING' ,xlabel="Daily Raing", ylabel="Score",legend=False)
df.plot(kind='line',subplots=True)   # plots the graph based on the col separately

# bar chart
df.plot(kind="bar")
df['Flavor Rating'].plot(kind="bar")  # only the specified col will be plotted

# stacked bar plot
df.plot(kind="bar", stacked=True)

# horizontal bar chart
# Note: No need to give 'kind' argument inside the plot()
df.plot.barh()
df['Overall Rating'].plot.barh()

# horizontal bar chart (Stacked)
df.plot.barh(stacked=True)

# Scatter plot
# Note: need to give 'x' & 'y' argument inside the plot()
# s --> size , c --> color
df.plot.scatter(x='Texture Rating',y='Flavor Rating', s=200, c='darkorange')


# histogram
df.plot.hist(bins=10, edgecolor='black', title="Ice cream Rating")

# Boxplot
df.boxplot(grid=False,figsize=[10,8], fontsize=15)
# df.plot.box() ---> another way
# figsize --> size of the plot in inches [width,height]

# Area chart
df.plot.area(figsize=[8,6])

# Pie Chart
# Note: Need the give 'y'(col-name) in the argument, based on the col it plots the chat
df.plot.pie(y='Flavor Rating',figsize=[18,8])

# autopct --> displays the values of each partition in pie
# labeldistance --> moves the label from the graph based on the distance given
df.plot.pie(y='Flavor Rating', figsize=[18,8],autopct='%1.f%%', labeldistance=1.01)




