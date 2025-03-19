import csv
import numpy as np


#------------------------------------------------------------------------------------------------------------------------------------------------------#
#CODE HEAVILY INFLUENCED BY "Project 2 briefing video shared by Dr. Keogh" 
#Lecture slides given in lectures by Dr. Keogh. Main slide deck referred to is titled "8_MachineLearning003"
#OTHER LINKS USED TO RELEARNING THEORY IN FINAL REPORT
#------------------------------------------------------------------------------------------------------------------------------------------------------#

class Classifier:
    def __init__(self, file_name):
        self.file_name = file_name
        self.num_features = 0
        self.data_matrix = None
        self.num_instances = 0
        self.correct_classifications = 0
        self.accuracy = 0
        self.default_rate = None

    def train(self):
        with open(self.file_name, 'r') as f:
            reader = csv.reader(f, delimiter=' ', skipinitialspace=True)
            self.data_matrix = list(reader)
            self.num_instances = len(self.data_matrix)
            self.num_features = len(self.data_matrix[0]) - 1
        class_counts = {}
        for row in self.data_matrix:
            class_label = row[0]
            class_counts[class_label] = class_counts.get(class_label, 0) + 1

        self.default_rate = round(max(class_counts.values()) / self.num_instances * 100, 2)

    def reset(self):
        self.correct_classifications = 0
        self.accuracy = None


#------------------------------------------------------------------------------------------------------------------------------------------------------#
#https://www.geeksforgeeks.org/euclidean-distance/
#------------------------------------------------------------------------------------------------------------------------------------------------------#
    def euclidean_distance(self, test_row, compare_row):
        test_array = np.array(test_row, dtype=float)
        compare_array = np.array(compare_row, dtype=float)
        squared_differences = np.square(test_array - compare_array)
        sum_squared_differences = np.sum(squared_differences)
        distance = np.sqrt(sum_squared_differences)

        return distance
    


    def _get_nearest_neighbor(self, validated_list, index):
        nearest_neighbor_distance = float('inf')
        nearest_neighbor_label = None

        for j, row in enumerate(validated_list):
            if index != j:
                distance = self.euclidean_distance(validated_list[index], row)
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_label = int(float(self.data_matrix[j][0]))

        return nearest_neighbor_label
    
    def test(self, validated_list):
        self.correct_classifications = sum(
            1 for i in range(len(validated_list))
            if self._get_nearest_neighbor(validated_list, i) == int(float(self.data_matrix[i][0]))
        )
        self.accuracy = self.correct_classifications / self.num_instances
