from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Debugging: Print the received form data
        print("Received Form Data:", request.form)

        # Extract user inputs
        name = request.form.get("name")
        cgpa = request.form.get("cgpa")
        comm_skills = request.form.get("comm_skills")
        discipline = request.form.get("discipline")
        hostel = request.form.get("hostel")
        internships = request.form.get("internships")
        certifications = request.form.get("certifications")
        projects = request.form.get("projects")

        # Validate if any field is missing
        if not all([name, cgpa, comm_skills, discipline, hostel, internships, certifications, projects]):
            return render_template("result.html", probability="Error")

        # Convert input values to proper data types
        cgpa = float(cgpa)
        comm_skills = int(comm_skills)
        internships = int(internships)
        certifications = int(certifications)
        projects = int(projects)

        # Mock prediction logic (Replace this with actual model prediction)
        probability = round((cgpa * 10 + comm_skills * 5 + internships * 2 + certifications * 3 + projects * 4) / 2, 2)

        # Determine strengths and weaknesses
        strengths = []
        weaknesses = []

        if cgpa > 8.0:
            strengths.append("Strong academic performance")
        else:
            weaknesses.append("Improve your CGPA")

        if comm_skills > 7:
            strengths.append("Good communication skills")
        else:
            weaknesses.append("Work on your communication skills")

        if internships > 1:
            strengths.append("Internship experience is a plus")
        else:
            weaknesses.append("Gain more internship experience")

        return render_template("result.html", probability=probability, strengths=strengths, weaknesses=weaknesses)

    except Exception as e:
        print("Error:", e)
        return render_template("result.html", probability="Error")

if __name__ == '__main__':
    app.run(debug=True)



