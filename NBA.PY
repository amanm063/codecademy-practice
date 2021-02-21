#HERE IS THE LINK TO THE DATA
#https://projects.fivethirtyeight.com/complete-history-of-the-nba/#lakers
#HERE IS SOME MORE USEFUL INFO ABOUT THE DATA
#https://github.com/fivethirtyeight/data/tree/master/nba-elo

import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

import codecademylib3
np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

knicks_pts = nba_2010.pts[nba_2010.fran_id == "Knicks"]
nets_pts = nba_2010.pts[nba_2010.fran_id == "Nets"]

knicks_mean = np.mean(knicks_pts)
nets_mean = np.mean(nets_pts)

diff_means_2010 = knicks_mean - nets_mean
print(diff_means_2010)

plt.hist(knicks_pts ,alpha = 0.5,normed = True,label = "knicks")
plt.hist(nets_pts ,alpha = 0.5,normed = True,label = "nets")
plt.legend()
plt.show()


knicks_pts_2014 = nba_2014.pts[nba_2014.fran_id == "Knicks"]
nets_pts_2014 = nba_2014.pts[nba_2014.fran_id == "Nets"]

knicks_mean_2014 = np.mean(knicks_pts_2014)
nets_mean_2014 = np.mean(nets_pts_2014)

diff_means_2014 = knicks_mean_2014 - nets_mean_2014
print(diff_means_2014)
plt.clf()
plt.hist(knicks_pts_2014 ,alpha = 0.5,normed = True,label = "knicks")
plt.hist(nets_pts_2014 ,alpha = 0.5,normed = True,label = "nets")
plt.legend()

plt.show()

plt.clf()
sns.boxplot(data = nba_2010 , x="fran_id",y = "pts")
plt.show()

location_result_freq = pd.crosstab(nba_2010["game_result"], nba_2010["game_location"])
print(location_result_freq)

location_result_porp = location_result_freq/len(nba_2010["game_location"])
print(location_result_porp)

chi2, pval, dof, expected = chi2_contingency(location_result_freq)
print(expected)
print(chi2)


covariance = np.cov(nba_2010.forecast , nba_2010.point_diff)

print(covariance)

point_diff_forecast_corr = pearsonr(nba_2010.forecast, nba_2010.point_diff)
print(point_diff_forecast_corr)

plt.clf()
plt.scatter('forecast', 'point_diff', data=nba)
plt.xlabel('Forecasted Win Probability')
plt.ylabel('Point Differential')
plt.show()
