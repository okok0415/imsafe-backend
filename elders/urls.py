from django.urls import path
from elders.Api import elders
from elders.Api import alarms

urlpatterns = [
    path("elder/", elders.all_users, name="JsonAllUser"),
    path("alarm/", alarms.all_users, name="JsonAllAlarm"),
    path("json/<username>", elders.specific_user, name="JsonSpecificUser"),
    # path('html/', HtmlTest.all_users, name='HtmlAllUser'),
    # path('html/<username>', HtmlTest.specific_user, name='HtmlSpecificUser')
]
