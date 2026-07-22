from odoo import fields, models


class XMLListView(models.Model):
    _name = "xml.list.view"
    _description = "XML List View Project"
    _rec_name = "name"
    _order = "sequence"

    sequence = fields.Integer(
        string="Sequence",
        default=10,
    )

    name = fields.Char(
        string="Employee Name",
        required=True,
    )

    employee_code = fields.Char(
        string="Employee Code",
    )

    photo = fields.Image(
        string="Photo",
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

    salary = fields.Float(
        string="Salary",
    )

    progress = fields.Integer(
        string="Progress %",
    )

    active = fields.Boolean(
        string="Active",
        default=True,
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