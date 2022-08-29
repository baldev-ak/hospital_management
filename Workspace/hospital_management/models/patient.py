from odoo import fields,models,api
from datetime import date

class Patient(models.Model):
    _name = "hospital.patient"
    _description = "Patient"

    name = fields.Char(string = 'Name')
    gender = fields.Selection([('male','Male'),('female','Female')], string = "Gender")
    phone_number = fields.Char(string='Phone No.')
    email_address = fields.Char(string='Email')
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string = 'Age', compute = '_compute_age', store = True)
    blood_group = fields.Selection([('a+','A+'),('a-','A-'),('b+','B+'),('b-','B-')], string = "Blood Group")
    hospital_id = fields.Many2one(comodel_name="hospital.hospital", string='Hospital')
    branch_id = fields.Many2one(comodel_name="hospital.branch", inverse_name="doctor_ids", string='Branch')
    doctor_id = fields.Many2one(comodel_name="hospital.doctor", string='Responsible Dr.')

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            rec.age = 0
            if rec.date_of_birth:
                openingdate = rec.date_of_birth
                today = date.today()
                age = today.year - openingdate.year - ((today.month, today.day) < (openingdate.month, openingdate.day))
                rec.age = age