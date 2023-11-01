from flask import Flask, jsonify
from flask_restful import Api
from resources.webhook import Migracao_Webhook

app = Flask("Github")
api = Api(app)

api.add_resource(Migracao_Webhook, '/migration-moonlight')

@app.route("/health")
def health():
    return jsonify({"health": True})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5001')