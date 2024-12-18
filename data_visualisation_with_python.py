# -*- coding: utf-8 -*-
"""CW_DataVisualisation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UfzT5f0tbabN6770ugpnFae5rFM-9KNF

# **Importing libraries and reading datasets**
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
!pip install -U matplotlib pandas

dailycustomers = pd.read_csv('https://tinyurl.com/ChrisCoDV/001258010/OutletDailyCustomers.csv', index_col=0)
dailycustomers = dailycustomers.reindex(dailycustomers.sum().sort_values(ascending=False).index, axis = 1)
outletmarketing = pd.read_csv('https://tinyurl.com/ChrisCoDV/001258010/OutletMarketing.csv', index_col=0)
outletoverheads = pd.read_csv('https://tinyurl.com/ChrisCoDV/001258010/OutletOverheads.csv', index_col=0)
outletsize = pd.read_csv('https://tinyurl.com/ChrisCoDV/001258010/OutletSize.csv', index_col=0)
outletstaff = pd.read_csv('https://tinyurl.com/ChrisCoDV/001258010/OutletStaff.csv', index_col=0)

print(dailycustomers.head())
print(dailycustomers.sum().head())

"""# **Reading Summary Data**



"""

summary_data=pd.DataFrame(index=dailycustomers.columns)
summary_data['Outlet_Marketing']=outletmarketing.values
summary_data['Outlet_Overheads']=outletoverheads.values
summary_data['Outlet_Size']=outletsize.values
summary_data['Outlet_Staff']=outletstaff.values
summary_data['Daily_Visitors']=dailycustomers.sum().values

print(dailycustomers.head())

print(summary_data.head())
print(summary_data.describe())

"""# **Bar chart for total customers by outlets**"""

# data.sum().plot.bar(width=0.8, rot=0, figsize=(8, 8))
plt.figure(figsize=(20, 8))
x_pos = np.arange(len(dailycustomers.columns))
plt.bar(x_pos, dailycustomers.sum(), align='center')
plt.xticks(x_pos, dailycustomers.columns)
plt.xlabel('Outlets', fontsize=18)
plt.ylabel('Daily Customers', fontsize=18)
plt.title('Total Customers Visited Outlets', fontsize=20)
plt.show()

"""**Segmenting customers (Manual)**



"""

high = dailycustomers.columns[dailycustomers.sum()>500_000]
print(dailycustomers[high].head())

high = ['RAN', 'RFY', 'DMN']
medium = ['EYS', 'DSA', 'EEC', 'BMF','BSQ','CYK','CGV']
low = ['DHJ','END','DTO','OZW','NFH','LLK','OTL','PLB','FZI','GNL','IFI','EHT','LTU','QZF','FTW','MZO','PFQ','CNW','HZQ','CTH']

print(dailycustomers.sum())

"""# **Segmenting Customers by the number of visits**



"""

import pandas as pd
from matplotlib import pyplot as plt

categories = ['High', 'Medium', 'Low']
colours = []

categories_selected = [[] for i in range(len(categories))]
for name in dailycustomers.columns:
    total_customers = dailycustomers[name].sum()
    if total_customers > 600_000:
        category = 0
        colour = 'orange'

    elif total_customers > 250_000:
        category = 1
        colour = 'green'
    else:
        category = 2
        colour = 'blue'
    colours.append(colour)
    categories_selected[category].append(name)
    #print('Outlet ' + name + ' is ' + categories[category] + ' volume')


plt.figure(figsize=(20, 8))
x_pos = np.arange(len(dailycustomers.columns))
plt.bar(x_pos, dailycustomers.sum(), align='center', color=colours)
plt.xticks(x_pos, dailycustomers.columns, rotation = 90)
plt.xlabel('Outlets', fontsize=18)
plt.ylabel('Customers', fontsize=18)
plt.title('Total Customers Visited Outlets by Segments', fontsize=20)
plt.show()

plt.figure(figsize=(30, 12))
counter = 1
x_pos = np.arange(len(summary_data.index))
for attribute in summary_data:
    sub = plt.subplot(3, 3, counter)
    sub.bar(x_pos, summary_data[attribute], align='center')
    sub.set_xticks([])
    sub.set_xticks(x_pos)
    sub.set_xticklabels(summary_data.index, rotation=45)
    sub.set_xlabel('Outlets', fontsize=12)
    sub.set_ylabel(attribute, fontsize=12)
    counter += 1
