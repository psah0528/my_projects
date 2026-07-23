from odoo import fields, models


class XMLPivotView(models.Model):
    _name = "xml.pivot.view"
    _description = "XML Pivot View Project"
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

    employee_count = fields.Integer(
        string="Employees",
        default=1,
    )