from flask import Flask, request, render_template_string
from agents.orchestrator import run_pipeline
from agents.memory import init_db
import uuid, os
from config import UPLOAD_FOLDER

init_db()
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

HTML = """
<h1>AgriAide — Multi-Agent Farmer Assistant</h1>
<form action="/upload" method="post" enctype="multipart/form-data">
    <input type="file" name="file">
    <button type="submit">Analyze</button>
</form>
"""

RESULT = """
<h2>Diagnosis</h2>
<p>Disease: <b>{{ d }}</b> (Confidence: {{ c }})</p>

<h2>Advice</h2>
<p>{{ a }}</p>

<h2>Local Suppliers</h2>
<ul>
{% for s in sup %}
<li>{{ s }}</li>
{% endfor %}
</ul>

<a href="/">Try Another</a>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/upload", methods=["POST"])
def upload():
    f = request.files["file"]
    uid = str(uuid.uuid4())[:8]
    path = os.path.join(UPLOAD_FOLDER, uid + "_" + f.filename)
    f.save(path)

    res = run_pipeline(uid, path)

    return render_template_string(RESULT,
                                  d=res["diagnosis"]["disease"],
                                  c=res["diagnosis"]["confidence"],
                                  a=res["advice"],
                                  sup=res["suppliers"])

app.run(port=7860)
