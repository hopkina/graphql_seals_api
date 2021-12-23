from datetime import datetime

from ariadne import convert_kwargs_to_snake_case

from api import db
from api.models import Sighting


@convert_kwargs_to_snake_case
def resolve_create_sighting(obj, info, x_coord, y_coord, description, date_seen):
    try:
        date_seen = datetime.strptime(date_seen, '%d-%m-%Y').date()
        sighting = Sighting(
            x_coord=x_coord, 
            y_coord=y_coord, 
            description=description, 
            date_seen=date_seen
        )
        db.session.add(sighting)
        db.session.commit()
        payload = {
            "success": True,
            "sighting": sighting.to_dict()
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_update_location(obj, info, sighting_id, x_coord, y_coord):
    try:
        sighting = Sighting.query.get(sighting_id)
        sighting.x_coord = x_coord
        sighting.y_coord = y_coord
        db.session.add(sighting)
        db.session.commit()
        payload = {
            "success": True,
            "sighting": sighting.to_dict()
        }
    except AttributeError:  # sighting not found
        payload = {
            "success": False,
            "errors":  [f"Sighting matching id {sighting_id} was not found"]
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_delete_sighting(obj, info, sighting_id):
    try:
        sighting = Sighting.query.get(sighting_id)
        db.session.delete(sighting)
        db.session.commit()
        payload = {"success": True}

    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"sighting matching id {sighting_id} not found"]
        }

    return payload


