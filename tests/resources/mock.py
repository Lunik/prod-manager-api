import responses

from .mock_responses.scope import API_RESPONSES as ScopeAPIResponses
from .mock_responses.service import API_RESPONSES as ServiceAPIResponses
from .mock_responses.monitor import API_RESPONSES as MonitorAPIResponses
from .mock_responses.weather import API_RESPONSES as WeatherAPIResponses

from .utils import *

API_TYPE = dict(
  scope=ScopeAPIResponses,
  service=ServiceAPIResponses,
  monitor=MonitorAPIResponses,
  weather=WeatherAPIResponses,
)

def mock_response(method, api_type, name):
  data = API_TYPE[api_type][name]
  
  responses.add(
    method=method,
    url=f"{PRODMANAGER_API_URL}/{data['path']}",
    json=data['json'],
    headers=data['headers'],
    status=data.get('status', 200),
  )