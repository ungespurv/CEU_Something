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
X = [data1['semi_major_axis'], data1['eccentricity'], data1['inclination'], data1['argument_of_perihelion']
    , data1['longitude_of_ascending_node'], data1['mean_anomaly']]
X1 = [data['semi_major_axis_upper_uncertainty'], data['eccentricity_upper_uncertainty'],
           data['inclination_upper_uncertainty'], data['argument_of_perihelion_upper_uncertainty'],
           data['longitude_of_ascending_node_upper_uncertainty'], data['mean_anomaly_upper_uncertainty']]
X2 = [data['semi_major_axis_lower_uncertainty'], data['eccentricity_lower_uncertainty'],
           data['inclination_lower_uncertainty'], data['argument_of_perihelion_lower_uncertainty'],
           data['longitude_of_ascending_node_lower_uncertainty'], data['mean_anomaly_lower_uncertainty']]
# F_3Ghz = []
# for i in range(len(df['T'])):
#     F_3Ghz.append(df['FluxD'][i] * (3e9/df['Freq'][i])**(c[1]))
# df['F_3Ghz'] = F_3Ghz
WYNIKI1 = []
WYNIKI2 = []

for i, x1 in enumerate(X1):
    WYNIKI1.append(x1/X[i])
    #FIXME

print(WYNIKI1)
# for i, slc in enumerate(slicers):
#     if i == 12:
#         ax1.errorbar(x=slc['T'], y=slc['FluxD'], yerr=slc['FluxDErr'],  marker=shapes[i], mec=colours[i], fmt='o',
#                      markeredgewidth=0.0, label=str('7895 Å'))


# for i in range(len(X1)):
#     fig, ax = plt.subplots(2, 1)
#     ax[0].scatter(length_of_observing_arc_days, WYNIKI1[i], s=0.5, c='red')
#     ax[1].scatter(length_of_observing_arc_days, WYNIKI2[i], s=0.5, c='green')
#     maxX1 = max(X1[i])
#     minX1 = min(X1[i])
#     maxX2 = max(X2[i])
#     minX2 = min(X2[i])
#     maxY = max(length_of_observing_arc_days)
#     minY = min(length_of_observing_arc_days)
#     ax[0].set_xscale('log')
#     ax[0].set_yscale('log')
#     ax[1].set_xscale('log')
#     ax[1].set_yscale('log')
#     # ax[0].set_xlim(minY, maxY)
#     # ax[0].set_ylim(minX1, maxX1)
#     # ax[1].set_xlim(minY, maxY)
#     # ax[1].set_ylim(minX2, minX2)
#     ax[0].set_xlim(1e-5, 10000)
#     ax[0].set_ylim(1e-7, 10000)
#     ax[1].set_xlim(1e-5, 10000)
#     ax[1].set_ylim(1e-7, 10000)
#     ax[0].set_ylabel(Y_label[i])
#     # ax[1].set_ylabel(Y_label[i])
#     ax[1].set_xlabel('length of observing arc days')
#     ax[1].invert_yaxis()
#     ax[1].legend()
#     ax[0].legend()
#     # fig.tight_layout()
#     plt.show()
