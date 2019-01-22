from django.conf.urls import url
from blog.views import post_list, post_detail


urlpatterns = [
	# post views
	url(r'^$',post_list, name ='post_list'),
	# url(r'^$',post_list, name ='post_list'),
	url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',post_detail, name ='post_detail'),
]