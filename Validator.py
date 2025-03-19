from Classifier import Classifier
from FeatureSet import FeatureSet

class Validator:
    def __init__(self, subset: FeatureSet, classifier: Classifier):
        self.subset = subset
        self.classifier = classifier
        self.accuracy = None

    def get_accuracy(self):
        return self.accuracy

    def validate(self):
        validated_list = [
            [self.classifier.data_matrix[row][feature] for feature in self.subset.subset]
            for row in range(len(self.classifier.data_matrix))
        ]

        self.classifier.test(validated_list)
        self.accuracy = self.classifier.accuracy