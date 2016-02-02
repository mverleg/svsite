
from django.contrib.messages import add_message, DEBUG, INFO, SUCCESS, WARNING, ERROR
from django.shortcuts import redirect, render


def playground(request):
	#todo: remove eventually
	#assert settings.DEBUG
	raise Exception('hello world!')
	add_message(request, DEBUG, 'Here is a message for you!')  # doesn't show
	add_message(request, INFO, 'Here is a message for you again!')
	add_message(request, SUCCESS, 'Here is a message for you once more!')
	add_message(request, WARNING, 'Here is yet another message for you!')
	add_message(request, ERROR, 'Here is the last message for you!')
	return redirect(to='/en/')


def notification(request, message, title = None, next = None):
	return render(request, 'notification.html', {
		'message': message,
		'title': title,
		'next': next,
	})


def error_view(request, message, title = None, next = None, status = 400):
	"""
		:param status:

			* 400 and subset mean something was wrong with the request (e.g. user error; this request will never work)
			* 500 and subset mean server error (might work after it's fixed)
			* See more: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
	"""
	return render(request, 'error.html', {
		'message': message,
		'title': title,
		'next': next,
	}, status = status)


def csrf_failure(request, reason):
	return error_view(request,
		message = 'There was a problem with the security (csrf protection). If the problem persists after reloading, please contact us.',
	)


