{
    "name": "My Projects",
    "version": "18.0.1.0.0",
    "summary": "Odoo Learning Projects",
    "author": "Puja",
    "category": "Learning",
    "license": "LGPL-3",
    "depends": [
        "base", "web",  "mail",
    ],


"data": [

    "security/ir.model.access.csv",
    "data/employee_sequence.xml",

    "views/orm_employee_views.xml",

    "views/xml_list_view_views.xml",
    "views/xml_form_view_views.xml",
    "views/xml_search_view_views.xml",
    "views/xml_kanban_view_views.xml",
    "views/xml_calendar_view_views.xml",
    "views/xml_activity_view_views.xml",
    "views/xml_graph_view_views.xml",
    "views/xml_pivot_view_views.xml",
    "views/xml_search_panel_views.xml",
    "views/xml_widgets_views.xml",
    "views/xml_form_features_views.xml",


    

    "views/department_views.xml",

    "views/skill_views.xml",

    "views/menu.xml",

],




    "application": True,
    "installable": True,
}