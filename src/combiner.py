import pandas as pd
from functools import reduce

class Combiner:
    # This will return the id to name dataframe
    @staticmethod
    def convert_id_to_name_df(roll_call_dict: dict):
        df = pd.DataFrame(data=[], columns=["display_name", "id", "party", "state", "vote"])
        vote_id = roll_call_dict.get("vote_id")
        votes_by_type = roll_call_dict.get("votes", {})
        rows = []
        for vote_type in ["Nay", "Yea", "Present", "Not Voting", "Aye", "No"]:
            votes = votes_by_type.get(vote_type, [])
            for v in votes:
                rows.append({
                    "id": v["id"],
                    "state": v["state"],
                    "party": v["party"],
                    "name": v["display_name"]
                })
        df = pd.DataFrame(rows, columns=["id", "state", "party", "name"])
        return df    
    

    @staticmethod
    def convert_roll_call_into_df(roll_call_dict: dict):
        df = pd.DataFrame(data=[], columns=["display_name", "id", "party", "state", "vote"])
        vote_id = roll_call_dict.get("vote_id")
        votes_by_type = roll_call_dict.get("votes", {})
        rows = []
        for vote_type in ["Nay", "Yea", "Present", "Not Voting", "Aye", "No"]:
            votes = votes_by_type.get(vote_type, [])
            for v in votes:
                rows.append({
                    "id": v["id"],
                    vote_id: vote_type,
                })
        df = pd.DataFrame(rows, columns=["id", vote_id])
        
        return df

    @staticmethod
    def combine_all_roll_calls_into_df(roll_calls: list[dict]):
        vote_dfs = [Combiner.convert_roll_call_into_df(rc) for rc in roll_calls]
        name_dfs = [Combiner.convert_id_to_name_df(rc) for rc in roll_calls]
        # Merge the id->name dfs and id->votes dfs separately
        vote_df = reduce(lambda l, r: pd.merge(l, r, on="id", how="outer"), vote_dfs)
        name_df = reduce(lambda l, r: pd.merge(l, r, on=["id","state", "party", "name"], how="outer"), name_dfs)
        return vote_df, name_df