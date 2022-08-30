from odoo import fields,models,api


class BranchWizard(models.TransientModel):
    _name = "branch.wizard"
    _description = "Branch Wizard"

    name = fields.Char(string = "name")

    def button_confirm(self):
        print("\n\n\n-----------Test-----------\n\n\n")