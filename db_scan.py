def db_scan_clustering(df, lat_col, long_col, max_distance, min_sample):
    '''
    Identifes clusters from a sample of points. Clusters are based on closest distance, however
    what defines a cluster is qualified below. The user can specify a minimum number of points 
    needed to form a cluster, as well as specifying the maximum distance which should seperate
    one cluster from another.
    
    df              Your dataframe of points, including longitude and latitude coordinates.
    long_col        The column containing longitude coordinates
    latitude_col    The column containing latitude coordinates
    max distance    The maximum distance (in meters) between a cluster and a point in order
                    for it to be considered a part of the same cluster.
    min sample      The minimum number of points needed to form a cluster
    
    Returns a series of cluster labels. Points which recieve a cluster label of '0' do not qualify
    to fit into any cluster.

    '''
    
    from sklearn.cluster import DBSCAN
    
    def greatCircleDistance(x, y):
      '''
      Calculates distance between two points. x and y prepresent points.
      Requires points in a tuple format: ie [y, x],[x,y]
      '''
      from geopy.distance import vincenty
      lat1, lon1 = x[0], x[1]
      lat2, lon2 = y[0], y[1]
      return vincenty((lat1, lon1), (lat2, lon2)).meters
    
    X = df[['latitude', 'longitude']].values
    est = DBSCAN(eps=max_distance, min_samples=min_sample, metric=greatCircleDistance).fit(X)
    return est.labels_.tolist()