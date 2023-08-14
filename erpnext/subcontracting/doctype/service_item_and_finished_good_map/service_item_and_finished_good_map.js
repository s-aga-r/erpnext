// Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Service Item and Finished Good Map", {
	setup: (frm) => {
		frm.trigger("set_queries");
	},

    set_queries: (frm) => {
        frm.set_query("service_item", () => {
            return {
                filters: {
                    disabled: 0,
                    is_stock_item: 0,
                }
            }
        });

        frm.set_query("finished_good_item", () => {
            return {
                filters: {
                    disabled: 0,
                    is_stock_item: 1,
                    default_bom: ['!=', ''],
                    is_sub_contracted_item: 1,
                }
            }
        });
    }
});
