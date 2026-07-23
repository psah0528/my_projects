from odoo import fields, models


class XMLFormView(models.Model):
    _name = "xml.form.view"
    _description = "XML Form View Project"
    _rec_name = "name"

    name = fields.Char(
        string="Employee Name",
        required=True,
    )

    employee_code = fields.Char(
        string="Employee Code",
    )

    email = fields.Char(
        string="Email",
    )

    phone = fields.Char(
        string="Phone",
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

    joining_date = fields.Date(
        string="Joining Date",
    )

    active = fields.Boolean(
        string="Active",
        default=True,
    )

    photo = fields.Image(
        string="Photo",
    )

    note = fields.Text(
        string="Notes",
    )