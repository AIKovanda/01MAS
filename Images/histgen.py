import numpy as np
from multiprocessing import Pool # použití více jader procesoru
import matplotlib.pyplot as plt
num_bins=512
plt.hist(np.random.normal(1.,2.,10000000), num_bins, range=[-7., 9.], facecolor='blue', alpha=.6,density=True)
plt.savefig("hist0.pdf")
plt.close()

def histgen(x):
    plt.hist([np.mean(np.random.normal(1.,2.,10**x))for i in range(10000000)], num_bins, range=[-7., 9.], facecolor='blue', alpha=0.6,density=True)
    plt.savefig("hist{}.pdf".format(x))
    plt.close()

pool = Pool(8)
pool.map(histgen, [i for i in range(1,5)])
