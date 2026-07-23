from odoo import fields, models


class XMLWidgets(models.Model):
    _name = "xml.widgets"
    _description = "XML Widgets Project"
    _rec_name = "name"

    name = fields.Char(
        string="Employee Name",
        required=True,
    )

    photo = fields.Image(
        string="Photo",
    )

    email = fields.Char(
        string="Email",
    )

    phone = fields.Char(
        string="Phone",
    )

    website = fields.Char(
        string="Website",
    )

    salary = fields.Float(
        string="Salary",
    )

    progress = fields.Integer(
        string="Progress",
        default=0,
    )

    priority = fields.Selection(
        [
            ("0", "Low"),
            ("1", "Medium"),
            ("2", "High"),
            ("3", "Very High"),
        ],
        string="Priority",
        default="0",
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

    color = fields.Integer(
        string="Color",
    )

    tags = fields.Char(
        string="Tags",
    )