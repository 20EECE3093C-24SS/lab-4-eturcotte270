# TODO-1: add convert_to_letter_grade(score) function
def convert_to_letter_grade(score):
    """
    This function takes a score as input and returns the corresponding letter grade.
    
    Parameters:
    score (int/float): the students score.
    
    Raises:
    TypeError: If score is not a numeric type (int or float).
    ValueError: If score is not between 0 and 100.
    
    Returns:
    string: the corresponding upper case letter grade.
    """
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a numeric value.")
    
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
