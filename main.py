from api import app, db
from api import models
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify

from api.queries import resolve_sites, resolve_site
from api.mutations import resolve_create_site, resolve_update_location, \
    resolve_delete_site

query = ObjectType("Query")

query.set_field("sites", resolve_sites)
query.set_field("site", resolve_site)

mutation = ObjectType("Mutation")
mutation.set_field("createSite", resolve_create_site)
mutation.set_field("updateLocation", resolve_update_location)
mutation.set_field("deleteSite", resolve_delete_site)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=True
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code
