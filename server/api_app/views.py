from django.http import JsonResponse

from .helpers import *

# Check if provided username exists
def checkUser(request,id):

    if not userExists(id):
        return JsonResponse({"success":False,"message":"Invalid username"},status=404)

    return JsonResponse({"success":True,"message":"Valid User"},status=200)


# Get details about the user
def getUserDetails(request,id):
    
    # Get Github user details
    search_result = getGithubUserInfo(id)

    # User details obtained
    if not search_result.get('error') : 
        return JsonResponse(search_result,status=200)

    return JsonResponse(search_result,status=404)

# Get details about the user repos
def getUserReposDetails(request,id):

    itemsPerPage = request.GET.get('per_page') if request.GET.get('per_page') else 10
    pageNumber = request.GET.get('page') if request.GET.get('page') else 1

    # Get Github user repos details
    search_result = getGithubUserReposInfo(id,itemsPerPage,pageNumber)

    # User Repos details obtained
    if not search_result.get('error') : 
        return JsonResponse(search_result,status=200)

    return JsonResponse(search_result,status=404)
