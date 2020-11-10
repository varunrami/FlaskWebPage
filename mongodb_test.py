import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'test',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

class User(db.Document):
    name = db.StringField()
    metadata = db.DictField()
    image = db.StringField()
    def to_json(self):
        return {"name": self.name,
                "image": self.image,
                "metadata": self.metadata}

@app.route('/query_records', methods=['GET','POST'])
def query_records():
    query = json.loads(request.data)
    print(query)
    user = User.objects(__raw__=query)
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        print("returned obkect")
        return jsonify(user)

@app.route('/create_record', methods=['PUT','POST','GET'])
def create_record():
    record = json.loads(request.data)
    user = User(name=record['name'],
                image=record['image'],
                metadata=record['metadata'])
    user.save()
    return jsonify(user.to_json())

#@app.route('/update_record', methods=['POST','GET'])
#def update_record():
    #record = json.loads(request.data)
 #   user = User.objects(name="Varun").first()#record['name']).first()
  #  if not user:
  #      return jsonify({'error': 'data not found'})
  #  else:
  #      user.update(email="sonaal@gmail.com")#record['email'])
  #  return jsonify(user.to_json())

#@app.route('/delete_record', methods=['DELETE'])
#def delete_record():
#    #record = json.loads(request.data)
#    user = User.objects(name=record['name']).first()
#    if not user:
#        return jsonify({'error': 'data not found'})
##    else:
 #       user.delete()
 #   return jsonify(user.to_json())

if __name__ == "__main__":
    app.run(debug=True)