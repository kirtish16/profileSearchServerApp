import requests
from .utils import Profile, Repos

API_BASE_URL = "https://api.github.com"
GITHUB_ACCESS_TOKEN = ''
HEADERS = {'Authorization' : 'Token ' + GITHUB_ACCESS_TOKEN}

# Helper function to check if a user exists
def userExists(username):
    try:
        USER_DETAILS_BASE_URL = API_BASE_URL + "/users/"

        url = USER_DETAILS_BASE_URL + username 

        # Make the API request
        response = requests.get(url,headers=HEADERS)

        if response.status_code == 200 :
            return True

    except requests.exceptions.RequestException as e:
        print("Error:", e)

    return False

# Helper function to get user info
def getGithubUserInfo(username):
    data = {}
    try:
        USER_DETAILS_BASE_URL = API_BASE_URL + "/users/"

        url = USER_DETAILS_BASE_URL + username 

        # Make the API request
        response = requests.get(url,headers=HEADERS)

        # Parse the JSON response
        user_data = response.json()

        if response.status_code != 200 :
            error_message= {'error': True,'message' : user_data['message']}
            data = error_message
            return data

        # Extracting relevant data from details and converting to dictionary 
        data = Profile(user_data).__dict__

    except requests.exceptions.RequestException as e:
        print("Error:", e)

    return data



# Helper function to get user repos info
def getGithubUserReposInfo(username,itemsPerPage=10,pageNumber=1):
    data = {}
    try:
        USER_DETAILS_BASE_URL = API_BASE_URL + "/users/{}/repos?sort=created_at&order=desc&per_page={}&page={}"

        url = USER_DETAILS_BASE_URL.format(username,itemsPerPage,pageNumber)

        # Make the API request
        response = requests.get(url,headers=HEADERS)

        # Parse the JSON response
        user_repos_data = response.json()

        if response.status_code != 200 :
            data['error'] = True
            data['message'] = user_repos_data['message']
            return data
        
        repos_data = []
        for repos_details in user_repos_data : 
            # Extracting relevant data from details and converting to dictionary 
            repos_data.append(Repos(repos_details).__dict__)

        data['repos'] = repos_data

    except requests.exceptions.RequestException as e:
        print("Error:", e)

    return data