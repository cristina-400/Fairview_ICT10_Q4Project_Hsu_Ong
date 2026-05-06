from pyscript import document
from js import localStorage
import json


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


# ✅ ADD CLASSMATE (unchanged, still works)
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
    localStorage.setItem("classmates", json.dumps(classmates))


    output.innerHTML = "✅ Info Added Successfully!"


# ✅ FIXED VIEW FUNCTION
def check_classmate(event=None):
    classmates_json = localStorage.getItem("classmates")
    output = document.getElementById("output3")


    if classmates_json:
        classmates = json.loads(classmates_json)
        output_text = "<h3>Classmates:</h3><ul>"
        for p in classmates:
            output_text += f"<li>Hi, I'm {p['name']} from {p['section']} and my favorite subject is {p['subject']}.</li>"
        output_text += "</ul>"
    else:
        output_text = "<p>No classmates have been added yet.</p>"


    output.innerHTML = output_text


    # store data globally
days = []
absences = []




def sample_numpy(event):


    # get values from HTML (FIXED ID)
    day = document.getElementById("dayofweek").value
    absence = document.getElementById("absences").value


    # validate input
    if absence == "":
        return


    absence = int(absence)


    # store data
    days.append(day)
    absences.append(absence)


    # NUMPY ARRAYS
    x = np.array(days)          # categorical data
    y = np.array(absences)     # numeric data


    # convert x into index positions for graphing
    x_index = np.arange(len(days))


    # create graph
    fig = plt.figure(5.5)
    plt.plot(x_index, y, marker='o', color='blue')


    # replace numbers with day labels
    plt.xticks(x_index, x)


    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Days")
    plt.ylabel("Absences")


    plt.grid(True)


    # clear previous output
    document.getElementById("output").innerHTML = ""


    # DISPLAY FIGURE
    display(fig, target="output")
