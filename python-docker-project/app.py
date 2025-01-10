from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = (
    "mssql+pyodbc://@DESKTOP-F6D48BK\\SQLEXPRESS/your_database"
    "?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Human(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }

@app.route('/')
def home():
    with app.app_context():
        db.create_all()
    return "Hello, Flask with SQL Server!"


@app.route('/humans', methods=['POST'])
def create_human():
    data = request.json
    new_human = Human(
        first_name=data['first_name'],
        last_name=data['last_name'],
        age=data['age']
    )
    db.session.add(new_human)
    db.session.commit()
    return jsonify(new_human.to_dict()), 201

# گرفتن لیست انسان‌ها
@app.route('/humans', methods=['GET'])
def get_humans():
    humans = Human.query.all()
    return jsonify([human.to_dict() for human in humans])


@app.route('/humans/<int:human_id>', methods=['GET'])
def get_human(human_id):
    human = Human.query.get_or_404(human_id)
    return jsonify(human.to_dict())


@app.route('/humans/<int:human_id>', methods=['PUT'])
def update_human(human_id):
    data = request.json
    human = Human.query.get_or_404(human_id)

    human.first_name = data.get('first_name', human.first_name)
    human.last_name = data.get('last_name', human.last_name)
    human.age = data.get('age', human.age)

    db.session.commit()
    return jsonify(human.to_dict())


@app.route('/humans/<int:human_id>', methods=['DELETE'])
def delete_human(human_id):
    human = Human.query.get_or_404(human_id)
    db.session.delete(human)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
