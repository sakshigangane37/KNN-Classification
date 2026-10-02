import math

# ------------------------------------------------------------
# Display Border
# ------------------------------------------------------------

def Border():
    print("-" * 70)

# ------------------------------------------------------------
# Calculate Euclidean Distance
# ------------------------------------------------------------

def CalculateDistance(X1, Y1, X2, Y2):
    Distance = math.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2)
    return Distance

# ------------------------------------------------------------
# Calculate Distances
# ------------------------------------------------------------

def CalculateDistances(Data, NewX, NewY):
    Distances = []

    for Point in Data:
        Distance = CalculateDistance(
            NewX,
            NewY,
            Point["X"],
            Point["Y"]
        )

        Distances.append({
            "Point": Point["Point"],
            "Distance": Distance,
            "Label": Point["Label"]
        })

    return Distances

# ------------------------------------------------------------
# Sort Distances
# ------------------------------------------------------------

def SortDistances(Distances):
    Distances.sort(key=lambda Item: Item["Distance"])
    return Distances

# ------------------------------------------------------------
# Select Nearest Neighbors
# ------------------------------------------------------------

def SelectNeighbors(Distances, K):
    if K > len(Distances):
        K = len(Distances)

    Neighbors = Distances[:K]
    return Neighbors

# ------------------------------------------------------------
# Predict Class Using Majority Voting
# ------------------------------------------------------------

def PredictClass(Neighbors):
    Counts = {}

    for Neighbor in Neighbors:
        Label = Neighbor["Label"]

        if Label not in Counts:
            Counts[Label] = 0

        Counts[Label] = Counts[Label] + 1

    MaximumCount = max(Counts.values())
    Winners = []

    for Label in Counts:
        if Counts[Label] == MaximumCount:
            Winners.append(Label)

    if len(Winners) == 1:
        return Winners[0]

    for Neighbor in Neighbors:
        if Neighbor["Label"] in Winners:
            return Neighbor["Label"]

# ------------------------------------------------------------
# Display Nearest Neighbors
# ------------------------------------------------------------

def DisplayNeighbors(Neighbors):
    print("Nearest Neighbors:")

    for Neighbor in Neighbors:
        print(Neighbor["Point"], "- Distance:", round(Neighbor["Distance"], 2), "-", Neighbor["Label"])

# ------------------------------------------------------------
# Perform KNN Classification
# ------------------------------------------------------------

def PerformKNN(Data, NewX, NewY, K):
    Distances = CalculateDistances(
        Data,
        NewX,
        NewY
    )

    SortedDistances = SortDistances(Distances)

    Neighbors = SelectNeighbors(
        SortedDistances,
        K
    )

    Prediction = PredictClass(Neighbors)

    return SortedDistances, Neighbors, Prediction

# ------------------------------------------------------------
# Display First Classification
# ------------------------------------------------------------

def ClassifyNewPoint(Data):
    Border()
    print("K-Nearest Neighbors Classification")
    Border()

    NewX = float(input("Enter X coordinate: "))
    NewY = float(input("Enter Y coordinate: "))

    SortedDistances, Neighbors, Prediction = PerformKNN(
        Data,
        NewX,
        NewY,
        3
    )

    DisplayNeighbors(Neighbors)
    print("Predicted Class:", Prediction)

# ------------------------------------------------------------
# Compare Different K Values
# ------------------------------------------------------------

def CompareKValues(Data, NewX, NewY):
    Border()
    print("Prediction Results for Different K Values")
    Border()

    KValues = [1, 3, 5]

    for K in KValues:
        Distances, Neighbors, Prediction = PerformKNN(
            Data,
            NewX,
            NewY,
            K
        )

        ActualK = min(K, len(Data))

        print("K =", K, "Used Neighbors =", ActualK, "Predicted Class:", Prediction)

    print("Prediction can change when K increases because more neighboring points participate in the majority voting process.")

# ------------------------------------------------------------
# Student KNN Classification
# ------------------------------------------------------------

def PredictStudentResult():
    Border()
    print("Student Pass or Fail Prediction")
    Border()

    Data = [
        {"StudyHours": 2, "Attendance": 60, "Result": "Fail"},
        {"StudyHours": 5, "Attendance": 80, "Result": "Pass"},
        {"StudyHours": 6, "Attendance": 85, "Result": "Pass"},
        {"StudyHours": 1, "Attendance": 50, "Result": "Fail"}
    ]

    StudyHours = float(input("Enter Study Hours: "))
    Attendance = float(input("Enter Attendance: "))

    Distances = []

    for Student in Data:
        Distance = CalculateDistance(
            StudyHours,
            Attendance,
            Student["StudyHours"],
            Student["Attendance"]
        )

        Distances.append({
            "Distance": Distance,
            "Result": Student["Result"]
        })

    Distances.sort(key=lambda Item: Item["Distance"])

    K = 3
    Neighbors = Distances[:K]

    Counts = {}

    for Neighbor in Neighbors:
        Result = Neighbor["Result"]

        if Result not in Counts:
            Counts[Result] = 0

        Counts[Result] = Counts[Result] + 1

    Prediction = max(
        Counts,
        key=Counts.get
    )

    print("Predicted Result:", Prediction)

# ------------------------------------------------------------
# Main Function
# ------------------------------------------------------------

def main():
    Data = [
        {"Point": "A", "X": 1, "Y": 2, "Label": "Red"},
        {"Point": "B", "X": 2, "Y": 3, "Label": "Red"},
        {"Point": "C", "X": 3, "Y": 1, "Label": "Blue"},
        {"Point": "D", "X": 6, "Y": 5, "Label": "Blue"}
    ]

    ClassifyNewPoint(Data)

    NewX = 2
    NewY = 2

    CompareKValues(
        Data,
        NewX,
        NewY
    )

    PredictStudentResult()

    Border()
    print("Assignment 42 Completed Successfully")
    Border()

if __name__ == "__main__":
    main()