from pyscript import document, display
from js import localStorage
import json

# GRAPH IMPORTS
import numpy as np
import matplotlib.pyplot as plt

# ================= CLASSMATE SYSTEM =================

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

    name = document.getElementById('name').value.strip()
    section = document.getElementById('section').value.strip()
    subject = document.getElementById('subject').value.strip()

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
        output_text = "<p>No classmates have been added yet.</p>"

    output.innerHTML = output_text

# ================= ATTENDANCE GRAPH =================

days = []
absences = []

def sample_numpy(event=None):

    day = document.getElementById("dayofweek").value
    absence = document.getElementById("absences").value

    if absence == "":
        return

    absence = int(absence)

    # STORE DATA
    days.append(day)
    absences.append(absence)

    # CREATE ARRAYS
    x = np.arange(len(days))
    y = np.array(absences)

    # CLEAR OLD GRAPH
    plt.clf()

    # CREATE GRAPH
    plt.plot(x, y, marker='o')

    # LABELS
    plt.xticks(x, days)

    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Days")
    plt.ylabel("Absences")

    plt.grid(True)

    # CLEAR OUTPUT DIV
    document.getElementById("output").innerHTML = ""

    # DISPLAY GRAPH
    display(plt, target="output", append=False)