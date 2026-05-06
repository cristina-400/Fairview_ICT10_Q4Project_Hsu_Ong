from pyscript import document
from js import localStorage
import json

# =========================
# CLASSMATE SYSTEM
# =========================

class Classmate:
    def __init__(self, name, section, subject):
        self.name = name
        self.section = section
        self.subject = subject

    def to_dict(self):
        return {
            "name": self.name,
            "section": self.section,
            "subject": self.subject
        }

# ADD CLASSMATE
def create_info(event=None):

    name = document.getElementById("name").value.strip()
    section = document.getElementById("section").value.strip()
    subject = document.getElementById("subject").value.strip()

    output = document.getElementById("output2")

    if not name or not section or not subject:
        output.innerHTML = "⚠️ Please complete all fields!"
        return

    person = Classmate(name, section, subject)

    classmates_json = localStorage.getItem("classmates")

    classmates = json.loads(classmates_json) if classmates_json else []

    classmates.append(person.to_dict())

    localStorage.setItem(
        "classmates",
        json.dumps(classmates)
    )

    output.innerHTML = "✅ Info Added Successfully!"

# VIEW CLASSMATES
def check_classmate(event=None):

    classmates_json = localStorage.getItem("classmates")

    output = document.getElementById("output3")

    if classmates_json:

        classmates = json.loads(classmates_json)

        output_text = "<h3>Classmates:</h3><ul>"

        for p in classmates:

            output_text += f"""
            <li>
            Hi, I'm <b>{p['name']}</b> from
            <b>{p['section']}</b> and my favorite
            subject is <b>{p['subject']}</b>.
            </li>
            """

        output_text += "</ul>"

    else:
        output_text = "<p>No classmates added yet.</p>"

    output.innerHTML = output_text

# =========================
# ATTENDANCE TRACKER
# =========================

days = []
absences = []

def sample_numpy(event=None):

    day = document.getElementById("dayofweek").value
    absence = document.getElementById("absences").value

    output = document.getElementById("output")

    if absence == "":
        output.innerHTML = "⚠️ Enter absences first."
        return

    absences.append(int(absence))
    days.append(day)

    # CREATE SIMPLE HTML GRAPH
    graph_html = "<h3>Attendance Graph</h3>"

    for i in range(len(days)):

        width = absences[i] * 40

        graph_html += f"""
        <p><b>{days[i]}</b> - {absences[i]} absences</p>

        <div style="
            background:#2d6cdf;
            height:30px;
            width:{width}px;
            border-radius:8px;
            margin-bottom:15px;
        "></div>
        """

    output.innerHTML = graph_html
