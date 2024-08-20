from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
#iuyghy
@app.route('/calculate', methods=['POST'])
def calculate():
    total_credits = 0
    total_grade_points = 0

    for i in range(1, 7):
        subject = request.form.get(f'subject{i}')
        grade = request.form.get(f'grade{i}')

        if subject and grade:
            credits = 4  # Assuming each subject has 4 credits
            grade_points = get_grade_points(grade)
            total_credits += credits
            total_grade_points += credits * grade_points

    if total_credits > 0:
        cgpa = total_grade_points / total_credits
        return render_template('result.html', cgpa=cgpa)

    return render_template('result.html', cgpa=None)

def get_grade_points(grade):
    grade_points_dict = {'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 'B': 6}
    return grade_points_dict.get(grade, 0)

if __name__ == '__main__':
    app.run(debug=True,port=8001)
