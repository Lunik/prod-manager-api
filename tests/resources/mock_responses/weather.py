from ..utils import *

API_RESPONSES = {
  'wheather_get_monitor': {
    'path': 'weather/monitor',
    'json': {
      "alert": 5,
      "ok": 59,
      "warning": 8
    },
    'headers': {}
  },
  'wheather_get_incident': {
    'path': 'weather/incident',
    'json': {
      "active": 1,
      "investigating": 0,
      "resolved": 2,
      "stable": 1
    },
    'headers': {}
  },
  'wheather_get_maintenance': {
    'path': 'weather/maintenance',
    'json': {
      "canceled": 0,
      "failed": 0,
      "in-progress": 1,
      "scheduled": 1,
      "succeed": 1
    },
    'headers': {}
  }
}
