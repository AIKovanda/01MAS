import numpy as np
from multiprocessing import Pool # použití více jader procesoru
import matplotlib.pyplot as plt
num_bins=512
plt.hist(np.random.exponential(.5,10000000), num_bins, range=[.0, 3.], facecolor='blue', alpha=.6,density=True)
plt.savefig("histexp0.pdf")
plt.close()

def histgen(x):
    plt.hist([np.mean(np.random.exponential(.5,x))for i in range(10000000)], num_bins, range=[.0, 3.], facecolor='blue', alpha=0.6,density=True)
    plt.savefig("histexp{}.pdf".format(x))
    plt.close()

pool = Pool(8)
pool.map(histgen, [i for i in [2,10,50,100,1000]])

def histgenvar(x):
    plt.hist([np.mean((np.random.exponential(.5,x)-0.5)**2)for i in range(10000000)], num_bins, range=[.0, 3.], facecolor='blue', alpha=0.6,density=True)
    plt.savefig("histexp_var{}.pdf".format(x))
    plt.close()

pool = Pool(8)
pool.map(histgenvar, [i for i in [2,10,50,100,1000]])

