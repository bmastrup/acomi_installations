# -*- coding: utf-8 -*-

from odoo import fields, models


class Installation(models.Model):
    _name = "acomi.installation"
    _description = "Installations"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char('Navn', required=True, tracking=True)
    description = fields.Text('Beskrivelse')
    active = fields.Boolean('Aktiv', default=True)
    date_installed = fields.Date('Installationsdato', tracking=True)
    installation_type_id = fields.Many2one('acomi.installation.type', string='Anlægstype', tracking=True)
    partner_id = fields.Many2one('res.partner', string='Ejer', tracking=True)
    attachment_count = fields.Integer(string='Dokumenter', compute='_compute_attachment_count')

    state = fields.Selection([
        ("proposal", "Tilbud"),
        ("accepted", "Accept"),
        ("planned", "Planlagt"),
        ("build", "Etableres"),
        ("delivered", "Afleveret"),
        ("service", "Serviceaftale"),
        ("inactive", "Inaktiv"),
    ], string="Status", default="proposal", tracking=True)

    def _compute_attachment_count(self):
        grouped_data = self.env['ir.attachment']._read_group(
            [('res_model', '=', self._name), ('res_id', 'in', self.ids)],
            ['res_id'],
            ['__count'],
        )
        counts = {res_id: count for res_id, count in grouped_data}
        for installation in self:
            installation.attachment_count = counts.get(installation.id, 0)

    def action_open_attachments(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Dokumenter',
            'res_model': 'ir.attachment',
            'view_mode': 'kanban,list,form',
            'domain': [('res_model', '=', self._name), ('res_id', '=', self.id)],
            'context': {
                'default_res_model': self._name,
                'default_res_id': self.id,
            },
        }