plt.tight_layout()
plt.show()

"""# **Heatmap for Correlation**"""

customers = pd.read_csv('https://tinyurl.com/ChrisCoDV/001258010/OutletDailyCustomers.csv', index_col=0)
marketing = pd.read_csv('https://tinyurl.com/ChrisCoDV/001258010/OutletMarketing.csv', index_col=0)
overheads = pd.read_csv('https://tinyurl.com/ChrisCoDV/001258010/OutletOverheads.csv', index_col=0)
size = pd.read_csv('https://tinyurl.com/ChrisCoDV/001258010/OutletSize.csv', index_col=0)
staff = pd.read_csv('https://tinyurl.com/ChrisCoDV/001258010/OutletStaff.csv', index_col=0)

sum_data=pd.DataFrame(index=customers.columns)
sum_data['Outlet_Marketing']=marketing.values
sum_data['Outlet_Overheads']=overheads.values
sum_data['Outlet_Size']=size.values
sum_data['Outlet_Staff']=staff.values
sum_data['Outlet_Customers']=customers.sum().values

plt.figure(figsize=(8, 8))
plt.title('Correlations between the variables', fontsize=20)
corr = sum_data.corr()
ax = sns.heatmap(corr, vmin=-1, vmax=1, center=0, cmap=sns.diverging_palette(220, 20, n=200), square=True, annot=True,
                 annot_kws={"size": 8})
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.show()

High = ['RAN', 'RFY', 'DMN']


counter = 1
fig = plt.figure(figsize=(8, 8))
fig.suptitle('Customers visiting correlations', fontsize=14, position=(0.5, 1.0))
for i, name_i in enumerate(High):
    for j in range(i + 1, len(High)):
        name_j = High[j]
        sub = fig.add_subplot(3, 3, counter)
        sub.set_title(name_i + ' vs ' + name_j, fontsize=10)
        sub.scatter(dailycustomers[name_i], dailycustomers[name_j], s=0.5)
        counter += 1
plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.tight_layout()
plt.show()

"""


# **Line Chart for Time Series**
"""

period = 14
rolling_average = dailycustomers.rolling(window=period).mean()
dailycustomers.index = pd.to_datetime(dailycustomers.index)

selected=['RAN', 'RFY', 'DMN']
print(dailycustomers[selected].head())

plt.figure(figsize=(15, 8))
plt.plot(dailycustomers[selected], linewidth=0.5)
plt.gca().set_prop_cycle(None)
plt.plot(rolling_average[selected], linewidth=2)
plt.gca().set_prop_cycle(None)
for name in selected:
    x = np.arange(len(dailycustomers[name]))
    z = np.polyfit(x, dailycustomers[name], 1)
    trend = np.poly1d(z)
    plt.plot(dailycustomers.index, trend(x), linestyle='--')
plt.ylim(ymin=0) #y xis starts from 0
plt.xlabel('Date', fontsize=18)
plt.ylabel('Customers', fontsize=18)
plt.title('Trend for High Volume Outlets (14 days rolling average)', fontsize=20)
plt.legend(selected, loc=2)
plt.show()

period = 14
rolling_average = dailycustomers.rolling(window=period).mean()

Medium = ['EYS', 'DSA', 'EEC', 'BMF','BSQ','CYK','CGV']
print(dailycustomers[Medium].head())

plt.figure(figsize=(15, 8))
plt.plot(dailycustomers[Medium], linewidth=0.5)
plt.gca().set_prop_cycle(None)
plt.plot(rolling_average[Medium], linewidth=2)
plt.gca().set_prop_cycle(None)
for name in Medium:
    x = np.arange(len(dailycustomers[name]))
    z = np.polyfit(x, dailycustomers[name], 1)
    trend = np.poly1d(z)
    plt.plot(dailycustomers.index, trend(x), linestyle='--')
plt.ylim(ymin=0) #y xis starts from 0
plt.xlabel('Date', fontsize=18)
plt.ylabel('Customers', fontsize=18)
plt.title('Trend for Medium Volume Outlets (14 days rolling average)', fontsize=20)
plt.legend(Medium, loc=2)
plt.show()

"""eliminate some of noise by using averages. plotting 14 days instead of daily data.  I computed the average of last 14 days. There is more smoother line."""

# sort the data according to the sum of each column
data = dailycustomers.reindex(dailycustomers.sum().sort_values(ascending=False).index, axis=1)

