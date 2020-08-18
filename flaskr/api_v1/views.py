import requests, sys

from flask import request, Response

from . import api_v1_bp
from flaskr.models import Planet
from flaskr.utils.database import db

api_timeout = 5

@api_v1_bp.route('/planets', methods=["POST"])
def create_planet():
  data = request.get_json()
  
  force_create = data['force'] if 'force' in data else False

  planet = Planet(
    name=data['name'],
    climate=data['climate'],
    terrain=data['terrain']
  )
  try:
    r = requests.get(f'https://swapi.dev/api/planets/?search={planet.name}', timeout=api_timeout)
    planet_data = r.json()
    any_planet = len(planet_data['results']) > 0
    if(not any_planet and not force_create):
      return {'message': f'Não foi possível buscar a quantidade de\
 aparições para o planeta: {planet.name}. Para forçar a criação utilize a chave "force" = true',
            'errors': [{'planetNotFound': planet.name}]}, 404
    movies_appearances = len(planet_data['results'][0]['films']) if any_planet else 0
    planet.movies_appearances = movies_appearances
    db.session.add(planet)
    db.session.commit()
    return {'message': f'O planeta {planet.name} foi criado com sucesso!', 'data': planet.to_dict()}, 201
  except requests.ConnectionError:
    return {'message': 'Resposta não recebida!',
            'errors': [{'ServerNotFound': f'Não foi possível se conectar com a API.'}]}, 502
  except requests.ReadTimeout:
    return {'message': 'Resposta não recebida!',
            'errors': [{'Timeout': f'Servidor não respondeu em até {api_timeout} segundos.'}]}, 408
  except:
    e = sys.exc_info()[0]
    return {'message': f'Erro desconhecido!',
            'errors': [{'unexpectedError': repr(e)}]}, 500

@api_v1_bp.route('/planets', methods=["GET"])
def get_planets():
  if(len(request.args) > 0):
    search = request.args['search']
    planets_query = Planet.query.filter_by(name=search.title())
    total_docs = planets_query.count()
  else:  
    planets_query = Planet.query.all()
    total_docs = len(planets_query)
  
  if(total_docs < 1):
    return {'message': "Nenhum planeta encontrado!"}, 404

  planets = []
  for planet in planets_query:
    planets.append(planet.to_dict())
  return {'message': f'{len(planets)} planetas encontrados com sucesso!', 'planets': planets} 

@api_v1_bp.route('/planets/<int:planet_id>', methods=["GET"])
def get_planet_by_id(planet_id):
  planet_query = Planet.query.filter_by(id=planet_id).first()
  if(planet_query == None):
    return {'message': "Planeta não encontrado!"}, 404

  planet = planet_query.to_dict()

  return {'message': 'Planeta encontrado com sucesso!', 'planet': planet}

@api_v1_bp.route('/planets/<int:planet_id>', methods=["DELETE"])
def delete_planet_by_id(planet_id):
  planet = Planet.query.filter_by(id=planet_id).first()

  if(planet is None):
    return {'message': "Planeta não encontrado!"}, 404

  db.session.delete(planet)
  db.session.commit()

  return {'message': 'Planeta deletado com sucesso!'}, 200  

