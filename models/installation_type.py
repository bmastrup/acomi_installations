# -*- coding: utf-8 -*-

from odoo import fields, models


class InstallationType(models.Model):
    _name = "acomi.installation.type"
    _description = "Anlægstype"

    name = fields.Char('Navn', required=True)
    description = fields.Text('Beskrivelse')
    active = fields.Boolean('Aktiv', default=True)
