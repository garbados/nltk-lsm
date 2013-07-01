import twitter


def _twitter(config, user1, user2):
    results = []
    api = twitter.Api(**config)
    for user in [user1, user2]:
        texts = '\n'.join([status.text for status in api.GetUserTimeline(
            screen_name=user)])
        results.append(texts)
    return results
