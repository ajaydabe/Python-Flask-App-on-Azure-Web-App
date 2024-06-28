from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<center><h1>Hello, Azure Web Apps!</h1></center>"

if __name__ == '__main__':
  app.run()
