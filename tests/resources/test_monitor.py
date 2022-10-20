import responses
import pytest

from prodmanager import ProdManager
from .utils import *
from .mock import mock_response

class TestMonitor:
  def setup(self):
    self.pm = ProdManager(PRODMANAGER_URL, PRODMANAGER_SECRET)

  def test_monitor_restmanager(self):
    assert str(self.pm.monitor) == "<RestManager(Monitor) /monitor>"

  @responses.activate
  def test_monitor_list(self):
    mock_response('GET', 'monitor', 'monitor_list_page_1')

    monitors = self.pm.monitor.list()
    monitor = next(monitors)
    assert monitor.name == "[F][B] Service status"

    monitor = next(monitors)
    assert monitor.name == "[F][B] Service status"

  @responses.activate
  def test_monitor_get(self):
    mock_response('GET', 'monitor', 'monitor_get_1')

    monitor = self.pm.monitor.get(1)
    assert monitor.name == "[F][D] Service status"

    assert str(monitor) == "<RestObject(Monitor) /monitor/1>"

  @responses.activate
  def test_monitor_get_notfound(self):
    mock_response('GET', 'monitor', 'monitor_get_404')

    with pytest.raises(Exception) as e:
      monitor = self.pm.monitor.get(404)

  @responses.activate
  def test_monitor_count(self):
    mock_response('GET', 'monitor', 'monitor_list_per_page_0')

    count = self.pm.monitor.count()
    assert count == 9

  @responses.activate
  def test_monitor_list_iterator(self):
    mock_response('GET', 'monitor', 'monitor_list_page_1_per_page_5')
    mock_response('GET', 'monitor', 'monitor_list_page_2_per_page_5')

    total = 0
    for monitor in self.pm.monitor.list(per_page=5):
      assert len(monitor.name) > 0

      total += 1

    assert total == 9

  @responses.activate
  def test_monitor_list_iterator_list(self):
    mock_response('GET', 'monitor', 'monitor_list_page_1_per_page_5')
    mock_response('GET', 'monitor', 'monitor_list_page_2_per_page_5')

    monitors = list(self.pm.monitor.list(per_page=5))

    assert len(monitors) == 9

  @responses.activate
  def test_monitor_create(self):
    mock_response('POST', 'monitor', 'monitor_create')

    monitor = self.pm.monitor.create(
      name="[F][D] Service status",
      description="Status of Databases in France DC01",
    )
    assert monitor.name == "[F][D] Service status"

  @responses.activate
  def test_monitor_updated(self):
    mock_response('GET', 'monitor', 'monitor_get_1')
    mock_response('POST', 'monitor', 'monitor_1_updated')

    monitor = self.pm.monitor.get(1)
    monitor = monitor.update(
      description="UPDATED - Status of Databases in France DC01",
    )
    assert monitor.description == "UPDATED - Status of Databases in France DC01"

  @responses.activate
  def test_monitor_deleted(self):
    mock_response('GET', 'monitor', 'monitor_get_1')
    mock_response('POST', 'monitor', 'monitor_1_delete')

    monitor = self.pm.monitor.get(1)
    monitor.delete()
