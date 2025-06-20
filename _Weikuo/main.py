import numpy as np
from sklearn.cluster import KMeans

_chars = '\%ˆ>|¡w?€=§[c¬•_¢(y∫i∆]zb∏p+8!:k{µ&7#g∞uh0¿∑¨j¶£df3®evl@16±√qs/.¥m,™}`‡t÷-\"$n°4∇\'~xo†9*×25;©¯r)<¤a^'
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


def _get_code_kmeans(data, n_clusters=26):
    data = np.array(data)
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(data)
    labels = kmeans.labels_
    code = [_chars[i] for i in labels]
    code = ''.join(code)
    return code

def get_code(data,*args,**kwargs):
    return  _get_code_kmeans(data,*args,**kwargs)

def test():
    data, ground_truth = _generate_test()
    data = np.array(data)
    ground_truth = np.array(ground_truth)
    kmeans = KMeans(n_clusters=10, random_state=0).fit(data)
    labels = kmeans.labels_
    code = [_chars[i] for i in labels]
    code = ''.join(code)

    mapping = _check(labels, ground_truth)
    for i in range(10):
        print('mapping: ',i,'->', mapping[i])
    
    print("\nextracted code: ")
    print("\033[32m", code, "\033[0m")

if __name__ == '__main__':
    # creates a list of 1d np arrays as list of embeddings, and a list of ints as ground truth
    data, ground_truth = _generate_test(n_clusters=10)

    # get extracted code
    code = get_code(data, n_clusters=10)

    print("\nextracted code: ")
    print("\033[32m", code, "\033[0m")
