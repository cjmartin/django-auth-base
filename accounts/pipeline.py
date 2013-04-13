import flickr_api
from urlparse import parse_qs

def update_extra_values(backend, user, response, is_new, *args, **kwargs):
    profile = user.get_profile()
    
    # This isn't necessary (unless you want more flickr user data).
    # It's here to illustrate use of the flickr API, comment out to speed things up.
    flickr_user = flickr_api.Person(nsid=response['id'])
    flickr_user_info = flickr_user.getInfo()
    print(flickr_user_info)
    
    access_token = parse_qs(response['access_token'])
    
    profile.flickr_nsid = response['id']
    profile.flickr_username = response['username']
    profile.flickr_fullname = response['fullname']
    profile.flickr_oauth_token = access_token['oauth_token'][0]
    profile.flickr_oauth_token_secret = access_token['oauth_token_secret'][0]
    
    profile.save()
    return None