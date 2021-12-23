from ariadne import convert_kwargs_to_snake_case

from .models import Sighting


def resolve_sightings(obj, info):
    try:
        sightings = [sighting.to_dict() for sighting in Sighting.query.all()]
        payload = {
            "success": True,
            "sightings": sightings
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def resolve_sighting(obj, info, sighting_id):
    try:
        sighting = Sighting.query.get(sighting_id)
        payload = {
            "success": True,
            "sighting": sighting.to_dict()
        }

    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Sighting item matching id {sighting_id} not found"]
        }

    return payload
