from FeatureSearches import FeatureSearches

def main(): 
    print("Welcome to Shubham's Feature Selection Algorithm.")

    dataset_choice = input("Select the dataset to use:\n" +
                           "\t1 - Small Dataset\n" +
                           "\t2 - Large Dataset\n")

    while dataset_choice not in {'1', '2'}:
        print("Invalid choice! Please enter 1 or 2.")
        dataset_choice = input("Select the dataset to use:\n" +
                               "\t1 - Small Dataset (CS170_Small_Data__50.txt)\n" +
                               "\t2 - Large Dataset (CS170_Large_Data__15.txt)\n")

    fileName = "CS170_Small_Data__50.txt" if dataset_choice == '1' else "CS170_Large_Data__15.txt"
    print(f"Using dataset: {fileName}")  

    algorithm = input("Type the number of the algorithm you want to run:\n" +
                      "\t1 - Forward Selection\n" +
                      "\t2 - Backward Elimination\n")

    while algorithm not in {'1', '2'}:
        print("Please enter a valid choice (1 or 2).")
        algorithm = input("Type the number of the algorithm you want to run:\n" +
                          "\t1 - Forward Selection\n" +
                          "\t2 - Backward Selection\n")

    algs = FeatureSearches(fileName, int(algorithm))
    algs.start()

if __name__ == "__main__":
    main()
