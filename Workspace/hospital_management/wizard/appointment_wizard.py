from odoo import fields,models,api
from datetime import date

class Appointment(models.TransientModel):
    _name = "hospital.patient.appointment.wizard"
    _description = "Patient Appointments Wizard"
    _rec_name="patient_id"

    patient_id = fields.Many2one(comodel_name = "hospital.patient", string = "Name")
    doctor_id = fields.Many2one(comodel_name = "hospital.doctor",compute = "_compute_all", string = "Responsible Dr.")
    referred_to_id = fields.Many2one(comodel_name = "hospital.doctor", string = "Referred to Dr.")
    date = fields.Date(string = "Date")  
    gender = fields.Selection([('male','Male'),('female','Female')], string = "Gender",compute = "_compute_all")
    phone_number = fields.Char(string='Phone No.',compute = "_compute_all")
    age = fields.Integer(string = 'Age', store = True,compute = "_compute_all")
    blood_group = fields.Selection([('a+','A+'),('a-','A-'),('b+','B+'),('b-','B-')], string = "Blood Group",compute = "_compute_all")
    hospital_id = fields.Many2one(comodel_name="hospital.hospital", string='Hospital',compute = "_compute_all")
    branch_id = fields.Many2one(comodel_name="hospital.branch", inverse_name="doctor_ids", string='Branch',compute = "_compute_all")
  
    
    # @api.depends('patient_id')
    # def _compute_all(self):
    #     for rec in self:
    #         rec.doctor_id = ""
    #         rec.gender = ""
    #         rec.phone_number = 0
    #         rec.age = 0
    #         rec.blood_group = ""
    #         rec.hospital_id = ""
    #         rec.branch_id = ""
    #         if rec.patient_id:
    #             rec.doctor_id = rec.patient_id.doctor_id
    #             rec.gender = rec.patient_id.gender
    #             rec.phone_number = rec.patient_id.phone_number
    #             rec.age = rec.patient_id.age
    #             rec.blood_group = rec.patient_id.blood_group
    #             rec.hospital_id = rec.patient_id.hospital_id
    #             rec.branch_id = rec.patient_id.branch_id



    # def button_confirm(self):
    #     doc = self.env['hospital.doctor'].search([('id','in',self.doctor_id.ids)])
    #     # hospital = self.env['hospital.hospital'].search([('id','in',self.hospital_id.ids)])
    #     # branch = self.env['hospital.branch'].search([('id','in',self.branch_id.ids)])
    #     patient = self.env['hospital.patient'].search([('name','=',self.patient_id.name)])

    #     if self.patient_id and self.doctor_id:
    #         print("Found")
    #         self.env['hospital.patient.appointment'].create({
    #             'patient_id': patient.id,
    #             'doctor_id': doc.id,
    #             'date': date.today()
    #             })
