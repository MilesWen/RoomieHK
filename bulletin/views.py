from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from bulletin.models import User, Room, Bookmark, Friend

## login via id & pwd pair or via cookies
def login(request):
	# This is a test in branch-Miles
	return render(request, 'bulletin/login.html')

# loging via FB
def login_FB(request):
	return render(request, 'bulletin/login.html')

# show profile of user
def profile(request, user_id):
	# scenario: user wants to check the profile of the roomate/room owner
	context_dict = {}

	try:
		user = User.objects.get(id=user_id)
		context_dict['userInfo'] = user

	except User.DoesNotExist:
		pass

	return render(request, 'bulletin/profile.html',context_dict)

# ask for preference (filtering info) from user
def preferences(request, user_id):
	context_dict = {}
	# scenario: user wants to check his/her preferences

	try:
		user = User.objects.get(id=user_id)
		context_dict['userInfo'] = user

	except User.DoesNotExist:
		pass

	return render(request, 'bulletin/preferences.html',context_dict)

# return bulletin listing
def listing(request, user_id):
	return render(request, 'bulletin/listing.html')

# return bulletin details
def details(request, room_id):
	# scenario: user views the details of a room and its owner details
	context_dict = {}
	
	try:
		room = Room.objects.get(id=room_id)
		context_dict['roomInfo'] = room
		context_dict['ownerInfo'] = room.user
		
		owner_id = room.id
		print room.id
	
	except Room.DoesNotExist:
		pass

    # Go render the response and return it to the client.
	return render(request, 'bulletin/details.html', context_dict)