document.addEventListener("DOMContentLoaded", function() {
	const reset_data_form = document.querySelector(".reset-data-form");
	const reset_spend_amt_button = reset_data_form?.querySelector(".reset-spend-amount-button") ?? null;
	const reset_port_value_button = reset_data_form?.querySelector(".reset-portfolio-value-button") ?? null;
	const reset_all_data_button = reset_data_form?.querySelector(".reset-data-button") ?? null;
	const data_table = document.querySelector("#data-table");
	let data_table_elem = null;

	if (!reset_data_form) {
		return;
	}

	reset_spend_amt_button.addEventListener("click", function(evt) {
		if ( confirm("Are you sure you want to reset your spend value?") ) {
			reset_data_form.submit();
		}
	});
	reset_port_value_button.addEventListener("click", function(evt) {
		if ( confirm("Are you sure you want to reset your portfolio value?") ) {
			reset_data_form.submit();
		}
	});
	reset_all_data_button.addEventListener("click", function(evt) {
		if ( confirm("Are you sure you want to reset all tech lab data?") ) {
			reset_data_form.submit();
		}
	});

	if (data_table) {
		data_table_elem = new DataTable('#data-table');	
	}
});