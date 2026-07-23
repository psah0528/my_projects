from odoo import fields, models


class XMLGraphView(models.Model):
    _name = "xml.graph.view"
    _description = "XML Graph View Project"
    _rec_name = "department"

    department = fields.Selection(
        [
            ("hr", "HR"),
            ("it", "IT"),
            ("sales", "Sales"),
            ("accounts", "Accounts"),
        ],
        string="Department",
        required=True,
    )

    salary = fields.Float(
        string="Salary",
    )

    employee_count = fields.Integer(
        string="Employees",
        default=1,
    )