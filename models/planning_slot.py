# -*- coding: utf-8 -*-

from odoo import fields, models


class PlanningSlot(models.Model):
    _inherit = "planning.slot"

    installation_id = fields.Many2one(
        "acomi.installation",
        string="Anlæg",
        index=True,
        ondelete="set null",
    )
