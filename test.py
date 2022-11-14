import matplotlib.pyplot as plt
plt.style.use('seaborn')
def main():
    data=[]
    f = open("NASAtext.rtf", "r")
    scan(f, data)
    plt.title('Test')
    'plt.scatter(*zip(*data), linewidth=.05, alpha=0.75)'
    plt.plot(*zip(*data))
    plt.show()

def scan(f, data):
    lines = f.readlines()
    total = 1
    word = "E0= "
    for r in lines:
        if word in r:
            energy = r.split()
            energy= energy[8]
            energy= float(energy[0:10])*10000
            energy= float(format(energy, '.4f'))
            data.append([total, energy])
            total+=1
main()


