from odoo import fields, models


class XMLKanbanView(models.Model):
    _name = "xml.kanban.view"
    _description = "XML Kanban View Project"
    _rec_name = "name"

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

    status = fields.Selection(
        [
            ("draft", "Draft"),
            ("progress", "In Progress"),
            ("done", "Done"),
        ],
        string="Status",
        default="draft",
    )

    active = fields.Boolean(
        string="Active",
        default=True,
    )