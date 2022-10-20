import responses
import pytest

from prodmanager import ProdManager
from .utils import *
from .mock import mock_response

class TestService:
  def setup(self):
    self.pm = ProdManager(PRODMANAGER_URL, PRODMANAGER_SECRET)

  def test_service_restmanager(self):
    assert str(self.pm.service) == "<RestManager(Service) /service>"

  @responses.activate
  def test_service_list(self):
    mock_response('GET', 'service', 'service_list_page_1')

    services = self.pm.service.list()
    service = next(services)
    assert service.name == "Block Storage"

    service = next(services)
    assert service.name == "Compute"

  @responses.activate
  def test_service_get(self):
    mock_response('GET', 'service', 'service_get_1')

    service = self.pm.service.get(1)
    assert service.name == "Databases"

    assert service.incidents_count >= 0
    assert service.maintenances_count >= 0
    assert service.monitors_count['alert'] >= 0
    assert service.monitors_count['warning'] >= 0
    assert service.monitors_count['ok'] >= 0

    assert str(service) == "<RestObject(Service) /service/1>"

  @responses.activate
  def test_service_get_notfound(self):
    mock_response('GET', 'service', 'service_get_404')

    with pytest.raises(Exception) as e:
      service = self.pm.service.get(404)

  @responses.activate
  def test_service_count(self):
    mock_response('GET', 'service', 'service_list_per_page_0')

    count = self.pm.service.count()
    assert count == 8

  @responses.activate
  def test_service_list_iterator(self):
    mock_response('GET', 'service', 'service_list_page_1_per_page_5')
    mock_response('GET', 'service', 'service_list_page_2_per_page_5')

    total = 0
    for service in self.pm.service.list(per_page=5):
      assert len(service.name) > 0

      total += 1

    assert total == 8

  @responses.activate
  def test_service_list_iterator_list(self):
    mock_response('GET', 'service', 'service_list_page_1_per_page_5')
    mock_response('GET', 'service', 'service_list_page_2_per_page_5')

    services = list(self.pm.service.list(per_page=5))

    assert len(services) == 8

  @responses.activate
  def test_service_create(self):
    mock_response('POST', 'service', 'service_create')

    service = self.pm.service.create(
      name="Databases",
      description="Databases PaaS services",
    )
    assert service.name == "Databases"

  @responses.activate
  def test_service_updated(self):
    mock_response('GET', 'service', 'service_get_1')
    mock_response('POST', 'service', 'service_1_updated')

    service = self.pm.service.get(1)
    service = service.update(
      description="UPDATED - Databases PaaS services",
    )
    assert service.description == "UPDATED - Databases PaaS services"

  @responses.activate
  def test_service_deleted(self):
    mock_response('GET', 'service', 'service_get_1')
    mock_response('POST', 'service', 'service_1_delete')

    service = self.pm.service.get(1)
    service.delete()
