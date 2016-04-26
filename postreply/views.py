from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.utils import timezone
from .models import Post, Reply
from django.core.context_processors import request
from django.http.response import HttpResponseRedirect

# Create your views here.

def home(request):
	username = request.user
	return render(request,'base.html',{'user':username})


def postform(request):
	posts = Post.objects.all().order_by('-posted_date')
	replys = Reply.objects.all().order_by('-posted_date')
	for rep in posts:
		reply = list(Reply.objects.filter(post=rep))
		rep.reply = reply
		print rep.reply
				
	return render(request, "post-reply.html",  { 'posts': posts})


@csrf_exempt
def addpost(request):
	print "welcome"
	data = request.POST.get('post_data',' ')
	print data
	print request.user
	print  timezone.now()
	post = Post(post = data, user = request.user, posted_date = timezone.now(), updated=timezone.now())
	post.save()
	response = "True"
	#response = json.dumps(datasend)
	return HttpResponse(response)

def getdata(request):
	posts = Post.objects.all().order_by('-posted_date')
	replys = Reply.objects.all().order_by('-posted_date')
	for rep in posts:
		reply = list(Reply.objects.filter(post=rep))
		rep.reply = reply
		
	html=render_to_string('postrender.html', { 'posts': posts})
	return HttpResponse(html)

@csrf_exempt	
def addreply(request):
	data = request.POST['reply_data']
	data_id = request.POST.get('postid',1)
	try:
		repost = Post.objects.get(id=int(data_id))
	except:
		print("addreply" + data_id)
	finally:
		print(data_id)	
		
	reply = Reply(user = request.user, post=repost, reply=data, posted_date=timezone.now())
	reply.save()
	response = "True"
	#response = json.dumps(datasend)
	return HttpResponse(response)


