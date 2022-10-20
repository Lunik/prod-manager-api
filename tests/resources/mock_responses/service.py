from ..utils import *

API_RESPONSES = {
  'service_list_per_page_0': {
    'path': 'service?per_page=0',
    'json': {
      "items": []
    },
    'headers': {
      'x-total-pages': '0',
      'x-total': '8',
      'x-page': '1',
      'x-per-page': '0',
      'x-prev-page': 'None',
      'x-next-page': 'None'
    }
  },
  'service_list_page_1': {
    'path': 'service?page=1',
    'json': {
      "items": [
        {
          "description": "Block Storage IaaS services",
          "id": 4,
          "incidents_count": 1,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?service=4",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?service=4",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?service=4",
            "self": f"{PRODMANAGER_API_URL}/service/4"
          },
          "maintenances_count": 0,
          "monitors_count": {
            "alert": 2,
            "ok": 6,
            "warning": 1
          },
          "name": "Block Storage"
        },
        {
          "description": "Compute IaaS services",
          "id": 2,
          "incidents_count": 0,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?service=2",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?service=2",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?service=2",
            "self": f"{PRODMANAGER_API_URL}/service/2"
          },
          "maintenances_count": 0,
          "monitors_count": {
            "alert": 0,
            "ok": 8,
            "warning": 1
          },
          "name": "Compute"
        },
        {
          "description": "Databases PaaS services",
          "id": 1,
          "incidents_count": 1,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?service=1",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?service=1",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?service=1",
            "self": f"{PRODMANAGER_API_URL}/service/1"
          },
          "maintenances_count": 1,
          "monitors_count": {
            "alert": 0,
            "ok": 9,
            "warning": 0
          },
          "name": "Databases"
        },
        {
          "description": "Kubernetes PaaS services",
          "id": 5,
          "incidents_count": 0,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?service=5",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?service=5",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?service=5",
            "self": f"{PRODMANAGER_API_URL}/service/5"
          },
          "maintenances_count": 0,
          "monitors_count": {
            "alert": 0,
            "ok": 8,
            "warning": 1
          },
          "name": "Kubernetes"
        },
        {
          "description": "Load Balancer PaaS services",
          "id": 8,
          "incidents_count": 1,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?service=8",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?service=8",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?service=8",
            "self": f"{PRODMANAGER_API_URL}/service/8"
          },
          "maintenances_count": 1,
          "monitors_count": {
            "alert": 1,
            "ok": 8,
            "warning": 0
          },
          "name": "Load Balancer"
        },
        {
          "description": "Object Storage PaaS services",
          "id": 3,
          "incidents_count": 0,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?service=3",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?service=3",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?service=3",
            "self": f"{PRODMANAGER_API_URL}/service/3"
          },
          "maintenances_count": 0,
          "monitors_count": {
            "alert": 0,
            "ok": 6,
            "warning": 3
          },
          "name": "Object Storage"
        },
        {
          "description": "Serverless Container PaaS services",
          "id": 6,
          "incidents_count": 0,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?service=6",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?service=6",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?service=6",
            "self": f"{PRODMANAGER_API_URL}/service/6"
          },
          "maintenances_count": 0,
          "monitors_count": {
            "alert": 1,
            "ok": 8,
            "warning": 0
          },
          "name": "Serverless Container"
        },
        {
          "description": "Serverless Function PaaS services",
          "id": 7,
          "incidents_count": 1,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?service=7",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?service=7",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?service=7",
            "self": f"{PRODMANAGER_API_URL}/service/7"
          },
          "maintenances_count": 1,
          "monitors_count": {
            "alert": 1,
            "ok": 6,
            "warning": 2
          },
          "name": "Serverless Function"
        }
      ]
    },
    'headers': {
      'x-total-pages': '1',
      'x-total': '8',
      'x-page': '1',
      'x-per-page': '20',
      'x-prev-page': 'None',
      'x-next-page': 'None'
    }
  },
  'service_get_1': {
    'path': 'service/1',
    'json': {
      "description": "Databases PaaS services",
      "id": 1,
      "incidents_count": 1,
      "links": {
        "incidents": f"{PRODMANAGER_API_URL}/incident?service=1",
        "maintenances": f"{PRODMANAGER_API_URL}/maintenance?service=1",
        "monitors": f"{PRODMANAGER_API_URL}/monitor?service=1",
        "self": f"{PRODMANAGER_API_URL}/service/1"
      },
      "maintenances_count": 1,
      "monitors_count": {
        "alert": 0,
        "ok": 9,
        "warning": 0
      },
      "name": "Databases"
    },
    'headers': {}
  },
  'service_get_404': {
    'path': 'service/404',
    'json': {
      "message": "Service show failed",
      "reasons": {
        "service": [
          "Resource not found : 404"
        ]
      }
    },
    'status': 404,
    'headers': {}
  },
  'service_create': {
    'path': 'service/create',
    'json': {
      "description": "Databases PaaS services",
      "id": 1,
      "incidents_count": 1,
      "links": {
        "incidents": f"{PRODMANAGER_API_URL}/incident?service=1",
        "maintenances": f"{PRODMANAGER_API_URL}/maintenance?service=1",
        "monitors": f"{PRODMANAGER_API_URL}/monitor?service=1",
        "self": f"{PRODMANAGER_API_URL}/service/1"
      },
      "maintenances_count": 1,
      "monitors_count": {
        "alert": 0,
        "ok": 9,
        "warning": 0
      },
      "name": "Databases"
    },
    'headers': {}
  },
  'service_1_updated': {
    'path': 'service/1/update',
    'json': {
      "description": "UPDATED - Databases PaaS services",
      "id": 1,
      "incidents_count": 1,
      "links": {
        "incidents": f"{PRODMANAGER_API_URL}/incident?service=1",
        "maintenances": f"{PRODMANAGER_API_URL}/maintenance?service=1",
        "monitors": f"{PRODMANAGER_API_URL}/monitor?service=1",
        "self": f"{PRODMANAGER_API_URL}/service/1"
      },
      "maintenances_count": 1,
      "monitors_count": {
        "alert": 0,
        "ok": 9,
        "warning": 0
      },
      "name": "Databases"
    },
    'headers': {}
  },
  'service_1_delete': {
    'path': 'service/1/delete',
    'json': { },
    'headers': {}
  },
  'service_list_page_1_per_page_5': {
    'path': 'service?page=1&per_page=5',
    'json': {
      "items": [
        {
          "description": "Block Storage IaaS services",
          "id": 4,
          "incidents_count": 1,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?service=4",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?service=4",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?service=4",
            "self": f"{PRODMANAGER_API_URL}/service/4"
          },
          "maintenances_count": 0,
          "monitors_count": {
            "alert": 2,
            "ok": 6,
            "warning": 1
          },
          "name": "Block Storage"
        },
        {
          "description": "Compute IaaS services",
          "id": 2,
          "incidents_count": 0,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?service=2",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?service=2",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?service=2",
            "self": f"{PRODMANAGER_API_URL}/service/2"
          },
          "maintenances_count": 0,
          "monitors_count": {
            "alert": 0,
            "ok": 8,
            "warning": 1
          },
          "name": "Compute"
        },
        {
          "description": "Databases PaaS services",
          "id": 1,
          "incidents_count": 1,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?service=1",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?service=1",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?service=1",
            "self": f"{PRODMANAGER_API_URL}/service/1"
          },
          "maintenances_count": 1,
          "monitors_count": {
            "alert": 0,
            "ok": 9,
            "warning": 0
          },
          "name": "Databases"
        },
        {
          "description": "Kubernetes PaaS services",
          "id": 5,
          "incidents_count": 0,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?service=5",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?service=5",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?service=5",
            "self": f"{PRODMANAGER_API_URL}/service/5"
          },
          "maintenances_count": 0,
          "monitors_count": {
            "alert": 0,
            "ok": 8,
            "warning": 1
          },
          "name": "Kubernetes"
        },
        {
          "description": "Load Balancer PaaS services",
          "id": 8,
          "incidents_count": 1,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?service=8",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?service=8",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?service=8",
            "self": f"{PRODMANAGER_API_URL}/service/8"
          },
          "maintenances_count": 1,
          "monitors_count": {
            "alert": 1,
            "ok": 8,
            "warning": 0
          },
          "name": "Load Balancer"
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
  'service_list_page_2_per_page_5': {
    'path': 'service?page=2&per_page=5',
    'json': {
      "items": [
        {
          "description": "Object Storage PaaS services",
          "id": 3,
          "incidents_count": 0,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?service=3",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?service=3",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?service=3",
            "self": f"{PRODMANAGER_API_URL}/service/3"
          },
          "maintenances_count": 0,
          "monitors_count": {
            "alert": 0,
            "ok": 6,
            "warning": 3
          },
          "name": "Object Storage"
        },
        {
          "description": "Serverless Container PaaS services",
          "id": 6,
          "incidents_count": 0,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?service=6",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?service=6",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?service=6",
            "self": f"{PRODMANAGER_API_URL}/service/6"
          },
          "maintenances_count": 0,
          "monitors_count": {
            "alert": 1,
            "ok": 8,
            "warning": 0
          },
          "name": "Serverless Container"
        },
        {
          "description": "Serverless Function PaaS services",
          "id": 7,
          "incidents_count": 1,
          "links": {
            "incidents": f"{PRODMANAGER_API_URL}/incident?service=7",
            "maintenances": f"{PRODMANAGER_API_URL}/maintenance?service=7",
            "monitors": f"{PRODMANAGER_API_URL}/monitor?service=7",
            "self": f"{PRODMANAGER_API_URL}/service/7"
          },
          "maintenances_count": 1,
          "monitors_count": {
            "alert": 1,
            "ok": 6,
            "warning": 2
          },
          "name": "Serverless Function"
        }
      ]
    },
    'headers': {
      'x-total-pages': '2',
      'x-total': '8',
      'x-page': '2',
      'x-per-page': '5',
      'x-prev-page': '1',
      'x-next-page': 'None'
    }
  }
}
