from odoo import fields, models


class XMLCalendarView(models.Model):
    _name = "xml.calendar.view"
    _description = "XML Calendar View Project"
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

    meeting_date = fields.Date(
        string="Meeting Date",
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

    notes = fields.Text(
        string="Notes",
    )