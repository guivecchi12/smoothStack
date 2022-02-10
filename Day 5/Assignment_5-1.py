# Day 5

def body_mass_index(input_data):
    num_people = input_data[0]
    people = input_data[1:]

    bmi = lambda data: data[0] / (data[1] ** 2)

    weights = map(bmi, people)
    weight_class = []

    for w in weights:
        if w < 18.5:
            weight_class.append('under')
        elif 18.5 <= w <= 25.0:
            weight_class.append('normal')
        elif 25.0 <= w <= 30.0:
            weight_class.append('over')
        else:
            weight_class.append('obese')
    
    print(*weight_class)

data = [3, (80, 1.73), (55, 1.58), (49, 1.91)]
body_mass_index(data)