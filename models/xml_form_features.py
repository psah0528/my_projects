from odoo import fields, models


class XMLFormFeatures(models.Model):
    _name = "xml.form.features"
    _description = "XML Form Features"
    _rec_name = "name"

    name = fields.Char(
        string="Employee Name",
        required=True,
    )

    department = fields.Selection(
        [
            ("hr", "HR"),
            ("it", "IT"),
            ("sales", "Sales"),
            ("accounts", "Accounts"),
        ],
        string="Department",
    )

    status = fields.Selection(
        [
            ("draft", "Draft"),
            ("progress", "In Progress"),
            ("done", "Done"),
        ],
        string="Status",
        default="draft",
    )

    salary = fields.Float(
        string="Salary",
    )

    active = fields.Boolean(
        default=True,
    )

    notes = fields.Text()


    def action_confirm(self):
     for rec in self:
        rec.status = "progress"


    def action_done(self):
     for rec in self:
        rec.status = "done"
