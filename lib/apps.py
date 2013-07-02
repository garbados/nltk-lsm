import twitter
import facebook


def _twitter(config, user1, user2):
    results = []
    api = twitter.Api(**config)
    for user in [user1, user2]:
        texts = '\n'.join([status.text for status in api.GetUserTimeline(
            screen_name=user)])
        results.append(texts)
    return results

def _facebook(config, user1, user2):
    results = []
    graph = facebook.GraphAPI(config['oauth_token'])
    for user in [user1, user2]:
        response = graph.get_object('/'.join([user, "statuses"]), fields="message")
        statuses = '\n'.join([status['message'] for status in response['data']])
        if statuses:
            results.append(statuses)
        else:
            raise Exception("No statuses to parse from " + user)
    return results