plt.figure(figsize=(8, 8))
# data.plot.area(figsize=(8, 8))
plt.stackplot(data.index, data[High].transpose())
plt.xlabel('Date', fontsize=18)
plt.ylabel('Customer', fontsize=18)
plt.title('The number of High Volume Customers', fontsize=20)
plt.legend(data.columns, loc=2)
plt.show()

# sort the data according to the sum of each column
data = dailycustomers.reindex(dailycustomers.sum().sort_values(ascending=False).index, axis=1)
plt.figure(figsize=(8, 8))
# data.plot.area(figsize=(8, 8))
plt.stackplot(data.index, data[Medium].transpose())
plt.xlabel('Date', fontsize=18)
plt.ylabel('Customer', fontsize=18)
plt.title('The number of Medium Volume Customers', fontsize=20)
plt.legend(data.columns, loc=2)
plt.show()

"""# **BOX PLOTS**"""

plt.figure(figsize=(20, 8))
# data[selected].boxplot()
plt.boxplot(dailycustomers[Medium], labels=Medium)
plt.xlabel('Outlets', fontsize=18)
plt.ylabel('Customers visiting per day', fontsize=18)
plt.title('Distributions of Medium volume customers visiting outlets', fontsize=20)
plt.show()

x_min = 800
x_max = 3000
bin_width = 70

n_bins = int((bin_width + x_max - x_min) / bin_width)
print(str(n_bins) + ' bins')
bins = [(x_min + x * (bin_width + x_max - x_min) / n_bins) for x in range(int(n_bins))]

fig = plt.figure(figsize=(8, 8))
fig.suptitle('High volume product sales distributions', fontsize=20, position=(0.5, 1.0))
counter = 1
for name in High:
    sub = fig.add_subplot(2, 2, counter)
    sub.hist(dailycustomers[name], bins, edgecolor='w')
    sub.set_title('Outlet ' + name, fontsize=10)
    sub.set_xlim(xmin=x_min, xmax=x_max)
    sub.set_ylim(ymin=0, ymax=140)
    counter += 1
# plt.subplots_adjust(wspace=0.4, hspace=0.4)
plt.show()

x_min = 250
x_max = 1500
bin_width = 70

n_bins = int((bin_width + x_max - x_min) / bin_width)
print(str(n_bins) + ' bins')
bins = [(x_min + x * (bin_width + x_max - x_min) / n_bins) for x in range(int(n_bins))]

fig = plt.figure(figsize=(12, 8))
fig.suptitle('Medium volume product sales distributions', fontsize=20, position=(0.5, 1.0))
counter = 1
for name in Medium:
    sub = fig.add_subplot(3, 3, counter)
    sub.hist(dailycustomers[name], bins, edgecolor='w')
    sub.set_title('Outlet ' + name, fontsize=10)
    sub.set_xlim(xmin=x_min, xmax=x_max)
    sub.set_ylim(ymin=0, ymax=140)
    counter += 1
# plt.subplots_adjust(wspace=0.4, hspace=0.4)
plt.show()

"""# **Radar Charts**"""

sum_data=pd.DataFrame(index=customers.columns)
sum_data['Outlet_Staff']=staff.values
sum_data['Outlet_Size']=size.values
sum_data['Outlet_Customers']=customers.sum().values
sum_data['Outlet_Marketing']=marketing.values
sum_data['Outlet_Overheads']=overheads.values


normalised_data = sum_data / sum_data.max()
print(normalised_data.head())

n_attributes = len(normalised_data.columns)
angles = [n / float(n_attributes) * 2 * np.pi for n in range(n_attributes + 1)]
plt.figure(figsize=(20, 20))
counter = 1
for name in High:
    values = normalised_data.loc[[name]].values.flatten().tolist()
    values += values[:1]
    sub = plt.subplot(5, 5, counter, polar=True)
    sub.plot(angles, values)
    sub.fill(angles, values, alpha=0.1)
    sub.set_ylim(ymax=1.05)
    sub.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    sub.set_xticks(angles[0:-1])
    sub.set_xticklabels(normalised_data.columns, fontsize=8)
    sub.set_title('Outlet ' + name, fontsize=12, loc='left')
    counter += 1
plt.tight_layout()
plt.show()

Medium = ['EYS', 'DSA', 'EEC', 'BMF', 'BSQ', 'CYK', 'CGV']
normalised_data = sum_data / sum_data.loc[Medium].max() #normalising

