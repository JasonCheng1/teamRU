from app.util import call_validate_endpoint, return_resp, call_auth_endpoint, get_name, coll
from flask import request


def get_team_profile(email, token):
    email = email.strip().lower()
    if call_validate_endpoint(email, token) != 200:
        return return_resp(404, "Invalid request")
    else:
        if request.method == 'GET':
            team = coll("teams").find_one({"members": {"$all": [email]}})
            if not team:
                return return_resp(400, "Team Not found")
            else:
                members = team['members']
                members_names = []
                for member in members:
                    token = call_auth_endpoint()
                    if token == 200:
                        continue
                    name = get_name(token, member)
                    if name == 200:
                        continue
                    members_names.append(name)
                    team.update({"names": members_names})
                return return_resp(200, team)
