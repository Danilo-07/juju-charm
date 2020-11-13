#!/usr/bin/env python3

import logging

from ops.charm import CharmBase
from ops.main import main

from src.app import App

logger = logging.getLogger(__name__)


class MyCharm(CharmBase):
    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.install, self.on_install)

    def on_install(self, event):
        logger.info("Congratulations, the charm was properly installed!")

    def on_start(self, event):
        # Handle the start event here.
        logger.info("hello")
        app = App()
        app.run()

if __name__ == "__main__":
    main(MyCharm)