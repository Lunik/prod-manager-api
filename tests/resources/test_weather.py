import responses
import pytest

from prodmanager import ProdManager
from .utils import *
from .mock import mock_response

class TestWeather:
  def setup(self):
    self.pm = ProdManager(PRODMANAGER_URL, PRODMANAGER_SECRET)

  def test_weather_restmanager(self):
    assert str(self.pm.weather) == "<RestManager(Weather) /weather>"

  @responses.activate
  def test_weather_get_monitor(self):
    mock_response('GET', 'weather', 'wheather_get_monitor')

    monitor_weather = self.pm.weather.monitor()

    assert monitor_weather.ok == 59
    assert monitor_weather.alert == 5
    assert monitor_weather.warning == 8

    assert str(self.pm.weather.monitor) == "<RestManager(Monitor) /weather/monitor>"

  @responses.activate
  def test_weather_get_incident(self):
    mock_response('GET', 'weather', 'wheather_get_incident')

    incident_weather = self.pm.weather.incident()

    assert incident_weather.active == 1
    assert incident_weather.investigating == 0
    assert incident_weather.resolved == 2
    assert incident_weather.stable == 1

    assert str(self.pm.weather.incident) == "<RestManager(Incident) /weather/incident>"

  @responses.activate
  def test_weather_get_maintenance(self):
    mock_response('GET', 'weather', 'wheather_get_maintenance')

    maintenance_weather = self.pm.weather.maintenance()

    assert maintenance_weather.canceled == 0
    assert maintenance_weather.failed == 0
    assert getattr(maintenance_weather, 'in-progress') == 1
    assert maintenance_weather.scheduled == 1
    assert maintenance_weather.succeed == 1

    assert str(self.pm.weather.maintenance) == "<RestManager(Maintenance) /weather/maintenance>"
