import copy
import time
from FeatureSet import FeatureSet
from Classifier import Classifier
from Validator import Validator


#------------------------------------------------------------------------------------------------------------------------------------------------------#
#CODE HEAVILY INFLUENCED BY "Project 2 briefing video shared by Dr. Keogh" 
#Lecture slides given in lectures by Dr. Keogh. Main slide deck referred to is titled "8_MachineLearning003"
#OTHER LINKS USED TO RELEARNING THEORY IN FINAL REPORT
#------------------------------------------------------------------------------------------------------------------------------------------------------#

class FeatureSearches:
    def __init__(self, fileName: int, algorithm_choice: int):
        self.fileName = fileName
        self.total_features = 0
        self.algorithm_choice = algorithm_choice
        self.best_so_far_accuracy = None
        self.current_set_of_features = set()
        self.selected_feature_subsets = {}
        self.last_selected_feature = -1
        self.classifier = None
        self.validator = None

    def forwardSelection(self):
        start_time = time.time()
        print(f"Starting Forward Selection...\nDefault rate accuracy: {self.classifier.default_rate}%")

        for level in range(self.total_features):
            best_so_far_accuracy = -1
            best_feature = None
            feature_to_add_at_this_level = None


            for feature in range(1, self.total_features + 1):
                if feature not in self.current_set_of_features:
                    temp_node = FeatureSet(copy.deepcopy(self.current_set_of_features))
                    temp_node.add_feature(feature)
                    accuracy = self.evaluate(temp_node)
                    
                    print(temp_node.displayResults(accuracy))

                    if accuracy > best_so_far_accuracy:
                        best_so_far_accuracy = accuracy
                        best_feature = temp_node
                        feature_to_add_at_this_level = feature

            if best_feature:
                print(best_feature.best_subset_summary())
                self.current_set_of_features.add(feature_to_add_at_this_level)
                self.selected_feature_subsets[best_feature.accuracy] = best_feature.subset

        temp_node = FeatureSet(set())
        accuracy = self.evaluate(temp_node)
        print(temp_node.displayResults(accuracy))

        self.selected_feature_subsets[accuracy] = temp_node.subset
        end_time = time.time()
        total_time = end_time - start_time

        best_accuracy = max(self.selected_feature_subsets.keys())
        best_subset = self.selected_feature_subsets[best_accuracy]

        print("\nSearch Completed!")
        print(f"Best feature subset found: {best_subset} with accuracy of {best_accuracy}%.")
        print(f"Total execution time: {total_time:.2f} seconds.")


    def backwardElimination(self):
        start_time = time.time()
        print("Starting Backward Elimination...")

        for feature in range(1, self.total_features + 1):
            self.current_set_of_features.add(feature)

        temp_node = FeatureSet(copy.deepcopy(self.current_set_of_features))
        accuracy = self.evaluate(temp_node)

        print(temp_node.displayResults(accuracy))
        print(temp_node.best_subset_summary())

        self.selected_feature_subsets[temp_node.accuracy] = temp_node.subset

        while self.current_set_of_features:  
            best_so_far_accuracy = -1
            best_feature = None
            feature_to_remove_at_this_level = None

            for feature in list(self.current_set_of_features):
                temp_node = FeatureSet(copy.deepcopy(self.current_set_of_features))
                temp_node.remove_feature(feature)
                accuracy = self.evaluate(temp_node)

                print(temp_node.displayResults(accuracy))

                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    best_feature = temp_node
                    feature_to_remove_at_this_level = feature

            if best_feature:
                print(best_feature.best_subset_summary())
                self.current_set_of_features.remove(feature_to_remove_at_this_level)
                self.selected_feature_subsets[best_feature.accuracy] = best_feature.subset

        end_time = time.time()
        total_time = end_time - start_time

        best_accuracy = max(self.selected_feature_subsets.keys())
        best_subset = self.selected_feature_subsets[best_accuracy]

        print("\nSearch Completed!")
        print(f"Best feature subset found: {best_subset} with accuracy of {best_accuracy}%.")
        print(f"Total execution time: {total_time:.2f} seconds.")

    def evaluate(self, node: FeatureSet):
        self.validator = Validator(node, self.classifier)
        self.validator.validate()
        accuracy = self.validator.get_accuracy()
        self.classifier.reset()
        return accuracy
    
    def start(self):
        print("Beginning Search.\n")
        self.classifier = Classifier(self.fileName)
        self.classifier.train()

        self.total_features = self.classifier.num_features

        if self.algorithm_choice == 1:
            self.forwardSelection()
        elif self.algorithm_choice == 2:
            self.backwardElimination()
        return
