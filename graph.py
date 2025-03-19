
#------------------------------------------------------------------------------------------------------------------------------------------------------#
#FIGURE 1 GRAPH
#------------------------------------------------------------------------------------------------------------------------------------------------------#

# import matplotlib.pyplot as plt


# custom_labels = ["{}", "{6}", "{1,6}", "{1,4,6}", "{1,4,5,6}", "{1,2,4,5,6}","{All Features}"]
# accuracy_values_updated = [83.2, 86.2, 95.4, 93.4, 90.4, 85.2, 84.4] 


# plt.figure(figsize=(10, 4))
# plt.bar(custom_labels, [val if val is not None else 0 for val in accuracy_values_updated], color='#6495ED')


# plt.xticks(range(len(custom_labels)), custom_labels, rotation=0)


# plt.xlabel("Current Feature Set: Forward Selection", fontsize=12)
# plt.ylabel("Accuracy", fontsize=12)


# plt.ylim(0, 100)


# plt.show()




#------------------------------------------------------------------------------------------------------------------------------------------------------#
#FIGURE 2 GRAPH
#------------------------------------------------------------------------------------------------------------------------------------------------------#

# import matplotlib.pyplot as plt


# custom_labels = ["{All Features}", "{1, 2, 3, 4, 6}", "{1, 3, 4, 6}", "{1,4,6}", "{1,6}", "{6}", "{}"]
# accuracy_values_updated = [84.4, 85.6, 88.6, 93.4, 95.4, 86.2, 83.2] 


# plt.figure(figsize=(10, 4))
# plt.bar(custom_labels, [val if val is not None else 0 for val in accuracy_values_updated], color='#6495ED')


# plt.xticks(range(len(custom_labels)), custom_labels, rotation=0)


# plt.xlabel("Current Feature Set: Backward Elimination", fontsize=12)
# plt.ylabel("Accuracy", fontsize=12)


# plt.ylim(0, 100)

# plt.show()




#------------------------------------------------------------------------------------------------------------------------------------------------------#
#FIGURE 3 GRAPH
#------------------------------------------------------------------------------------------------------------------------------------------------------#

# import matplotlib.pyplot as plt


# feature_sets = ["{}", "{24}", "{24,27}", "{24,10,27}", "{yp}", "Dummy 1", "Dummy 2", "all - 2", "all -1", "{All Features}"]
# accuracy_values = [81.7, 84.1, 96.4, 94.8, None, 0, 0, 69.4, 68.7, 66.6]

# plt.figure(figsize=(12, 4))
# plt.bar(feature_sets, [val if val is not None else 0 for val in accuracy_values], color='#6495ED')

# plt.xticks(rotation=0, ha='center', fontsize=10)

# plt.xlabel("Current Feature Set: Forward Selection", fontsize=12)
# plt.ylabel("Accuracy", fontsize=12)


# plt.ylim(0, 100)


# plt.tight_layout()
# plt.show()





#------------------------------------------------------------------------------------------------------------------------------------------------------#
#FIGURE 4 GRAPH
#------------------------------------------------------------------------------------------------------------------------------------------------------#

# import matplotlib.pyplot as plt


# feature_sets = ['{All Features}', 'all -1', 'all - 2', 'Dummy 2', 'Dummy 1', '{yp}', '{8, 26, 5}', '{8,5}', '{8}', '{}']
# accuracy_values = [66.6, 68.8, 69.8, 0, 0, None, 73.6, 71.3, 69.8, 81.7]

# plt.figure(figsize=(12, 4))
# plt.bar(feature_sets, [val if val is not None else 0 for val in accuracy_values], color='#6495ED')

# plt.xticks(rotation=0, ha='center', fontsize=10)

# plt.xlabel("Current Feature Set: Backward Elimination", fontsize=12)
# plt.ylabel("Accuracy", fontsize=12)


# plt.ylim(0, 100)


# plt.tight_layout()
# plt.show()