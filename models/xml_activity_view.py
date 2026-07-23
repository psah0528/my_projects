from odoo import fields, models


class XMLActivityView(models.Model):
    _name = "xml.activity.view"
    _description = "XML Activity View Project"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "name"

    name = fields.Char(
        string="Task Name",
        required=True,
        tracking=True,
    )

    employee = fields.Char(
        string="Employee",
        tracking=True,
    )

    department = fields.Selection(
        [
            ("hr", "HR"),
            ("it", "IT"),
            ("sales", "Sales"),
            ("accounts", "Accounts"),
        ],
        string="Department",
        tracking=True,
    )

    deadline = fields.Date(
        string="Deadline",
        tracking=True,
    )

    status = fields.Selection(
        [
            ("draft", "Draft"),
            ("progress", "In Progress"),
            ("done", "Done"),
        ],
        string="Status",
        default="draft",
        tracking=True,
    )

    notes = fields.Text(
        string="Notes",
    )