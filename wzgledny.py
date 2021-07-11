import pandas as pd
import matplotlib.pyplot as plt

colnames1 = ['length_of_observing_arc_days', 'length_of_observing_arc_degree', 'semi_major_axis_upper_uncertainty',
            'eccentricity_upper_uncertainty', 'inclination_upper_uncertainty', 'argument_of_perihelion_upper_uncertainty',
            'longitude_of_ascending_node_upper_uncertainty', 'mean_anomaly_upper_uncertainty', 'semi_major_axis_lower_uncertainty',
            'eccentricity_lower_uncertainty', 'inclination_lower_uncertainty', 'argument_of_perihelion_lower_uncertainty',
            'longitude_of_ascending_node_lower_uncertainty', 'mean_anomaly_lower_uncertainty']
colnames = ['semi_major_axis','eccentricity', 'inclination', 'argument_of_perihelion',
            'longitude_of_ascending_node','mean_anomaly']

data = pd.read_csv('orbital_element.csv', names=colnames1, header=None)
data1 = pd.read_csv('orbital_element6.csv', names=colnames, header=None)

length_of_observing_arc_days = data['length_of_observing_arc_days'].tolist()
length_of_observing_arc_degree = data['length_of_observing_arc_degree'].tolist()

semi_major_axis1 = data['semi_major_axis_upper_uncertainty'].tolist()
semi_major_axis2 = data['semi_major_axis_lower_uncertainty'].tolist()
semi_major_axis = data1['semi_major_axis'].tolist()

eccentricity1 = data['eccentricity_upper_uncertainty'].tolist()
eccentricity2 = data['eccentricity_lower_uncertainty'].tolist()
eccentricity = data1['eccentricity'].tolist()

inclination1 = data['inclination_upper_uncertainty'].tolist()
inclination2 = data['inclination_lower_uncertainty'].tolist()
inclination = data1['inclination'].tolist()

argument_of_perihelion1 = data['argument_of_perihelion_upper_uncertainty'].tolist()
argument_of_perihelion2 = data['argument_of_perihelion_lower_uncertainty'].tolist()
argument_of_perihelion = data1['argument_of_perihelion'].tolist()

longitude_of_ascending_node1 = data['longitude_of_ascending_node_upper_uncertainty'].tolist()
longitude_of_ascending_node2 = data['longitude_of_ascending_node_lower_uncertainty'].tolist()
longitude_of_ascending_node = data1['longitude_of_ascending_node'].tolist()

mean_anomaly1 = data['mean_anomaly_upper_uncertainty'].tolist()
mean_anomaly2 = data['mean_anomaly_lower_uncertainty'].tolist()
mean_anomaly = data1['mean_anomaly'].tolist()

print(mean_anomaly)

X1_description = ['semi_major_axis_upper_uncertainty', 'eccentricity_upper_uncertainty',
                  'inclination_upper_uncertainty', 'argument_of_perihelion_upper_uncertainty',
            'longitude_of_ascending_node_upper_uncertainty', 'mean_anomaly_upper_uncertainty']
X2_description = ['semi_major_axis_lower_uncertainty',
            'eccentricity_lower_uncertainty', 'inclination_lower_uncertainty',
                  'argument_of_perihelion_lower_uncertainty',
            'longitude_of_ascending_node_lower_uncertainty', 'mean_anomaly_lower_uncertainty']
Y_label = ['semi major axis uncertainty', 'eccentricity uncertainty',
                  'inclination_upper uncertainty', 'argument of perihelion uncertainty',
            'longitude of ascending node uncertainty', 'mean anomaly uncertainty']
X = [semi_major_axis, eccentricity, inclination, argument_of_perihelion, longitude_of_ascending_node, mean_anomaly]
X1 = [semi_major_axis1, eccentricity1, inclination1, argument_of_perihelion1, longitude_of_ascending_node1,
      mean_anomaly1]
X2 = [semi_major_axis2, eccentricity2, inclination2, argument_of_perihelion2, longitude_of_ascending_node2,
      mean_anomaly2]

print(mean_anomaly1)
wyniki1 = []
wyniki2 = []
wyniki3 = []
wyniki4 = []
wyniki5 = []
wyniki6 = []
wyniki7 = []
wyniki8 = []
wyniki9 = []
wyniki10 = []
wyniki11 = []
wyniki12 = []
WYNIKI1 = []
WYNIKI2 =[]

for i in range(len(semi_major_axis)):
    wyniki1.append(semi_major_axis1[i]/semi_major_axis[i])
    wyniki2.append(eccentricity1[i]/eccentricity[i])
    wyniki3.append(inclination1[i]/inclination[i])
    wyniki4.append(argument_of_perihelion1[i]/argument_of_perihelion[i])
    wyniki5.append(longitude_of_ascending_node1[i]/ longitude_of_ascending_node[i])
    wyniki6.append(mean_anomaly1[i]/mean_anomaly[i])
    wyniki7.append(semi_major_axis2[i] / semi_major_axis[i])
    wyniki8.append(eccentricity2[i] / eccentricity[i])
    wyniki9.append(inclination2[i] / inclination[i])
    wyniki10.append(argument_of_perihelion2[i] / argument_of_perihelion[i])
    wyniki11.append(longitude_of_ascending_node2[i] / longitude_of_ascending_node[i])
    wyniki12.append(mean_anomaly2[i] / mean_anomaly[i])

WYNIKI1.append(wyniki1)
WYNIKI1.append(wyniki2)
WYNIKI1.append(wyniki3)
WYNIKI1.append(wyniki4)
WYNIKI1.append(wyniki5)
WYNIKI1.append(wyniki6)
WYNIKI2.append(wyniki7)
WYNIKI2.append(wyniki8)
WYNIKI2.append(wyniki9)
WYNIKI2.append(wyniki10)
WYNIKI2.append(wyniki11)
WYNIKI2.append(wyniki12)





for i in range(len(X1)):
    fig, ax = plt.subplots(2, 1)
    ax[0].scatter(x=length_of_observing_arc_days, y=WYNIKI1[i], s=0.5, c='red')
    ax[1].scatter(x=length_of_observing_arc_days, y=WYNIKI2[i], s=0.5, c='green')
    maxX1 = max(X1[i])
    minX1 = min(X1[i])
    maxX2 = max(X2[i])
    minX2 = min(X2[i])
    maxY = max(length_of_observing_arc_days)
    minY = min(length_of_observing_arc_days)
    ax[0].set_xscale('log')
    ax[0].set_yscale('log')
    ax[1].set_xscale('log')
    ax[1].set_yscale('log')
    # ax[0].set_xlim(minY, maxY)
    # ax[0].set_ylim(minX1, maxX1)
    # ax[1].set_xlim(minY, maxY)
    # ax[1].set_ylim(minX2, minX2)
    ax[0].set_xlim(1e-5, 10000)
    ax[0].set_ylim(1e-7, 10000)
    ax[1].set_xlim(1e-5, 10000)
    ax[1].set_ylim(1e-7, 10000)
    ax[0].set_ylabel(Y_label[i])
    # ax[1].set_ylabel(Y_label[i])
    ax[1].set_xlabel('length of observing arc days')
    ax[1].invert_yaxis()
    ax[1].legend()
    ax[0].legend()
    # fig.tight_layout()
    plt.show()
