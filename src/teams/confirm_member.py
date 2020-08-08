from flask import request

from src.flaskapp.util import format_string, return_resp
from src.flaskapp.db import coll
from src.flaskapp.schemas import (
    ensure_json,
    ensure_user_logged_in,
    ensure_feature_is_enabled,
)


<<<<<<< HEAD
@ensure_json()
@ensure_user_logged_in()
@ensure_feature_is_enabled("confirm member")
def confirm():
    if request.method == "POST":
        data = request.get_json(silent=True)
        email = data["user_email"]
        email = format_string(email)
        if not data or "email" not in data or not data["email"]:
            return return_resp(401, "Missing inf")
        hacker = format_string(data["email"])
        team_name = coll("teams").find_one({"members": {"$all": [email]}}, {"_id"})[
            "_id"
        ]
        team = coll("teams").find_one({"_id": team_name})
        team_members = team["members"]
        complete = coll("teams").find_one({"_id": team_name, "complete": True})
        if len(team_members) >= 4 or complete:
            return return_resp(402, "Team Complete")
        coll("users").update_one({"_id": hacker}, {"$set": {"hasateam": True}})
        coll("users").update_one(
            {"_id": hacker}, {"$pull": {"potentialteams": team_name}}
        )
        coll("teams").update_one({"_id": team_name}, {"$push": {"members": hacker}})
        coll("teams").update_one({"_id": team_name}, {"$pull": {"interested": hacker}})
        return return_resp(200, "Success")
=======

def confirm(email, hacker):  # if request.method == 'POST'
    team_name = coll("teams").find_one({"members": {"$all": [email]}}, {"_id"})['_id']
    team = coll("teams").find_one({"_id": team_name})
    team_members = team['members']
    complete = coll("teams").find_one({"_id": team_name, "complete": True})
    if len(team_members) >= 4 or complete:
        return return_resp(402, "Team Complete")
    coll("users").update_one({"_id": hacker}, {"$set": {"hasateam": True}})
    coll("users").update_one({"_id": hacker}, {"$pull": {"potentialteams": team_name}})
    coll("teams").update_one({"_id": team_name}, {"$push": {"members": hacker}})
    coll("teams").update_one({"_id": team_name}, {"$pull": {"interested": hacker}})
    return return_resp(200, "Success")
>>>>>>> 60d5414739f632846331633b5ee8e567451fcbae
