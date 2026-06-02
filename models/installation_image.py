# -*- coding: utf-8 -*-

from odoo import fields, models


class InstallationImage(models.Model):
    _name = "acomi.installation.image"
    _description = "Anlægsbillede"
    _order = "date desc, id desc"

    name = fields.Char('Titel', required=True, default="Billede")
    installation_id = fields.Many2one(
        'acomi.installation',
        string='Anlæg',
        required=True,
        index=True,
        ondelete='cascade',
    )
    image_1920 = fields.Image('Billede', required=True, max_width=1920, max_height=1920)
    image_128 = fields.Image(
        'Miniature',
        related='image_1920',
        max_width=128,
        max_height=128,
        store=True,
    )
    date = fields.Date('Dato', default=fields.Date.context_today, required=True)
    image_type = fields.Selection([
        ('general', 'Generelt'),
        ('before', 'Før'),
        ('after', 'Efter'),
        ('nameplate', 'Typeskilt'),
        ('location', 'Placering'),
        ('issue', 'Fejl'),
    ], string='Type', default='general', required=True)
    note = fields.Text('Note')
