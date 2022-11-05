from ..utils import *

API_RESPONSES = {
  'scope_list_per_page_0': {
    'path': 'scope?per_page=0',
    'json': {
      "items": []
    },
    'headers': {
      'x-total-pages': '0',
      'x-total': '9',
      'x-page': '1',
      'x-per-page': '0',
      'x-prev-page': 'None',
      'x-next-page': 'None'
    }
  },
  'scope_list_page_1': {
    'path': 'scope?page=1',
    'json': {
      "items": [
        {
          "description": "France datacenter - zone 01",
          "id": 1,
          "incidents_count": 0,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?scope=1",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?scope=1",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?scope=1",
            "self": f"{PRODMANAGER_API_URL}/scope/1"
          },
          "maintenances_count": 0,
          "monitors_count": {
            "alert": 0,
            "ok": 8,
            "warning": 0
          },
          "name": "France DC01"
        }, {
          "description": "France datacenter - zone 02",
          "id": 2,
          "incidents_count": 1,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?scope=2",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?scope=2",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?scope=2",
            "self": f"{PRODMANAGER_API_URL}/scope/2"
          },
          "maintenances_count": 0,
          "monitors_count": {
            "alert": 0,
            "ok": 7,
            "warning": 1
          },
          "name": "France DC02"
        }, {
          "description": "France datacenter - zone 03",
          "id": 3,
          "incidents_count": 1,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?scope=3",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?scope=3",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?scope=3",
            "self": f"{PRODMANAGER_API_URL}/scope/3"
          },
          "maintenances_count": 1,
          "monitors_count": {
            "alert": 1,
            "ok": 7,
            "warning": 0
          },
          "name": "France DC03"
        }, {
          "description": "Japan datacenter - zone 01",
          "id": 7,
          "incidents_count": 0,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?scope=7",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?scope=7", 
            "monitors": f"{PRODMANAGER_API_URL}/monitor?scope=7",
            "self": f"{PRODMANAGER_API_URL}/scope/7"
          },
          "maintenances_count": 0,
          "monitors_count": {
            "alert": 0,
            "ok": 8,
            "warning": 0
          },
          "name": "Japan DC01"
        }, {
          "description": "Japan datacenter - zone 02",
          "id": 8,
          "incidents_count": 0,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?scope=8",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?scope=8",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?scope=8",
            "self": f"{PRODMANAGER_API_URL}/scope/8"
          },
          "maintenances_count": 1,
          "monitors_count": {
            "alert": 0,
            "ok": 7,
            "warning": 1
          },
          "name": "Japan DC02"
        }, {
          "description": "Japan datacenter - zone 03",
          "id": 9,
          "incidents_count": 1,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?scope=9",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?scope=9",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?scope=9",
            "self": f"{PRODMANAGER_API_URL}/scope/9"
          },
          "maintenances_count": 1,
          "monitors_count": {
            "alert": 0,
            "ok": 7,
            "warning": 1
          },
          "name": "Japan DC03"
        }, {
          "description": "West-US datacenter - zone 01",
          "id": 4,
          "incidents_count": 1,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?scope=4",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?scope=4",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?scope=4",
            "self": f"{PRODMANAGER_API_URL}/scope/4"
          },
          "maintenances_count": 0,
          "monitors_count": {
            "alert": 0,
            "ok": 7,
            "warning": 1
          },
          "name": "West-US DC01"
        }, {
          "description": "West-US datacenter - zone 02",
          "id": 5,
          "incidents_count": 0,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?scope=5",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?scope=5",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?scope=5",
            "self": f"{PRODMANAGER_API_URL}/scope/5"
          },
          "maintenances_count": 0,
          "monitors_count": {
            "alert": 1,
            "ok": 7,
            "warning": 0
          },
          "name": "West-US DC02"
        }, {
          "description": "West-US datacenter - zone 03",
          "id": 6,
          "incidents_count": 0,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?scope=6",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?scope=6",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?scope=6",
            "self": f"{PRODMANAGER_API_URL}/scope/6"
          },
          "maintenances_count": 0,
          "monitors_count": {
            "alert": 0,
            "ok": 6,
            "warning": 2
          },
          "name": "West-US DC03"
        }
      ]
    },
    'headers': {
      'x-total-pages': '1',
      'x-total': '9',
      'x-page': '1',
      'x-per-page': '20',
      'x-prev-page': 'None',
      'x-next-page': 'None'
    }
  },
  'scope_get_1': {
    'path': 'scope/1',
    'json': {
      "description": "France datacenter - zone 01",
      "id": 1,
      "incidents_count": 0,
      "links": {
        "incidents": f"{PRODMANAGER_API_URL}/incident?scope=1",
        "maintenances": f"{PRODMANAGER_API_URL}/maintenance?scope=1",
        "monitors": f"{PRODMANAGER_API_URL}/monitor?scope=1",
        "self": f"{PRODMANAGER_API_URL}/scope/1"
      },
      "maintenances_count": 0,
      "monitors_count": {
        "alert": 0,
        "ok": 8,
        "warning": 0
      },
      "name": "France DC01"
    },
    'headers': {}
  },
  'scope_get_404': {
    'path': 'scope/404',
    'json': {
      "message": "Scope show failed",
      "reasons": {
        "scope": [
          "Resource not found : 404"
        ]
      }
    },
    'status': 404,
    'headers': {}
  },
  'scope_create': {
    'path': 'scope/create',
    'json': {
      "description": "France datacenter - zone 01",
      "id": 1,
      "incidents_count": 0,
      "links": {
        "incidents": f"{PRODMANAGER_API_URL}/incident?scope=1",
        "maintenances": f"{PRODMANAGER_API_URL}/maintenance?scope=1",
        "monitors": f"{PRODMANAGER_API_URL}/monitor?scope=1",
        "self": f"{PRODMANAGER_API_URL}/scope/1"
      },
      "maintenances_count": 0,
      "monitors_count": {
        "alert": 0,
        "ok": 8,
        "warning": 0
      },
      "name": "France DC01"
    },
    'headers': {}
  },
  'scope_1_updated': {
    'path': 'scope/1/update',
    'json': {
      "description": "UPDATED - France datacenter - zone 01",
      "id": 1,
      "incidents_count": 0,
      "links": {
        "incidents": f"{PRODMANAGER_API_URL}/incident?scope=1",
        "maintenances": f"{PRODMANAGER_API_URL}/maintenance?scope=1",
        "monitors": f"{PRODMANAGER_API_URL}/monitor?scope=1",
        "self": f"{PRODMANAGER_API_URL}/scope/1"
      },
      "maintenances_count": 0,
      "monitors_count": {
        "alert": 0,
        "ok": 8,
        "warning": 0
      },
      "name": "France DC01"
    },
    'headers': {}
  },
  'scope_1_delete': {
    'path': 'scope/1/delete',
    'json': { },
    'headers': {}
  },
  'scope_list_page_1_per_page_5': {
    'path': 'scope?page=1&per_page=5',
    'json': {
      "items": [
        {
          "description": "France datacenter - zone 01",
          "id": 1,
          "incidents_count": 0,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?scope=1",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?scope=1",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?scope=1",
            "self": f"{PRODMANAGER_API_URL}/scope/1"
          },
          "maintenances_count": 0,
          "monitors_count": {
            "alert": 0,
            "ok": 8,
            "warning": 0
          },
          "name": "France DC01"
        }, {
          "description": "France datacenter - zone 02",
          "id": 2,
          "incidents_count": 1,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?scope=2",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?scope=2",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?scope=2",
            "self": f"{PRODMANAGER_API_URL}/scope/2"
          },
          "maintenances_count": 0,
          "monitors_count": {
            "alert": 0,
            "ok": 7,
            "warning": 1
          },
          "name": "France DC02"
        }, {
          "description": "France datacenter - zone 03",
          "id": 3,
          "incidents_count": 1,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?scope=3",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?scope=3",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?scope=3",
            "self": f"{PRODMANAGER_API_URL}/scope/3"
          },
          "maintenances_count": 1,
          "monitors_count": {
            "alert": 1,
            "ok": 7,
            "warning": 0
          },
          "name": "France DC03"
        }, {
          "description": "Japan datacenter - zone 01",
          "id": 7,
          "incidents_count": 0,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?scope=7",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?scope=7", 
            "monitors": f"{PRODMANAGER_API_URL}/monitor?scope=7",
            "self": f"{PRODMANAGER_API_URL}/scope/7"
          },
          "maintenances_count": 0,
          "monitors_count": {
            "alert": 0,
            "ok": 8,
            "warning": 0
          },
          "name": "Japan DC01"
        }, {
          "description": "Japan datacenter - zone 02",
          "id": 8,
          "incidents_count": 0,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?scope=8",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?scope=8",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?scope=8",
            "self": f"{PRODMANAGER_API_URL}/scope/8"
          },
          "maintenances_count": 1,
          "monitors_count": {
            "alert": 0,
            "ok": 7,
            "warning": 1
          },
          "name": "Japan DC02"
        }
      ]
    },
    'headers': {
      'x-total-pages': '2',
      'x-total': '8',
      'x-page': '1',
      'x-per-page': '5',
      'x-prev-page': 'None',
      'x-next-page': '2'
    }
  },
  'scope_list_page_2_per_page_5': {
    'path': 'scope?page=2&per_page=5',
    'json': {
      "items": [
        {
          "description": "Japan datacenter - zone 03",
          "id": 9,
          "incidents_count": 1,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?scope=9",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?scope=9",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?scope=9",
            "self": f"{PRODMANAGER_API_URL}/scope/9"
          },
          "maintenances_count": 1,
          "monitors_count": {
            "alert": 0,
            "ok": 7,
            "warning": 1
          },
          "name": "Japan DC03"
        }, {
          "description": "West-US datacenter - zone 01",
          "id": 4,
          "incidents_count": 1,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?scope=4",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?scope=4",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?scope=4",
            "self": f"{PRODMANAGER_API_URL}/scope/4"
          },
          "maintenances_count": 0,
          "monitors_count": {
            "alert": 0,
            "ok": 7,
            "warning": 1
          },
          "name": "West-US DC01"
        }, {
          "description": "West-US datacenter - zone 02",
          "id": 5,
          "incidents_count": 0,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?scope=5",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?scope=5",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?scope=5",
            "self": f"{PRODMANAGER_API_URL}/scope/5"
          },
          "maintenances_count": 0,
          "monitors_count": {
            "alert": 1,
            "ok": 7,
            "warning": 0
          },
          "name": "West-US DC02"
        }, {
          "description": "West-US datacenter - zone 03",
          "id": 6,
          "incidents_count": 0,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?scope=6",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?scope=6",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?scope=6",
            "self": f"{PRODMANAGER_API_URL}/scope/6"
          },
          "maintenances_count": 0,
          "monitors_count": {
            "alert": 0,
            "ok": 6,
            "warning": 2
          },
          "name": "West-US DC03"
        }
      ]
    },
    'headers': {
      'x-total-pages': '2',
      'x-total': '9',
      'x-page': '2',
      'x-per-page': '5',
      'x-prev-page': '1',
      'x-next-page': 'None'
    }
  }
}
