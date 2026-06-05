# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    installation_id = fields.Many2one(
        "acomi.installation",
        string="Anlæg",
        index=True,
        ondelete="set null",
    )
