from pyscript import document
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io, base64


scores = []
labels = []


def show_stats():
    np_scores = np.array(scores)
    avg = np.mean(np_scores)
    high = np.max(np_scores)
    low = np.min(np_scores)

    document.getElementById('output').innerHTML = (
        f"<b>Scores:</b> {scores}<br>"
        f"<b>Average:</b> {round(float(avg), 2)}<br>"
        f"<b>Highest:</b> {int(high)}<br>"
        f"<b>Lowest:</b> {int(low)}"
    )


def draw_graph():
    plt.figure(figsize=(6, 4))
    plt.plot(labels, scores, marker='o', color='blue', label='Score')
    plt.axhline(y=float(np.mean(np.array(scores))), color='red', linestyle='--', label='Average')
    plt.title("Student Performance Graph")
    plt.xlabel("Activities")
    plt.ylabel("Score")
    plt.legend()
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()

    document.getElementById('graph').innerHTML = f'<img src="data:image/png;base64,{img}">'


def add_score(event):
    activity = document.getElementById('activity').value
    score = document.getElementById('score').value

    if activity == "" or score == "":
        document.getElementById('output').innerHTML = "Please fill in both fields."
        return

    labels.append(activity)
    scores.append(float(score))

    document.getElementById('score').value = ''

    show_stats()
    draw_graph()


def reset_all(event):
    scores.clear()
    labels.clear()
    document.getElementById('output').innerHTML = "No scores yet."
    document.getElementById('graph').innerHTML = ""

