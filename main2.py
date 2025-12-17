from pyscript import display, document # type: ignore


def general_weighted_average(e): #Clears previous results
    document.getElementById('student_info').innerHTML = ' '
    document.getElementById('summary').innerHTML = ' '
    document.getElementById('output').innerHTML = ' '
    document.getElementById('stamp_pass').innerHTML = ' '
    document.getElementById('stamp_fail').innerHTML = ' '
    subjects = ['Science', 'Math', 'English', 'Filipino', 'ICT', 'PE', 'Art', 'Social Science']
    units_subject = (5, 3, 2, 1)

    first_name = document.getElementById('first_name').value
    last_name = document.getElementById('last_name').value

    #Gets the value from HTML and converts into float
    science = float(document.getElementById('science').value)
    math = float(document.getElementById('math').value)
    english = float(document.getElementById('english').value)
    filipino = float(document.getElementById('filipino').value)
    ict = float(document.getElementById('ict').value)
    pe = float(document.getElementById('pe').value)
    art = float(document.getElementById('art').value)
    SocSci = float(document.getElementById('SocSci').value)

    #Multiplies the subjects' grades by the hours they all take in a week (their importance), then adds them together. 
    weighted_sum = (science * units_subject[0] + 
        math * units_subject[0] + 
        english * units_subject[0] + 
        filipino * units_subject[1] + 
        ict * units_subject[2] + 
        pe * units_subject[3] +
        art * units_subject[3] +
        SocSci * units_subject[1])
    
    #Multiplies each units' hours (importance) by how many subjects take that much time (importance), then adds them all together
    total_units = (units_subject[0] * 3) + (units_subject[1] * 2) + units_subject[2] + (units_subject[3] * 2)

    #Calculates for the general weighted average by dividing the weighted sum by the total units
    gwa = weighted_sum / total_units
    
    #Removes all decimal places from the numbers
    summary = f"""
        {subjects[0]}: {science:.0f}
        {subjects[1]}: {math:.0f}
        {subjects[2]}: {english:.0f}
        {subjects[3]}: {filipino:.0f}
        {subjects[4]}: {ict:.0f}
        {subjects[5]}: {pe:.0f}
        {subjects[6]}: {art:.0f}
        {subjects[7]}: {SocSci:.0f}
            """

    #Displays the final report
    display(f'Name: {first_name} {last_name}', target="student_info")
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output', )

    #Checks whether average is failing/passing
    if gwa >= 75:
        display('✅ PASSED', target='stamp_pass')
    else:
        display('❌ FAILED', target='stamp_fail')