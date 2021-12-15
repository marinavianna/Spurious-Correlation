from matplotlib import pyplot as plt

years = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]
margarine = [3.7,3.2,2.9,2.4,2.3,1.8,2.1,2.1,1.9,1.7]
divorce = [5,4.7,4.6,4.4,4.3,4.1,4.2,4.2,4.2,4.1]

plt.plot(years,margarine, color = 'pink', marker = 'o')

plt.plot(years,divorce, color = 'gray', marker = 'o')

plt.show()