n_attributes = len(normalised_data.columns)
angles = [n / float(n_attributes) * 2 * np.pi for n in range(n_attributes + 1)]
plt.figure(figsize=(20, 20))
counter = 1
for name in Medium:
    values = normalised_data.loc[[name]].values.flatten().tolist()
    values += values[:1]
    sub = plt.subplot(6, 6, counter, polar=True)
    sub.plot(angles, values)
    sub.fill(angles, values, alpha=0.1)
    sub.set_ylim(ymax=1.05)
    sub.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    sub.set_xticks(angles[0:-1])
    sub.set_xticklabels(normalised_data.columns, fontsize=8)
    sub.set_title('Outlet ' + name, fontsize=12, loc='left')
    counter += 1
plt.tight_layout()
plt.show()

s_data=pd.DataFrame(index=customers.columns)
s_data['Outlet_Customers']=customers.sum().values
s_data['Outlet_Size']=size.values
s_data['Outlet_Staff']=staff.values
s_data['Outlet_Marketing']=marketing.values
s_data['Outlet_Overheads']=overheads.values

norm_data = s_data / s_data.max()
print(norm_data.head())

sel = ['RAN', 'RFY', 'DMN']


n_attributes = len(norm_data.columns)
angles = [n / float(n_attributes) * 2 * np.pi for n in range(n_attributes + 1)]
colours = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
c = 0
plt.figure(figsize=(8, 8))
sub = plt.subplot(1, 1, 1, polar=True)
for name in sel:
    values = norm_data.loc[[name]].values.flatten().tolist()
    values += values[:1]
    sub.plot(angles, values, colours[c % len(colours)], label='Outlet ' + name)
    sub.fill(angles, values, colours[c % len(colours)], alpha=0.1)
    sub.set_ylim(ymax=1.05)
    sub.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    sub.set_xticks(angles[0:-1])
    sub.set_xticklabels(norm_data.columns)
    c += 1
plt.legend(loc=4)
plt.show()

s_data=pd.DataFrame(index=customers.columns)
s_data['Outlet_Customers']=customers.sum().values
s_data['Outlet_Size']=size.values
s_data['Outlet_Staff']=staff.values
s_data['Outlet_Marketing']=marketing.values
s_data['Outlet_Overheads']=overheads.values

norm_data = s_data / s_data.max()
print(norm_data.head())

sel_m = ['EYS', 'DSA', 'EEC', 'BMF', 'BSQ', 'CYK', 'CGV']


n_attributes = len(norm_data.columns)
angles = [n / float(n_attributes) * 2 * np.pi for n in range(n_attributes + 1)]
colours = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
c = 0
plt.figure(figsize=(8, 8))
sub = plt.subplot(1, 1, 1, polar=True)
for name in sel_m:
    values = norm_data.loc[[name]].values.flatten().tolist()
    values += values[:1]
    sub.plot(angles, values, colours[c % len(colours)], label='Outlet ' + name)
    sub.fill(angles, values, colours[c % len(colours)], alpha=0.1)
    sub.set_ylim(ymax=1.05)
    sub.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    sub.set_xticks(angles[0:-1])
    sub.set_xticklabels(norm_data.columns)
    c += 1
plt.legend(loc=4)
plt.show()

"""# **Comparative Bar Chart**"""

# selected = ['G', 'H', 'J', 'S', 'W']  # medium volume
# selected = ['D', 'E', 'M', 'O', 'P', 'T', 'X']  # low volume

selected = ['RAN', 'RFY', 'DMN']  # high volume
colours = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
plt.figure(figsize=(15, 8))
c = 0
n_bars = len(sel_m)
x_pos_base = np.arange(len(s_data.columns))
bar_width = 0.8 / n_bars
for name in sel_m:
    values = norm_data.loc[[name]].values.flatten().tolist()
    x_pos = [x + (bar_width * c) for x in x_pos_base]
    plt.bar(x_pos, values, color=colours[c % len(colours)],
            width=bar_width, edgecolor='white', label='Outlet ' + name)
    c += 1
plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0])
x_pos = [x + (bar_width * (c - 1) / 2) for x in x_pos_base]
plt.xticks(x_pos, s_data.columns)
plt.title('Comparative Bar Chart for Medium Volume Outlets', fontsize=20, position=(0.5, 1.0))
plt.legend()
plt.show()

# selected = ['G', 'H', 'J', 'S', 'W']  # medium volume
# selected = ['D', 'E', 'M', 'O', 'P', 'T', 'X']  # low volume

