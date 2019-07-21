from rest_framework import routers
from books.views import BookViewSet

router = routers.SimpleRouter()
router.register(r'book', BookViewSet)

urlpatterns = router.urls
