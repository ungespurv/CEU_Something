import pandas as pd
import matplotlib.pyplot as plt

colnames = ['length_of_observing_arc_days', 'length_of_observing_arc_degree', 'semi_major_axis_upper_uncertainty',
            'eccentricity_upper_uncertainty', 'inclination_upper_uncertainty', 'argument_of_perihelion_upper_uncertainty',
            'longitude_of_ascending_node_upper_uncertainty', 'mean_anomaly_upper_uncertainty', 'semi_major_axis_lower_uncertainty',
            'eccentricity_lower_uncertainty', 'inclination_lower_uncertainty', 'argument_of_perihelion_lower_uncertainty',
            'longitude_of_ascending_node_lower_uncertainty', 'mean_anomaly_lower_uncertainty']

data = pd.read_csv('orbital_element.csv', names=colnames, header=None)

length_of_observing_arc_days = data['length_of_observing_arc_days'].tolist()
length_of_observing_arc_degree = data['length_of_observing_arc_degree'].tolist()

semi_major_axis1 = data['semi_major_axis_upper_uncertainty'].tolist()
semi_major_axis2 = data['semi_major_axis_lower_uncertainty'].tolist()
# semi_major_axis = [*semi_major_axis2, *semi_major_axis1]

eccentricity1 = data['eccentricity_upper_uncertainty'].tolist()
eccentricity2 = data['eccentricity_lower_uncertainty'].tolist()
# eccentricity = [*eccentricity2, *eccentricity1]

inclination1 = data['inclination_upper_uncertainty'].tolist()
inclination2 = data['inclination_lower_uncertainty'].tolist()
# inclination = [*inclination2, *inclination1]

argument_of_perihelion1 = data['argument_of_perihelion_upper_uncertainty'].tolist()
argument_of_perihelion2 = data['argument_of_perihelion_lower_uncertainty'].tolist()
# argument_of_perihelion = [*argument_of_perihelion2, *argument_of_perihelion1]

longitude_of_ascending_node1 = data['longitude_of_ascending_node_upper_uncertainty'].tolist()
longitude_of_ascending_node2 = data['longitude_of_ascending_node_lower_uncertainty'].tolist()
# longitude_of_ascending_node = [*longitude_of_ascending_node2, *longitude_of_ascending_node1]

mean_anomaly1 = data['mean_anomaly_upper_uncertainty'].tolist()
mean_anomaly2 = data['mean_anomaly_lower_uncertainty'].tolist()
# mean_anomaly = [*mean_anomaly2, *mean_anomaly1]

X1 = [[semi_major_axis1], [eccentricity1], [inclination1], [argument_of_perihelion1], [longitude_of_ascending_node1],
      [mean_anomaly1]]
X1_description = ['semi_major_axis_upper_uncertainty', 'eccentricity_upper_uncertainty',
                  'inclination_upper_uncertainty', 'argument_of_perihelion_upper_uncertainty',
            'longitude_of_ascending_node_upper_uncertainty', 'mean_anomaly_upper_uncertainty']
X2 = [[semi_major_axis2], [eccentricity2], [inclination2], [argument_of_perihelion2], [longitude_of_ascending_node2],
      [mean_anomaly2]]
X2_description = ['semi_major_axis_lower_uncertainty',
            'eccentricity_lower_uncertainty', 'inclination_lower_uncertainty', 'argument_of_perihelion_lower_uncertainty',
            'longitude_of_ascending_node_lower_uncertainty', 'mean_anomaly_lower_uncertainty']
Y_label = ['semi major axis uncertainty', 'eccentricity uncertainty',
                  'inclination_upper uncertainty', 'argument of perihelion uncertainty',
            'longitude of ascending node uncertainty', 'mean anomaly uncertainty']

for i in range(len(X1)):
    plt.figure()
    plt.scatter(x=length_of_observing_arc_days, y=X1[i], label=X1_description[i])
    plt.scatter(x=length_of_observing_arc_days, y=X2[i], label=X2_description[i])
    # plt.xscale('log')
    plt.yscale('log')
    plt.ylabel(Y_label[i])
    plt.xlabel('length of observing arc days')
    plt.legend()
    plt.show()