selected = ['RAN', 'RFY', 'DMN']  # high volume
colours = ['y', 'g', 'b']
plt.figure(figsize=(15, 8))
c = 0
n_bars = len(sel)
x_pos_base = np.arange(len(s_data.columns))
bar_width = 0.8 / n_bars
for name in sel:
    values = norm_data.loc[[name]].values.flatten().tolist()
    x_pos = [x + (bar_width * c) for x in x_pos_base]
    plt.bar(x_pos, values, color=colours[c % len(colours)],
            width=bar_width, edgecolor='white', label='Outlet ' + name)
    c += 1
plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0])
x_pos = [x + (bar_width * (c - 1) / 2) for x in x_pos_base]
plt.xticks(x_pos, s_data.columns)
plt.title('Comparative Bar Chart for High Volume Outlets',fontsize=20, position=(0.5, 1.0))
plt.legend()
plt.show()

"""I organized the columns, I ordered the positve measures to the beginning order."""

import seaborn as sns
sns.pairplot(sum_data, height=1.5, plot_kws={'s': 20} )

"""There are high correlation between the staff, size and marketing. The bigger

outlets need the bigger staff. As we expect, for big stores the more spending on marketing needs. More customers are received by big stores compared to the other stores.

# **INTERACTIVE PLOTS**
"""

!pip install hvplot
import holoviews as hv

selected = ['RAN','RFY','DMN']

import hvplot.pandas
dailycustomers.index = pd.to_datetime(dailycustomers.index)
plot = dailycustomers[selected].hvplot.line(
    frame_height=500, frame_width=500,
    xlabel='Date', ylabel='Daily Customers',
    title='Interactive Line Plot for High Volume Outlets'
)

hv.extension('bokeh')
plot

Med = ['EYS', 'DSA', 'EEC', 'BMF', 'BSQ', 'CYK', 'CGV']

import hvplot.pandas
dailycustomers.index = pd.to_datetime(dailycustomers.index)
plot = dailycustomers[Med].hvplot.line(
    frame_height=500, frame_width=500,
    xlabel='Date', ylabel='Daily Customers',
    title='Interactive Line Graph for Medium Volume Outlets'
)

hv.extension('bokeh')
plot

x_min = 800
x_max = 3100
bin_width = 10
n_bins = int((bin_width + x_max - x_min) / bin_width)
print(str(n_bins) + ' bins')
bins = [(x_min + x * (bin_width + x_max - x_min) / n_bins) for x in range(int(n_bins))]

plot = dailycustomers[selected].hvplot.hist(
    frame_height=500, frame_width=500,
    xlabel='Daily customer', ylabel='Frequency',
    title='High Volume Outlets',
    alpha=0.5, muted_alpha=0, muted_fill_alpha=0, muted_line_alpha=0,
    tools=['pan', 'box_zoom', 'wheel_zoom', 'undo', 'redo', 'hover', 'save', 'reset'],
    bins=bins
)
hv.extension('bokeh')
plot

x_min = 300
x_max = 1500
bin_width = 10
n_bins = int((bin_width + x_max - x_min) / bin_width)
print(str(n_bins) + ' bins')
bins = [(x_min + x * (bin_width + x_max - x_min) / n_bins) for x in range(int(n_bins))]

plot = dailycustomers[Med].hvplot.hist(
    frame_height=500, frame_width=500,
    xlabel='Daily customer', ylabel='Frequency',
    title='Medium Volume Outlets',
    alpha=0.5, muted_alpha=0, muted_fill_alpha=0, muted_line_alpha=0,
    tools=['pan', 'box_zoom', 'wheel_zoom', 'undo', 'redo', 'hover', 'save', 'reset'],
    bins=bins
)
hv.extension('bokeh')
plot

print(sum_data.head())

sum_data['BubbleSize'] = sum_data['Outlet_Marketing'] * 0.08

plot = sum_data.hvplot.scatter(
    frame_height=500, frame_width=500,
    title='Customers vs Store Size (vs Marketing)',
    xlabel='Customers', ylabel='Outlet Size',
    alpha=0.5, padding=0.1, hover_cols='all',
    tools=['pan', 'box_zoom', 'wheel_zoom', 'undo', 'redo', 'hover', 'save', 'reset'],
    x='Outlet_Customers', y='Outlet_Size', size='BubbleSize'
)
hv.extension('bokeh')
plot