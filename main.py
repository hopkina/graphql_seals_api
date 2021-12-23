from api import app, db
from api import models
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify

from api.queries import resolve_sightings, resolve_sighting
from api.mutations import resolve_create_sighting, resolve_update_location, \
    resolve_delete_sighting

query = ObjectType("Query")

query.set_field("sightings", resolve_sightings)
query.set_field("sighting", resolve_sighting)

mutation = ObjectType("Mutation")
mutation.set_field("createSighting", resolve_create_sighting)
mutation.set_field("updateLocation", resolve_update_location)
mutation.set_field("deleteSighting", resolve_delete_sighting)

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
