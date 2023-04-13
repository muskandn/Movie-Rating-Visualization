import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10,7))
info=['gold','silver','bronze','total']
au=[80,59,59,198]
eng=[45,45,46,136]
ind=[26,20,20,66]
can=[15,40,27,82]
X=np.arange(len(info))
plt.bar(info,au,width=.15)
plt.bar(X+.15,eng,width=.15)
plt.bar(X+.30,ind,width=.15)
plt.bar(X+.45,can,width=.15)
plt.show()