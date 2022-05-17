from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Please subscribe, like, and comment on this video, TY!!! This is GitOPs with ArgoCD Demo from Security Delivery!!!!'
