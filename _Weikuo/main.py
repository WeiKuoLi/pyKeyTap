import numpy as np
from sklearn.cluster import KMeans

def _generate_test(n_samples=1000, n_features=5, n_clusters=10, noise_level=1.2):
    np.random.seed(0)
    noise = np.random.randn(n_samples, n_features) * noise_level
    
    clean = np.random.randn(n_clusters, n_features)
    data = []
    ground_truth = []
    for i in range(n_samples):
        _key = int(np.random.randint(0, n_clusters))
        ground_truth.append(_key)
        data.append(clean[_key,:] + noise[i,:])
    return data, ground_truth   

def _check(labels, ground_truth):
    _dict = {}
    for i in range(len(labels)):
        label = int(labels[i])
        ans = int(ground_truth[i])
        if label not in _dict:
            _dict[label] = {ans:1}
        else:
            if ans not in _dict[label]:
                _dict[label][ans] = 1
            else:
                _dict[label][ans] += 1
    return _dict


if __name__ == '__main__':
    data, ground_truth = _generate_test()
    data = np.array(data)
    ground_truth = np.array(ground_truth)
    print(data.shape, ground_truth.shape)
    kmeans = KMeans(n_clusters=10, random_state=0).fit(data)
    labels = kmeans.labels_
    

    mapping = _check(labels, ground_truth)
    for i in range(10):
        print(i, mapping[i])
