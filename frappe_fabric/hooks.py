app_name = "frappe_fabric"
app_title = "Frappe Fabric"
app_publisher = "Your Company"
app_description = "Fabric and Roll Management for ERPNext"
app_email = "info@yourcompany.com"
app_license = "MIT"
app_version = "1.0.0"

# Required Apps
required_apps = ["frappe", "erpnext"]

# Installation
after_install = "frappe_fabric.install.after_install"

# Fixtures
fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [["module", "=", "Frappe Fabric"]]
    },
    {
        "doctype": "Role",
        "filters": [["name", "in", ["Fabric Manager", "Fabric User", "Fabric Viewer"]]]
    }
]

# Document Events
doc_events = {
    "Fabric Roll": {
        "before_save": "frappe_fabric.fabric_management.doctype.fabric_roll.fabric_roll.before_save",
        "on_update": "frappe_fabric.fabric_management.doctype.fabric_roll.fabric_roll.on_update"
    },
    "Container Receipt": {
        "on_submit": "frappe_fabric.fabric_management.doctype.container_receipt.container_receipt.on_submit",
        "on_cancel": "frappe_fabric.fabric_management.doctype.container_receipt.container_receipt.on_cancel"
    },
    "Sample Cutting": {
        "on_submit": "frappe_fabric.fabric_management.doctype.sample_cutting.sample_cutting.on_submit",
        "on_cancel": "frappe_fabric.fabric_management.doctype.sample_cutting.sample_cutting.on_cancel"
    },
    "Retail Cutting Sale": {
        "on_submit": "frappe_fabric.fabric_management.doctype.retail_cutting_sale.retail_cutting_sale.on_submit",
        "on_cancel": "frappe_fabric.fabric_management.doctype.retail_cutting_sale.retail_cutting_sale.on_cancel"
    },
    "Roll Transfer": {
        "on_submit": "frappe_fabric.fabric_management.doctype.roll_transfer.roll_transfer.on_submit",
        "on_cancel": "frappe_fabric.fabric_management.doctype.roll_transfer.roll_transfer.on_cancel"
    }
}

# Scheduled Tasks
scheduler_events = {
    "daily": [
        "frappe_fabric.tasks.daily.check_low_stock_rolls",
        "frappe_fabric.tasks.daily.update_roll_aging"
    ],
    "weekly": [
        "frappe_fabric.tasks.weekly.generate_stock_report"
    ]
}

# Permissions
has_permission = {
    "Fabric Roll": "frappe_fabric.permissions.fabric_roll_permission"
}

# Desk Card
desk_card = {
    "doctype": "Fabric Roll",
    "label": "Fabric Rolls",
    "route": "/app/fabric-roll"
}
