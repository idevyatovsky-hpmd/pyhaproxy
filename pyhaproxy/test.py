#!/usr/bin/env python
# -*- coding: utf-8 -*-

import parse


class TestParse(object):

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup(self):
        self.parser = parse.Parser('haproxy.cfg')
        self.configration = self.parser.build_configration()

    def teardown(self):
        pass

    def test_parse_global_section(self):
        print self.configration.globall.configs
        print '-' * 30
        print self.configration.globall.options

    def test_parse_frontend_section(self):
        for frontend in self.configration.frontends:
            print frontend.name, frontend.host, frontend.port
            print frontend.configs
            print frontend.options
            print '-' * 30


if __name__ == '__main__':
    main()