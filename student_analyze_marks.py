
def analyze_marks(marks):
    if len(marks) == 0:
        return "No marks found"
    max_mark = max(marks)
    min_mark = min(marks)
    avg_mark = sum(marks) / len(marks)
    print(f"Maximum Mark: {max_mark}")
    print(f"Minimum Mark: {min_mark}")
    print(f"Average Mark: {avg_mark:.2f}")

marks = list(map(int, input("Enter Marks Separated by spaces: ").split()))
analyze_marks(marks)