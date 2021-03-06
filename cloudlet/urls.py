# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django.conf.urls import include
from django.conf.urls import url

from openstack_dashboard.dashboards.project.cloudlet.images \
    import urls as image_urls
from openstack_dashboard.dashboards.project.cloudlet.instances \
    import urls as instance_urls
from openstack_dashboard.dashboards.project.cloudlet \
    import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'', include(image_urls, namespace='images')),
    url(r'', include(instance_urls, namespace='instances')),
]
