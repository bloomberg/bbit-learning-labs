<?php
/**
 * Bootstrap this theme
 *
 * @package techlabs
 */

/*
  Copyright 2024 Bloomberg Finance L.P.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
*/

namespace Bloomberg\TechLabs\NextJS\Options;

use Bloomberg\TechLabs\NextJS\Utils\Helpers;

defined( 'ABSPATH' ) || exit;

/**
 *
 */
class DataOptions {

	public function __construct() {
		add_action( 'admin_menu', array( $this, 'add_options_menu_page' ) );
		add_action( 'init', [ $this, 'handle_import_sources' ] );
		Helpers::store_techlab_data();
	}

	public function add_options_menu_page() {
		add_menu_page(
			__( 'Tech Labs Data Options', 'techlabs' ),
			'Tech Labs Data',
			'manage_options',
			'techlabs-api-options',
			array( $this, 'data_options_menu_page' ),
			'dashicons-admin-site-alt3',
			20
		);
	}

	public function handle_import_sources() {
		if ( isset( $_POST['techlabs_data_import'] )
			&& wp_verify_nonce( $_POST['techlabs_data_import'], 'techlabs_action' )
		) {
			$filename = $_FILES["data_source"]["tmp_name"];

			if ( $_FILES["data_source"]["size"] > 0 ) {
				$file = fopen($filename, "r");

				while ( ( $getData = fgetcsv( $file, 10000, "," ) ) !== FALSE ){
				}
			}
		}

		if ( isset( $_POST['techlabs_data_reset'] ) && isset( $_POST['reset-portfolio-value'] )
			&& wp_verify_nonce( $_POST['techlabs_data_reset'], 'techlabs_action' )
		) {
			Helpers::reset_portfolio_value_data();
		}

		if ( isset( $_POST['techlabs_data_reset'] ) && isset( $_POST['reset-spend-amount'] )
			&& wp_verify_nonce( $_POST['techlabs_data_reset'], 'techlabs_action' )
		) {
			Helpers::reset_spend_amount_data();
		}

		if ( isset( $_POST['techlabs_data_reset'] ) && isset( $_POST['reset-all-data'] )
			&& wp_verify_nonce( $_POST['techlabs_data_reset'], 'techlabs_action' )
		) {
			Helpers::reset_all_lab_data();
		}
	}

	/**
	* Display a custom menu page
	*/
	public function data_options_menu_page() { ?>
		<div class="wrap">
			<h1><?php esc_html_e( 'Import Source', 'techlabs' ); ?></h1>
			<div class="bbg-block-row">
				<div class="bbg-block-column bbg-block-column-half">
					<div class="poststuff">
						<form class="postbox acf-postbox" action="<?php echo admin_url( 'admin.php?page=techlabs-api-options' ); ?>" method="post" enctype="multipart/form-data">
							<h2 class="hndle ui-sortable-handle"><span><?php echo __( 'Tech Labs API', 'techlabs' ); ?></span></h2>
							<div class="inside acf-fields -top">
								<div class="acf-field">
									<div class="acf-label"><?php echo __( 'Select which data type you would like to export. Use the download button to export to a .json file which you can then import to another GA4 Datalayer Plugin installation.', 'bloomberg' ); ?></div>
									<div class="acf-input-wrap">
										<input type="file" name="data_source" accept="text/json" />
									</div>
								</div>
								<div class="acf-field">
									<input type="hidden" name="techlabs_action" value="import" />
									<?php wp_nonce_field( 'techlabs_action', 'techlabs_data_import' ); ?>
									<button type="submit" class="acf-button button button-large button-primary"><?php echo __( 'Import File', 'techlabs' ); ?></button>
								</div>
							</div>
						</form>
					</div>
				</div>
				<div class="bbg-block-column bbg-block-column-half">
					<div class="poststuff">
						<form class="postbox acf-postbox reset-data-form" action="<?php echo admin_url( 'admin.php?page=techlabs-api-options' ); ?>" method="post" enctype="multipart/form-data">
							<h2 class="hndle ui-sortable-handle"><span><?php echo __( 'Reset Tech Lab Data', 'techlabs' ); ?></span></h2>
							<div class="inside acf-fields -top">
								<div class="acf-field">
									<input type="hidden" name="techlabs_action" value="reset" />
									<?php wp_nonce_field( 'techlabs_action', 'techlabs_data_reset' ); ?>
									<button type="submit" class="acf-button button button-large button-danger reset-portfolio-value-button" name="reset-portfolio-value"><?php echo __( 'Reset Portfolio Value', 'techlabs' ); ?></button>
									<button type="submit" class="acf-button button button-large button-danger reset-spend-amount-button" name="reset-spend-amount"><?php echo __( 'Reset Spend Amount', 'techlabs' ); ?></button>
									<button type="submit" class="acf-button button button-large button-primary reset-data-button" name="reset-all-data"><?php echo __( 'Reset All Data', 'techlabs' ); ?></button>
								</div>
							</div>
						</form>
					</div>
				</div>
			</div>
			<div class="bbg-block-row">
				<?php
				$techlab_data = Helpers::get_techlab_data();
				?>
				<div class="postbox" style="padding: 15px;">
					<table id="data-table" class="display">
						<thead>
							<tr>
								<th>Symbol</th>
								<th>Name</th>
								<th>Last Sale</th>
								<th>Net Change</th>
								<th>% Change</th>
								<th>Market Cap</th>
								<th>Country</th>
								<th>IPO Year</th>
								<th>Volume</th>
								<th>Sector</th>
								<th>Industry</th>
							</tr>
						</thead>
						<tbody>
							<?php foreach ( $techlab_data as $data ) { ?>
								<tr>
									<td><?php echo $data['Symbol']; ?></td>
									<td><?php echo $data['Name']; ?></td>
									<td><?php echo $data['Last Sale']; ?></td>
									<td><?php echo $data['Net Change']; ?></td>
									<td><?php echo $data['% Change']; ?></td>
									<td><?php echo $data['Market Cap']; ?></td>
									<td><?php echo $data['Country']; ?></td>
									<td><?php echo $data['IPO Year']; ?></td>
									<td><?php echo $data['Volume']; ?></td>
									<td><?php echo $data['Sector']; ?></td>
									<td><?php echo $data['Industry']; ?></td>
								</tr>
							<?php } ?>
						</tbody>
					</table>
				</div>
			</div>
		</div>
	<?php
	}
}
