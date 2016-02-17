
from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from haystack.views import SearchView
import minimal_logger.urls
from base.views import playground
from base.forms import SearchForm
from base.views import autocomplete


urlpatterns = (
	url(r'^playground/$', playground),
	url(r'^log/', include(minimal_logger.urls)),
	url(r'^sitemap.xml$', sitemap, {'sitemaps': {'cmspages': CMSSitemap}}),  # todo: do something to have this used?
	# url(r'^backup/media$', download_media, name='backup_media'),
	# url(r'^backup/db$', download_database, name='backup_db'),
	# url(r'^backup$', lambda request: redirect(reverse('backup_db')), name='backup'),
	# url(r'^backup/restore$', upload_database, name='restore'),
	url(r'^search/$', SearchView(template='search_page.html', form_class=SearchForm), name='search'),
	url(r'^autocomplete/$', autocomplete, name='autocomplete'),
)


