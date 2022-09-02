from odoo import fields,models,api


class Appointment(models.Model):
    _name = "hospital.patient.appointment"
    _description = "Patient Appointments"
    _rec_name="patient_id"

    patient_id = fields.Many2one(comodel_name = "hospital.patient", string = "Name")
    doctor_id = fields.Many2one(comodel_name = "hospital.doctor", string = "Responsible Dr.")
    # referred_to_id = fields.Many2one(comodel_name = "hospital.doctor", string = "Referred to Dr.")
    date = fields.Date(string = "Date")    

    @api.model
    def create(self,vals):
        res = super(Appointment, self).create(vals)
        # print("\n\n---------",res)
        if vals.get('patient_id',False):
            self.env['hospital.patient'].create({
                'doctor_id': self.doctor_id,
            })

        return res