
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "hospital.patient"

    name = fields.Char(string='First Name')
    ref = fields.Char(string='Patient ID')
    lastname = fields.Char(string='Surname')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender')
    active = fields.Boolean(string="Active", default=True)


"""
specialty = fields.Selection([('pediatrician', 'Pediatrician'), ('neurologist', 'Neurologist'),
('family doctor', 'Family doctor'), ('cardiologist', 'Cardiologist'),
('dentist', 'Dentist')], string='Specialist')
"""