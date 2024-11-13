import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("C://Users/win-10/Downloads/matches.csv")
matches_per_season=data.groupby('Season').size().reset_index(name='match_count')
print(matches_per_season)
plt.bar(matches_per_season['Season'],matches_per_season['match_count'])
plt.xlabel('Season')
plt.ylabel('number of matches')
plt.title('number of matches in each Seasons')
plt.show()