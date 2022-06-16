from matplotlib import pyplot as plt
from GradientByHand import renew_lrbyhand
from GradientDescentUpdateModel import renew_gradientdescent
from MultiScikit import renew_multivariate


def plot():
    ypoints = []
    for i in range(50):
        ypoints.append(i)
    byhandpoints = []
    gradient, bias = renew_lrbyhand()
    for i in range(0, 50):
        byhandpoints.append((i * gradient + bias))
    gradient, bias = renew_gradientdescent()
    gdpoints = []
    for i in range(0, 50):
        gdpoints.append((i * gradient + bias))
    plt.figure()
    By_Hand = plt.plot(ypoints, byhandpoints, label='By Hand')
    gd_line = plt.plot(ypoints, gdpoints, label='Gradient Descent')
    plt.legend()
    plt.title('Plots')
    plt.xlabel('Wind Speed/ KmpH')
    plt.ylabel('Predicted Swell Height/ m')
    fig = plt.gcf()
    fig.savefig('Images\plot.png')


plot()
