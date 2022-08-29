from odoo import fields,models,api
from datetime import date

class Doctor(models.Model):
    _name = "hospital.doctor"
    _description = "Doctor"

    name = fields.Char(string = 'Name')
    gender = fields.Selection([('male','Male'),('female','Female')], string = "Gender")
    phone_number = fields.Char(string='Phone No.')
    email_address = fields.Char(string='Email')
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string = 'Age', compute = '_compute_age', store = True)
    no_of_patients = fields.Integer(compute='_compute_count_patients', string='Total Patients')
    date_of_joining = fields.Date(string='Date of Joining')
    hospital_id = fields.Many2one(comodel_name="hospital.hospital", string='Hospital')
    branch_id = fields.Many2one(comodel_name="hospital.branch", inverse_name="doctor_ids", string='Branch')
    speciality_id = fields.Many2one(comodel_name="hospital.specialities", string='Specialities')
    degree_ids = fields.Many2many(comodel_name = "doctor.degree", string = "Degree")

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            rec.age = 0
            if rec.date_of_birth:
                openingdate = rec.date_of_birth
                today = date.today()
                age = today.year - openingdate.year - ((today.month, today.day) < (openingdate.month, openingdate.day))
                rec.age = age

    def action_patient(self):
        return {
        'type': 'ir.actions.act_window',
        'name':'Patients',
        'res_model':'hospital.patient',
        'domain':[('doctor_id','=',self.id)],
        'view_mode': 'tree,form',
        'target':'current'
        }

    def _compute_count_patients(self):
        for rec in self:
            patients = self.env['hospital.patient'].search_count([('doctor_id','=',rec.id)])
            rec.no_of_patients = patients
    
class Degree(models.Model):
    _name = "doctor.degree"
    _description = "Doctor Degrees"

    name = fields.Char(string = "Degree")