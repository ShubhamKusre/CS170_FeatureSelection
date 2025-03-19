class FeatureSet:
    def __init__(self, subset):
        self.subset = subset
        self.accuracy = None

    def add_feature(self, feature):
        self.subset.add(feature)

    def remove_feature(self, feature):
        self.subset.remove(feature)

    def displayResults(self, accuracy : float):
        self.accuracy = round(accuracy * 100, 2)
        return (f'Using feature(s) {self.subset} is {self.accuracy}%')
    
    def best_subset_summary(self):
        return f"Best feature set: {self.subset}, Accuracy: {self.accuracy}%\n"
