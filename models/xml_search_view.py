from odoo import fields, models


class XMLSearchView(models.Model):
    _name = "xml.search.view"
    _description = "XML Search View Project"
    _rec_name = "name"

    name = fields.Char(
        string="Employee Name",
        required=True,
    )

    employee_code = fields.Char(
        string="Employee Code",
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
        default="draft",
        string="Status",
    )

    active = fields.Boolean(
        string="Active",
        default=True,
    )

    salary = fields.Float(
        string="Salary",
    )