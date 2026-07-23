from odoo import fields, models


class XMLSearchPanel(models.Model):
    _name = "xml.search.panel"
    _description = "XML Search Panel Project"
    _rec_name = "name"

    name = fields.Char(
        string="Employee",
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
        string="Active",
        default=True,
    )