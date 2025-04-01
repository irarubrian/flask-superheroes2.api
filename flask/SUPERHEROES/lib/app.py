from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict_basic() for hero in heroes])

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({'error': 'Hero not found'}), 404
    return jsonify(hero.to_dict_with_powers())

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict_basic() for power in powers])

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404
    return jsonify(power.to_dict_basic())

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404

    data = request.get_json()
    if 'description' not in data:
        return jsonify({'errors': ['description is required']}), 400

    new_description = data['description']

    try:
        power.description = new_description
        db.session.commit()
    except ValueError as e:
        db.session.rollback()
        return jsonify({'errors': [str(e)]}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'errors': ['An error occurred']}), 500

    return jsonify(power.to_dict_basic()), 200

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    required_fields = ['strength', 'power_id', 'hero_id']
    if not all(field in data for field in required_fields):
        return jsonify({'errors': ['Missing required fields']}), 400

    strength = data['strength']
    power_id = data['power_id']
    hero_id = data['hero_id']

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)
    if not hero or not power:
        return jsonify({'errors': ['Hero or Power not found']}), 404

    try:
        hero_power = HeroPower(
            strength=strength,
            hero_id=hero_id,
            power_id=power_id
        )
        db.session.add(hero_power)
        db.session.commit()
    except ValueError as e:
        db.session.rollback()
        return jsonify({'errors': [str(e)]}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'errors': ['An error occurred']}), 500

    return jsonify(hero_power.to_dict()), 201

if __name__ == '__main__':
    app.run(port=5555)