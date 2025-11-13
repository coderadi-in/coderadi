'''coderadi &bull; site runner `development only`'''

# ? IMPORTING MAIN FILE
from main import server

# ! RUNNING SERVER
if (__name__ == "__main__"):
    server.run(debug=True, host='0.0.0.0')