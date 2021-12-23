from datetime import datetime

from ariadne import convert_kwargs_to_snake_case

from api import db
from api.models import Site


@convert_kwargs_to_snake_case
def resolve_create_site(obj, info, x_coord, y_coord, description, date_updated):
    try:
        date_updated = datetime.strptime(date_updated, '%d-%m-%Y').date()
        site = Site(
            x_coord=x_coord, 
            y_coord=y_coord, 
            description=description, 
            date_updated=date_updated
        )
        db.session.add(site)
        db.session.commit()
        payload = {
            "success": True,
            "site": site.to_dict()
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_update_location(obj, info, site_id, x_coord, y_coord):
    try:
        site = Site.query.get(site_id)
        site.x_coord = x_coord
        site.y_coord = y_coord
        db.session.add(site)
        db.session.commit()
        payload = {
            "success": True,
            "site": site.to_dict()
        }
    except AttributeError:  # site not found
        payload = {
            "success": False,
            "errors":  [f"Site matching id {site_id} was not found"]
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_delete_site(obj, info, site_id):
    try:
        site = Site.query.get(site_id)
        db.session.delete(site)
        db.session.commit()
        payload = {"success": True}

    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"site matching id {site_id} not found"]
        }

    return payload
