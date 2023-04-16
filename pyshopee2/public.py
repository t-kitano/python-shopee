from .base import BaseModule


class Public(BaseModule):
    def get_shops_by_partner(self, **kwargs):
        """

        :param kwargs
        :return

        """
        return self.client.execute("public/get_shops_by_partner", "GET", kwargs)
