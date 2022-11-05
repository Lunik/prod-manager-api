from ..utils import *

API_RESPONSES = {
  'monitor_list_per_page_0': {
    'path': 'monitor?per_page=0',
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
  'monitor_list_page_1': {
    'path': 'monitor?page=1',
    'json': {
      "items": [
        {
          "description": "Status of Block Storage in France DC01",
          "external_link": None,
          "external_reference": None,
          "id": 4,
          "integration": None,
          "links": {
            "scope": f"{PRODMANAGER_API_URL}/scope/1",
            "self": f"{PRODMANAGER_API_URL}/monitor/4",
            "service": f"{PRODMANAGER_API_URL}/service/4"
          },
          "name": "[F][B] Service status",
          "scope": 1,
          "service": 4,
          "status": "ok"
        },
        {
          "description": "Status of Block Storage in France DC02",
          "external_link": None,
          "external_reference": None,
          "id": 12,
          "integration": None,
          "links": {
            "scope": f"{PRODMANAGER_API_URL}/scope/2",
            "self": f"{PRODMANAGER_API_URL}/monitor/12",
            "service": f"{PRODMANAGER_API_URL}/service/4"
          },
          "name": "[F][B] Service status",
          "scope": 2,
          "service": 4,
          "status": "alert"
        },
        {
          "description": "Status of Block Storage in France DC03",
          "external_link": None,
          "external_reference": None,
          "id": 20,
          "integration": None,
          "links": {
            "scope": f"{PRODMANAGER_API_URL}/scope/3",
            "self": f"{PRODMANAGER_API_URL}/monitor/20",
            "service": f"{PRODMANAGER_API_URL}/service/4"
          },
          "name": "[F][B] Service status",
          "scope": 3,
          "service": 4,
          "status": "ok"
        },
        {
          "description": "Status of Compute in France DC01",
          "external_link": None,
          "external_reference": None,
          "id": 2,
          "integration": None,
          "links": {
            "scope": f"{PRODMANAGER_API_URL}/scope/1",
            "self": f"{PRODMANAGER_API_URL}/monitor/2",
            "service": f"{PRODMANAGER_API_URL}/service/2"
          },
          "name": "[F][C] Service status",
          "scope": 1,
          "service": 2,
          "status": "ok"
        },
        {
          "description": "Status of Compute in France DC02",
          "external_link": None,
          "external_reference": None,
          "id": 10,
          "integration": None,
          "links": {
            "scope": f"{PRODMANAGER_API_URL}/scope/2",
            "self": f"{PRODMANAGER_API_URL}/monitor/10",
            "service": f"{PRODMANAGER_API_URL}/service/2"
          },
          "name": "[F][C] Service status",
          "scope": 2,
          "service": 2,
          "status": "ok"
        },
        {
          "description": "Status of Compute in France DC03",
          "external_link": None,
          "external_reference": None,
          "id": 18,
          "integration": None,
          "links": {
            "scope": f"{PRODMANAGER_API_URL}/scope/3",
            "self": f"{PRODMANAGER_API_URL}/monitor/18",
            "service": f"{PRODMANAGER_API_URL}/service/2"
          },
          "name": "[F][C] Service status",
          "scope": 3,
          "service": 2,
          "status": "ok"
        },
        {
          "description": "Status of Databases in France DC01",
          "external_link": None,
          "external_reference": None,
          "id": 1,
          "integration": None,
          "links": {
            "scope": f"{PRODMANAGER_API_URL}/scope/1",
            "self": f"{PRODMANAGER_API_URL}/monitor/1",
            "service": f"{PRODMANAGER_API_URL}/service/1"
          },
          "name": "[F][D] Service status",
          "scope": 1,
          "service": 1,
          "status": "ok"
        },
        {
          "description": "Status of Databases in France DC02",
          "external_link": None,
          "external_reference": None,
          "id": 9,
          "integration": None,
          "links": {
            "scope": f"{PRODMANAGER_API_URL}/scope/2",
            "self": f"{PRODMANAGER_API_URL}/monitor/9",
            "service": f"{PRODMANAGER_API_URL}/service/1"
          },
          "name": "[F][D] Service status",
          "scope": 2,
          "service": 1,
          "status": "ok"
        },
        {
          "description": "Status of Databases in France DC03",
          "external_link": None,
          "external_reference": None,
          "id": 17,
          "integration": None,
          "links": {
            "scope": f"{PRODMANAGER_API_URL}/scope/3",
            "self": f"{PRODMANAGER_API_URL}/monitor/17",
            "service": f"{PRODMANAGER_API_URL}/service/1"
          },
          "name": "[F][D] Service status",
          "scope": 3,
          "service": 1,
          "status": "ok"
        }
      ]
    },
    'headers': {
      'x-total-pages': '4',
      'x-total': '9',
      'x-page': '1',
      'x-per-page': '20',
      'x-prev-page': 'None',
      'x-next-page': 'None'
    }
  },
  'monitor_get_1': {
    'path': 'monitor/1',
    'json': {
      "description": "Status of Databases in France DC01",
      "external_link": None,
      "external_reference": None,
      "id": 1,
      "integration": None,
      "links": {
        "scope": f"{PRODMANAGER_API_URL}/scope/1",
        "self": f"{PRODMANAGER_API_URL}/monitor/1",
        "service": f"{PRODMANAGER_API_URL}/service/1"
      },
      "name": "[F][D] Service status",
      "scope": 1,
      "service": 1,
      "status": "ok"
    },
    'headers': {}
  },
  'monitor_get_404': {
    'path': 'monitor/404',
    'json': {
      "message": "Monitor show failed",
      "reasons": {
        "monitor": [
          "Resource not found : 404"
        ]
      }
    },
    'status': 404,
    'headers': {}
  },
  'monitor_create': {
    'path': 'monitor/create',
    'json': {
      "description": "Status of Databases in France DC01",
      "external_link": None,
      "external_reference": None,
      "id": 1,
      "integration": None,
      "links": {
        "scope": f"{PRODMANAGER_API_URL}/scope/1",
        "self": f"{PRODMANAGER_API_URL}/monitor/1",
        "service": f"{PRODMANAGER_API_URL}/service/1"
      },
      "name": "[F][D] Service status",
      "scope": 1,
      "service": 1,
      "status": "ok"
    },
    'headers': {}
  },
  'monitor_1_updated': {
    'path': 'monitor/1/update',
    'json': {
      "description": "UPDATED - Status of Databases in France DC01",
      "external_link": None,
      "external_reference": None,
      "id": 1,
      "integration": None,
      "links": {
        "scope": f"{PRODMANAGER_API_URL}/scope/1",
        "self": f"{PRODMANAGER_API_URL}/monitor/1",
        "service": f"{PRODMANAGER_API_URL}/service/1"
      },
      "name": "[F][D] Service status",
      "scope": 1,
      "service": 1,
      "status": "ok"
    },
    'headers': {}
  },
  'monitor_1_delete': {
    'path': 'monitor/1/delete',
    'json': { },
    'headers': {}
  },
  'monitor_list_page_1_per_page_5': {
    'path': 'monitor?page=1&per_page=5',
    'json': {
      "items": [
        {
          "description": "Status of Block Storage in France DC01",
          "external_link": None,
          "external_reference": None,
          "id": 4,
          "integration": None,
          "links": {
            "scope": f"{PRODMANAGER_API_URL}/scope/1",
            "self": f"{PRODMANAGER_API_URL}/monitor/4",
            "service": f"{PRODMANAGER_API_URL}/service/4"
          },
          "name": "[F][B] Service status",
          "scope": 1,
          "service": 4,
          "status": "ok"
        },
        {
          "description": "Status of Block Storage in France DC02",
          "external_link": None,
          "external_reference": None,
          "id": 12,
          "integration": None,
          "links": {
            "scope": f"{PRODMANAGER_API_URL}/scope/2",
            "self": f"{PRODMANAGER_API_URL}/monitor/12",
            "service": f"{PRODMANAGER_API_URL}/service/4"
          },
          "name": "[F][B] Service status",
          "scope": 2,
          "service": 4,
          "status": "alert"
        },
        {
          "description": "Status of Block Storage in France DC03",
          "external_link": None,
          "external_reference": None,
          "id": 20,
          "integration": None,
          "links": {
            "scope": f"{PRODMANAGER_API_URL}/scope/3",
            "self": f"{PRODMANAGER_API_URL}/monitor/20",
            "service": f"{PRODMANAGER_API_URL}/service/4"
          },
          "name": "[F][B] Service status",
          "scope": 3,
          "service": 4,
          "status": "ok"
        },
        {
          "description": "Status of Compute in France DC01",
          "external_link": None,
          "external_reference": None,
          "id": 2,
          "integration": None,
          "links": {
            "scope": f"{PRODMANAGER_API_URL}/scope/1",
            "self": f"{PRODMANAGER_API_URL}/monitor/2",
            "service": f"{PRODMANAGER_API_URL}/service/2"
          },
          "name": "[F][C] Service status",
          "scope": 1,
          "service": 2,
          "status": "ok"
        },
        {
          "description": "Status of Compute in France DC02",
          "external_link": None,
          "external_reference": None,
          "id": 10,
          "integration": None,
          "links": {
            "scope": f"{PRODMANAGER_API_URL}/scope/2",
            "self": f"{PRODMANAGER_API_URL}/monitor/10",
            "service": f"{PRODMANAGER_API_URL}/service/2"
          },
          "name": "[F][C] Service status",
          "scope": 2,
          "service": 2,
          "status": "ok"
        }
      ]
    },
    'headers': {
      'x-total-pages': '2',
      'x-total': '9',
      'x-page': '1',
      'x-per-page': '5',
      'x-prev-page': 'None',
      'x-next-page': '2'
    }
  },
  'monitor_list_page_2_per_page_5': {
    'path': 'monitor?page=2&per_page=5',
    'json': {
      "items": [
        {
          "description": "Status of Compute in France DC03",
          "external_link": None,
          "external_reference": None,
          "id": 18,
          "integration": None,
          "links": {
            "scope": f"{PRODMANAGER_API_URL}/scope/3",
            "self": f"{PRODMANAGER_API_URL}/monitor/18",
            "service": f"{PRODMANAGER_API_URL}/service/2"
          },
          "name": "[F][C] Service status",
          "scope": 3,
          "service": 2,
          "status": "ok"
        },
        {
          "description": "Status of Databases in France DC01",
          "external_link": None,
          "external_reference": None,
          "id": 1,
          "integration": None,
          "links": {
            "scope": f"{PRODMANAGER_API_URL}/scope/1",
            "self": f"{PRODMANAGER_API_URL}/monitor/1",
            "service": f"{PRODMANAGER_API_URL}/service/1"
          },
          "name": "[F][D] Service status",
          "scope": 1,
          "service": 1,
          "status": "ok"
        },
        {
          "description": "Status of Databases in France DC02",
          "external_link": None,
          "external_reference": None,
          "id": 9,
          "integration": None,
          "links": {
            "scope": f"{PRODMANAGER_API_URL}/scope/2",
            "self": f"{PRODMANAGER_API_URL}/monitor/9",
            "service": f"{PRODMANAGER_API_URL}/service/1"
          },
          "name": "[F][D] Service status",
          "scope": 2,
          "service": 1,
          "status": "ok"
        },
        {
          "description": "Status of Databases in France DC03",
          "external_link": None,
          "external_reference": None,
          "id": 17,
          "integration": None,
          "links": {
            "scope": f"{PRODMANAGER_API_URL}/scope/3",
            "self": f"{PRODMANAGER_API_URL}/monitor/17",
            "service": f"{PRODMANAGER_API_URL}/service/1"
          },
          "name": "[F][D] Service status",
          "scope": 3,
          "service": 1,
          "status": "ok"
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
