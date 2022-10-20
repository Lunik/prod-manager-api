import responses
import pytest

from prodmanager import ProdManager
from .utils import *
from .mock import mock_response

class TestScope:
  def setup(self):
    self.pm = ProdManager(PRODMANAGER_URL, PRODMANAGER_SECRET)

  def test_scope_restmanager(self):
    assert str(self.pm.scope) == "<RestManager(Scope) /scope>"

  @responses.activate
  def test_scope_list(self):
    mock_response('GET', 'scope', 'scope_list_page_1')

    scopes = self.pm.scope.list()
    scope = next(scopes)
    assert scope.name == "France DC01"

    scope = next(scopes)
    assert scope.name == "France DC02"

  @responses.activate
  def test_scope_get(self):
    mock_response('GET', 'scope', 'scope_get_1')

    scope = self.pm.scope.get(1)
    assert scope.name == "France DC01"

    assert scope.incidents_count >= 0
    assert scope.maintenances_count >= 0
    assert scope.monitors_count['alert'] >= 0
    assert scope.monitors_count['warning'] >= 0
    assert scope.monitors_count['ok'] >= 0

    assert str(scope) == "<RestObject(Scope) /scope/1>"

  @responses.activate
  def test_scope_get_notfound(self):
    mock_response('GET', 'scope', 'scope_get_404')

    with pytest.raises(Exception) as e:
      scope = self.pm.scope.get(404)

  @responses.activate
  def test_scope_count(self):
    mock_response('GET', 'scope', 'scope_list_per_page_0')

    count = self.pm.scope.count()
    assert count == 9

  @responses.activate
  def test_scope_list_iterator(self):
    mock_response('GET', 'scope', 'scope_list_page_1_per_page_5')
    mock_response('GET', 'scope', 'scope_list_page_2_per_page_5')

    total = 0
    for scope in self.pm.scope.list(per_page=5):
      assert len(scope.name) > 0

      total += 1

    assert total == 9

  @responses.activate
  def test_scope_list_iterator_list(self):
    mock_response('GET', 'scope', 'scope_list_page_1_per_page_5')
    mock_response('GET', 'scope', 'scope_list_page_2_per_page_5')

    scopes = list(self.pm.scope.list(per_page=5))

    assert len(scopes) == 9

  @responses.activate
  def test_scope_create(self):
    mock_response('POST', 'scope', 'scope_create')

    scope = self.pm.scope.create(
      name="France DC01",
      description="France datacenter - zone 01",
    )
    assert scope.name == "France DC01"

  @responses.activate
  def test_scope_updated(self):
    mock_response('GET', 'scope', 'scope_get_1')
    mock_response('POST', 'scope', 'scope_1_updated')

    scope = self.pm.scope.get(1)
    scope = scope.update(
      description="UPDATED - France datacenter - zone 01",
    )
    assert scope.description == "UPDATED - France datacenter - zone 01"

  @responses.activate
  def test_scope_deleted(self):
    mock_response('GET', 'scope', 'scope_get_1')
    mock_response('POST', 'scope', 'scope_1_delete')

    scope = self.pm.scope.get(1)
    scope.delete()
