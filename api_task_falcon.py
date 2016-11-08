#!/usr/bin/env python2.7

import falcon

import psutil
import datetime
import json

import cpuinfo


class PingResource:
    def on_get(self, req, resp):
        pass


class PSResource:

    def on_get(self, req, resp):

        username = req.get_param('user', required=True)

        user_procs_attrs = (
            proc.as_dict(
                attrs=[
                    'pid',
                    'terminal',
                    'cmdline',
                    'cpu_times'
                ]
            ) for proc in psutil.process_iter() if proc.as_dict(attrs=['username'])['username'] == username
        )

        user_procs_attrs_filled = [
            {
                'pid': p['pid'],
                'tty': p['terminal'],
                'cmd': p['cmdline'][0] if p['cmdline'] else None,
                'time': str( datetime.timedelta(
                    seconds=int(sum(p['cpu_times'][0:2]))
                )) if p['cpu_times'] else None,
            } for p in user_procs_attrs
        ]

        resp.body = json.dumps(user_procs_attrs_filled)


class CPUModelResource:

    def on_get(self, req, resp):
        resp.body = cpuinfo.get_cpu_info()['brand']


application = falcon.API()

application.add_route('/ping', PingResource())
application.add_route('/ps', PSResource())
application.add_route('/cpu/model', CPUModelResource())
