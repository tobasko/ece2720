import csv
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as scis
import math
import codecs
u1 = codecs.open('/classes/ece2720/pe3/unicode1.dat', encoding='utf-8')
t1 = u1.readline()
print t1
u2 = codecs.open('/classes/ece2720/pe3/unicode2.dat', encoding='utf-32-le')
t2 = u2.readline()
print t2
u3 = codecs.open('/classes/ece2720/pe3/unicode3.dat', encoding='utf-8')
t3 = u3.readline()
print t3
u4 = codecs.open('/classes/ece2720/pe3/unicode4.dat', encoding='utf-16')
t4 = u4.readline()
print t4
u5 = codecs.open('/classes/ece2720/pe3/unicode5.dat', encoding='utf-8')
t5 = u5.readline()
print t5
def synthdata():
    synth = open('/classes/ece2720/pe3/synthetic.csv', 'rb')
    synthread = csv.reader(synth)
    for i in synthread:
        num = i
        num2 = []
        for x in num:
            num2.append(float(x))
    return num2
def synthhist():
    x = synthdata()
    plt.hist(x, bins = 100, density = True)
    mean = np.mean(x)
    std = np.std(x)
    x.sort()
    pdf = [scis.norm.pdf(value, mean, std) for value in x]
    plt.plot(x, pdf)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Synthetic.csv Values')
    plt.savefig('figure1')
    plt.clf()
def synthprobplt():
    x = synthdata()
    scis.probplot(x, plot = plt.subplot())
    plt.title('Normal Probability Plot of Synthetic.csv Values')
    plt.savefig('figure2')
    plt.clf()
def synthMLE():
    x = synthdata()
    synthavg = (sum(x)/float(len(x)))
    y = [(i-synthavg)**2.0 for i in x]
    synthvar = ((sum(y)/len(x)))
    stdeviation = math.sqrt(synthvar)
    z = [(i-synthavg)/stdeviation for i in x]
    Dmax = max(z)
    cc = (2*len(x))*(1-scis.norm.cdf(Dmax))
    print synthavg
    print synthvar
    print Dmax
    print cc
def titanicdata():
    titanic = open("/classes/ece2720/pe3/titanic.csv")
    titanicread = csv.reader(titanic)
    return titanicread
def agedata(y):
    titanic = open("/classes/ece2720/pe3/titanic.csv")
    titanicread = csv.reader(titanic)
    arr = []
    for row in titanicread:
        try:
            arr.append(int(row[y]))
        except:
            continue
    return arr
def faredata(y):
    titanic = open("/classes/ece2720/pe3/titanic.csv")
    titanicread = csv.reader(titanic)
    arr = []
    for row in titanicread:
        try:
            arr.append(float(row[y]))
        except:
            continue
    return arr
def agehist():
    x = agedata(5)
    plt.hist(x, bins=100, density=True)
    mean = np.mean(x)
    std = np.std(x)
    x.sort()
    pdf = [scis.norm.pdf(value, mean, std) for value in x]
    plt.plot(x, pdf)
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Age Histogram')
    plt.savefig('figure3')
    plt.clf()
def farehist():
    x = faredata(9)
    plt.hist(x, bins=100, density=True)
    mean = np.mean(x)
    std = np.std(x)
    x.sort()
    pdf = [scis.norm.pdf(value, mean, std) for value in x]
    plt.plot(x, pdf)
    plt.xlabel('Fare')
    plt.ylabel('Frequency')
    plt.title('Fare Histogram')
    plt.savefig('figure4')
    plt.clf()
def agenormplt():
    x = agedata(5)
    scis.probplot(x, plot=plt.subplot())
    plt.title('Normal Probability Plot of Age Values')
    plt.savefig('figure5')
    plt.clf()
def farenormplt():
    x = faredata(9)
    scis.probplot(x, plot=plt.subplot())
    plt.title('Normal Probability Plot of Fare Values')
    plt.savefig('figure6')
    plt.clf()
def ageMLE():
    x = agedata(5)
    ageavg = (sum(x)/float(len(x)))
    y = [(i - ageavg) ** 2.0 for i in x]
    agevar = (sum(y) / len(x))
    print ageavg
    print agevar
def fareMLE():
    x = faredata(9)
    fareavg = (sum(x)/float(len(x)))
    y = [(i - fareavg) ** 2.0 for i in x]
    farevar = (sum(y) / len(x))
    print fareavg
    print farevar
def survival_rate():
    x = titanicdata()
    dead = 0
    survived = 0
    for i in x:
        try:
            if int(i[1]) == 0:
                dead += 1
            elif int(i[1]) == 1:
                survived +=1
        except:
            continue
    total = float(survived) + float(dead)
    print(int(total), float(survived)/float(total))
def survival_rate_men_and_women():
    x = titanicdata()
    women = 0
    dwomen = 0
    alwomen = 0
    men = 0
    dmen = 0
    almen = 0
    for i in x:
        try:
            if(i[4] == 'female'):
                women += 1
                if int(i[1]) == 0:
                    dwomen += 1
                elif int(i[1]) == 1:
                    alwomen += 1
            elif(i[4] == 'male'):
                men += 1
                if int(i[1]) == 0:
                    dmen += 1
                elif int(i[1]) == 1:
                    almen += 1
        except:
            continue
    total_women = women
    total_men = men
    print(total_women, float(alwomen)/float(total_women))
    print(total_men, float(almen)/float(total_men))
def class_survival_rate(p_class):
    x = titanicdata()
    num_class = 0
    alclass = 0
    dclass = 0
    for i in x:
        try:
            if i[2] == p_class:
                num_class += 1
                if int(i[1]) == 0:
                    dclass += 1
                elif int(i[1]) == 1:
                    alclass += 1
        except:
            continue
    print(num_class, float(alclass) / float(num_class))
def class_sex_survival_rate(p_class, sex):
    x = titanicdata()
    group = 0
    alive = 0
    dead = 0
    for i in x:
        try:
            if i[2] == p_class:
                if i[4] == sex:
                    group+=1
                    if int(i[1]) == 0:
                        dead += 1
                    elif int(i[1]) == 1:
                        alive += 1
        except:
            continue
    print(group,  float(alive) / float(group))
def fare_survived_100(fare):
    x = titanicdata()
    group = 0
    alive = 0
    dead = 0
    for i in x:
        try:
            if float(i[9]) >= fare:
                group += 1
                if int(i[1]) == 0:
                    dead += 1
                elif int(i[1]) == 1:
                    alive += 1
        except:
            continue
    print(group, float(alive) / float(group))
def fare_survived_50 (fare):
    x = titanicdata()
    group = 0
    alive = 0
    dead = 0
    for i in x:
        try:
            if float(i[9]) <= fare:
                group += 1
                if int(i[1]) == 0:
                    dead += 1
                elif int(i[1]) == 1:
                    alive += 1
        except:
            continue
    print(group, float(alive) / float(group))
def family_survival():
    x = titanicdata()
    group = 0
    alive = 0
    dead = 0
    for i in x:
        try:
            if int(i[7]) != 0:
                group += 1
                if int(i[1]) == 0:
                    dead += 1
                elif int(i[1]) == 1:
                    alive += 1
        except:
            continue
    print(group, float(alive) / float(group))
synthhist()
synthprobplt()
synthMLE()
agehist()
farehist()
agenormplt()
farenormplt()
ageMLE()
fareMLE()
survival_rate()
survival_rate_men_and_women()
class_survival_rate('1')
class_survival_rate('3')
class_sex_survival_rate('1','male')
class_sex_survival_rate('3','female')
fare_survived_100(100)
fare_survived_50(50)
family_survival()