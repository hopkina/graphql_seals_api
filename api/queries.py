from ariadne import convert_kwargs_to_snake_case

from .models import Site


def resolve_sites(obj, info):
    try:
        sites = [site.to_dict() for site in Site.query.all()]
        payload = {
            "success": True,
            "sites": sites
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def resolve_site(obj, info, site_id):
    try:
        site = Site.query.get(site_id)
        payload = {
            "success": True,
            "site": site.to_dict()
        }

    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Site item matching id {site_id} not found"]
        }

    return payload
