from pyscript import display, document


def general_weighted_average(e):
    document.getElementById('student_info').innerHTML = ' '
    document.getElementById('summary').innerHTML = ' '
    document.getElementById('output').innerHTML = ' '
    subjects = ['Science', 'Math', 'English', 'Filipino', 'ICT', 'PE']
    units_subject = (5, 3, 2, 1)

    first_name = document.getElementById('first_name').value
    last_name = document.getElementById('last_name').value

    science = float(document.getElementById('science').value)
    math = float(document.getElementById('math').value)
    english = float(document.getElementById('english').value)
    filipino = float(document.getElementById('filipino').value)
    ict = float(document.getElementById('ict').value)
    pe = float(document.getElementById('pe').value)

    weighted_sum = (science * units_subject[0] + 
           math * units_subject[0] + 
           english * units_subject[0] + 
           filipino * units_subject[1] + 
           ict * units_subject[2] + 
           pe * units_subject[3]) 
    total_units = (units_subject[0] * 3) + units_subject[1] + units_subject[2] + units_subject[3]
    gwa = weighted_sum / total_units
    
    summary = f"""{subjects[0]}: {science:.0f}
{subjects[1]}: {math:.0f}
{subjects[2]}: {english:.0f}
{subjects[3]}: {filipino:.0f}
{subjects[4]}: {ict:.0f}
{subjects[5]}: {pe:.0f}
    """
    display(f'Name: {first_name} {last_name}', target="student_info")
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output', )