from urllib.parse import urlparse

def format(url,i,j):
    parsed_url = urlparse(url)
    path_segments = parsed_url.path.split('/')
    desired_path = "/".join(path_segments[i:j])
    return desired_path