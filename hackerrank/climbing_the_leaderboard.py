def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked = sorted(list(set(ranked)), reverse=True)
    player_rank = []
    l = len(ranked)

    for p in player:
        while (l > 0) and (p >= ranked[l-1]):
            l -= 1
        player_rank.append(l+1)

    return player_rank
