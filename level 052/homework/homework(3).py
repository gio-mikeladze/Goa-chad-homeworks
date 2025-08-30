#Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

#Numerical Score	Letter Grade
#90 <= score <= 100	'A'
#80 <= score < 90	'B'
#70 <= score < 80	'C'
#60 <= score < 70	'D'
#0 <= score < 60	'F'
def get_grade(s1, s2, s3):
    if 100>=(s1+s2+s3)/3>=90:
        return 	'A'
    elif 90>(s1+s2+s3)/3>=80:
        return 	'B'
    elif 80>(s1+s2+s3)/3>=70:
        return 'C'
    elif 70>(s1+s2+s3)/3>=60:
        return 'D'
    return 'F'