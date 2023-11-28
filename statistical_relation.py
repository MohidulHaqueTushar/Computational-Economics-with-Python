# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 03:18:57 2022

@author: Md Mohidul Haque
"""

"""Import Necessary Modules"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm

""" Read Data Set's """
df_unemploymentRate = pd.read_csv("LMUNRRTTDEM156S.csv")
df_unfilled_job = pd.read_csv("LMJVTTUVDEQ647S.csv")

"""Print Data"""
print("The data of Unemployment Rate of Germany is: \n\n ", df_unemploymentRate)
print("\nThe data of unfilled job vacancies in Germany is: \n\n ", df_unfilled_job)

""" Clean Data Sets"""

""" Fix Column Names"""
df_unemploymentRate.columns = ["Date", "UnemploymentRate"]
df_unfilled_job.columns = ["Date", "UnfilledJob"]

""" Typecast Date Column into pd.datetime"""
df_unemploymentRate["Date"] = pd.to_datetime(df_unemploymentRate["Date"])
df_unfilled_job["Date"] = pd.to_datetime(df_unfilled_job["Date"])

print("\nDescribe the Unemployment Rate data of Germany: \n\n ", df_unemploymentRate.describe(include = 'all'))
print("\nDescribe unfilled job vacancies data of Germany: \n\n ", df_unfilled_job.describe(include = 'all'))

""" Merge data sets"""
df = pd.merge(df_unemploymentRate, df_unfilled_job, on="Date", how="inner")

"""sorting data frames """
df = df.sort_values("Date")

"""Print merge data"""
print("\nThe data set after merging:\n\n",df)

"""How many rows each data frame loose"""
print("\nAfter merging two data sets,\n\ndf_unemploymentRate data loses {} rows.".format(df_unemploymentRate.shape[0] - df.shape[0]))
print("and df_unfilled_job data loses {} rows.".format(df_unfilled_job.shape[0] - df.shape[0]))

"Describe merge data"
print("\nMore details about the merge data:\n\n",df.describe(include = 'all'))

""" Compute the Growth Rates"""
df["Growth_UR"] = df["UnemploymentRate"].pct_change(periods=4)
df["Growth_UJ"] = df["UnfilledJob"].pct_change(periods=4)

"""Calculate the correlation of the data df"""
print("\nThe correlation of the data df are:\n\n",df.corr())

""" Plot Data"""
fig, ax = plt.subplots(nrows=1, ncols=1, squeeze=False)
ax[0][0].scatter(df["Growth_UR"], df["Growth_UJ"], color="b", s=5)
ax[0][0].set_xlabel("Growth of Unemployment Rate")
ax[0][0].set_ylabel("Growth of unfilled job vacancies")
"save figure as pdf"
plt.savefig("Scatter plot of Growth_UJ against Growth_UR.pdf")
"save figure as image"
plt.savefig("Scatter plot of Growth_UJ against Growth_UR.png", dpi=300)

plt.show()

""" Perform Regression"""
"""define linear regression model"""
linear_model = smf.ols(formula="Growth_UJ ~ Growth_UR", data=df)

"""fit the linear model"""
linear_model_fit = linear_model.fit()

"""Print Intercept and coefficient"""
print("\nIntercept and coefficient:\n\n",linear_model_fit.params)

"""Print all the details about the regression """
print("\nMore extensive summary of the fit:\n\n",linear_model_fit.summary())

""" Additional Analysis"""

"""Component and component plus residual plot"""
fig1 = sm.graphics.plot_ccpr(linear_model_fit, "Growth_UR")
fig1.tight_layout()
"save figure as pdf"
plt.savefig("CCPR plot.pdf")
"save figure as image"
plt.savefig("CCPR plot.png", dpi=300)
plt.show()

"""Fit Plot"""
fig2 = sm.graphics.plot_fit(linear_model_fit, "Growth_UR")
fig2.tight_layout()
"save figure as pdf"
plt.savefig("Fit plot.pdf")
"save figure as image"
plt.savefig("Fit plot.png", dpi=300)
plt.show()

"""Influence plot"""
fig3 = sm.graphics.influence_plot(linear_model_fit, criterion="cooks")
fig3.tight_layout()
"save figure as pdf"
plt.savefig("Influence plot.pdf")
"save figure as image"
plt.savefig("Influence plot.png", dpi=300)

plt.show()

"""QQ plot"""
fig4 = sm.qqplot(linear_model_fit.resid, line="s")
fig4.tight_layout()
plt.savefig("QQ plot.pdf")
"save figure as image"
plt.savefig("QQ plot.png", dpi=300)
plt.show()

"""Histrogram"""
fig, ax = plt.subplots(nrows = 1, ncols = 1, squeeze = False)
ax[0][0].hist(df["Growth_UR"], bins = 100, color = 'b', alpha = 0.6, rwidth = 0.85, label = 'Growth_UR')
ax[0][0].hist(df["Growth_UJ"], bins = 100, color = 'g', alpha = 0.6, rwidth = 0.85, label = 'Growth_HJ')
ax[0][0].legend()
ax[0][0].set_xlabel('X')
ax[0][0].set_ylabel('Frequency')

plt.tight_layout()
plt.savefig("Histrogram of Growth_UR and Growth_UJ.pdf")
"save figure as image"
plt.savefig("Histrogram of Growth_UR and Growth_UJ.png", dpi=300)
plt.show()