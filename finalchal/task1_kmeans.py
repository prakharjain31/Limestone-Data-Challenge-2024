from sklearn import datasets # to retrieve the iris Dataset
import pandas as pd # to load the dataframe
from sklearn.preprocessing import StandardScaler # to standardize the features
from sklearn.decomposition import PCA # to apply PCA
from sklearn.cluster import KMeans
import seaborn as sns # to plot the heat maps
import matplotlib.pyplot as plt
from dict import players_trust_list


dataf = pd.DataFrame(players_trust_list , columns=["0" , "TC" , "CC" , "TT" , "CT" , "titfortat" , "trustperc" , "0" , "1" , "2","3","4","5","6","7"])
# print(dataf)
# heat_map = sns.heatmap(dataf.corr())
# plt.show()



#Standardize the features
#Create an object of StandardScaler which is present in sklearn.preprocessing
scalar = StandardScaler() 
scaled_data = pd.DataFrame(scalar.fit_transform(dataf)) #scaling the data
# print(scaled_data)
# heat_map = sns.heatmap(scaled_data.corr())
# plt.show()

#Applying PCA
#Taking no. of Principal Components as {n_components}

n_components = 3
pca = PCA(n_components = n_components)
pca_columns = [f'PC{i}' for i in range(1,n_components+1)]
pca.fit(scaled_data)
data_pca = pca.transform(scaled_data)
data_pca = pd.DataFrame(data_pca,columns=pca_columns)
# print(data_pca.head())
# heat_map = sns.heatmap(data_pca.corr())
# plt.show()


#initialize kmeans parameters
kmeans_kwargs = {
"init": "random",
"n_init": 10,
"random_state": 1,
}

#create list to hold SSE values for each k
sse = []
r = range(2, 15)
for k in r:
    kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
    kmeans.fit(data_pca)
    sse.append(kmeans.inertia_)

#visualize results
plt.plot(r, sse)
plt.xticks(r)
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.show()

n_clusters = 14
#instantiate the k-means class, using optimal number of clusters
kmeans = KMeans(init="random", n_clusters=n_clusters, n_init=10, random_state=1)

#fit k-means algorithm to data
kmeans.fit(data_pca)
dataf['cluster'] = kmeans.labels_
# print(kmeans.labels_)
# print(df)
# print(data_pca)



lulu = [[] for i in range(n_clusters)]
for ind in dataf.index:
    lulu[int(dataf["cluster"][ind])].append(ind)
for i in range(n_clusters):
    print(lulu[i])
    print(len(lulu[i]))