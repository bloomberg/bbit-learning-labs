<?php

namespace Bloomberg\TechLabs\NextJS\Rest;

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

defined( 'ABSPATH' ) || exit;

use Bloomberg\TechLabs\NextJS\Utils\Helpers;

use WP_Error;
use WP_REST_Request;
use WP_REST_Response;



class TechLabsRoutes {
	private $namespace = 'techlabs/v1';

	public function __construct() {
		add_action(
			'rest_api_init',
			function () {
				register_rest_route(
					$this->namespace,
					'/get_share_names',
					array(
						'methods'             => 'GET',
						'callback'            => array( $this, 'get_share_names_api' ),
						'permission_callback' => '__return_true',
					)
				);
				register_rest_route(
					$this->namespace,
					'/buy_share',
					array(
						'methods'             => 'POST',
						'callback'            => array( $this, 'buy_share_api' ),
						'permission_callback' => '__return_true',
					)
				);
				register_rest_route(
					$this->namespace,
					'/sell_share',
					array(
						'methods'             => 'POST',
						'callback'            => array( $this, 'sell_share_api' ),
						'permission_callback' => '__return_true',
					)
				);
				register_rest_route(
					$this->namespace,
					'/get_portfolio_value',
					array(
						'methods'             => 'GET',
						'callback'            => array( $this, 'get_portfolio_value_api' ),
						'permission_callback' => '__return_true',
					)
				);
				register_rest_route(
					$this->namespace,
					'/get_shares',
					array(
						'methods'             => 'GET',
						'callback'            => array( $this, 'get_shares_api' ),
						'permission_callback' => '__return_true',
					)
				);
				register_rest_route(
					$this->namespace,
					'/get_share_price/(?P<symbol>[a-zA-Z0-9-]+)',
					array(
						'methods'             => 'GET',
						'callback'            => array( $this, 'get_share_price_symbol_api' ),
						'permission_callback' => '__return_true',
					)
				);
				register_rest_route(
					$this->namespace,
					'/get_percentage_change/(?P<symbol>[a-zA-Z0-9-]+)',
					array(
						'methods'             => 'GET',
						'callback'            => array( $this, 'get_percentage_change_api' ),
						'permission_callback' => '__return_true',
					)
				);
				register_rest_route(
					$this->namespace,
					'/reset_data',
					array(
						'methods'             => 'POST',
						'callback'            => array( $this, 'reset_portfolio_data_api' ),
						'permission_callback' => '__return_true',
					)
				);
			}
		);
	}

	public function get_share_names_api( WP_REST_Request $request ) {

		$share_names = Helpers::get_share_symbol_list();

		return new WP_REST_Response(
			array(
				'records' => $share_names,
			)
		);
	}

	public function buy_share_api( WP_REST_Request $request ) {
		$tech_lab_data = Helpers::get_techlab_data();
		$request_params = $request->get_params();
		$req_share_symbol = $request_params['shareSymbol'] ?? null;
		$req_share_amount = $request_params['shareAmount'] ?? null;
		$req_share_count = $request_params['shareCount'] ?? null;
		$req_user_amount = $request_params['hardCodedUserAmount'] ?? null;
		$req_portfolio_value = $request_params['portfolioValue'] ?? null;

		$found_key = array_search( $req_share_symbol, array_column( $tech_lab_data, 'Symbol' ) );
		$techlabs_portfolio_value = get_option( 'techlabs_portfolio_value', 10000 );
		$techlabs_spend_value = get_option( 'techlabs_spend_value', 10000 );
		$found_share = $tech_lab_data[ $found_key ];

		if ( ! $found_key ) {
			return new WP_Error(
				'rest_stock_error',
				'This stock or share does not exist.',
				array(
					'status' => 400,
					'hardCodedUserAmount' => $req_user_amount,
					'portfolioValue' => $req_portfolio_value,
				)
			);
		}

		$new_amount = $techlabs_spend_value - $req_share_amount;
		$new_portfolio_value = $techlabs_portfolio_value + $req_share_amount;
		$tech_lab_data[ $found_key ] = $found_share;
		$new_share = array(
			'name' => $found_share['Name'],
			'symbol' => $req_share_symbol,
			'share_price' => floatval( str_replace( '$', '', $found_share['Last Sale'] ) ),
			'1d_change' => 0,
			'your_shares' => $req_share_count,
			'avg_price' => 0,
			'mkt_value' => $found_share['Market Cap'],
			'your_change' => 0,
			'timestamp' => date( 'F j, Y, g:i A' ),
		);

		$found_post = get_posts(
			array(
				'post_type' => 'share',
				's' => $req_share_symbol,
			)
		);

		if ( empty( $found_post ) ) {
			$post_arr = array(
				'post_type' => 'share',
				'post_title'   => $req_share_symbol,
				'post_content' => '',
				'post_status'  => 'publish',
				'post_author'  => get_current_user_id(),
			);
			$new_post_id = wp_insert_post( $post_arr );

			// Update custom fields post meta for share
			foreach ( $new_share as $key => $value ) {
				update_post_meta( $new_post_id, $key, $value );
			}

			$new_share_title = get_the_title( $new_post_id );
			$tech_lab_data[ $found_key ] = $found_share;

			// Update data with bought share
			update_option( 'techlabs_share_data', $tech_lab_data );
			update_option( 'techlabs_spend_value', $new_amount );
			update_option( 'techlabs_portfolio_value', $new_portfolio_value );

			return new WP_REST_Response(
				array(
					'success'     => true,
					'post_id' => $new_post_id,
					'message' => sprintf( 'Successfully bought %s shares of %s', $req_share_count, $new_share_title ),
					'newAmount'     => $new_amount,
					'newPortfolioValue' => $new_portfolio_value,
				)
			);
		} else {

			$found_post_item = $found_post[0];
			$current_shares = get_post_meta( $found_post_item->ID, 'your_shares', true );
			$current_shares = ! empty( $current_shares ) ? floatval( $current_shares ) + floatval( $req_share_count ) : 0;

			update_post_meta( $found_post_item->ID, 'your_shares', $current_shares );

			// Update data with bought share
			update_option( 'techlabs_share_data', $tech_lab_data );
			update_option( 'techlabs_spend_value', $new_amount );
			update_option( 'techlabs_portfolio_value', $new_portfolio_value );

			return new WP_REST_Response(
				array(
					'success'     => true,
					'message' => sprintf( 'Successfully bought %s more shares of %s', $req_share_count, $found_post_item->post_title ),
					'newAmount'     => $new_amount,
					'newPortfolioValue' => $new_portfolio_value,
				)
			);
		}

		return new WP_REST_Response(
			array(
				'newAmount'     => $new_amount,
				'newPortfolioValue' => $new_portfolio_value,
			)
		);
	}

	public function sell_share_api( WP_REST_Request $request ) {
		$tech_lab_data = Helpers::get_techlab_data();
		$request_params = $request->get_params();
		$request_params = $request->get_params();
		$req_share_symbol = $request_params['shareSymbol'] ?? null;
		$req_share_amount = $request_params['shareAmount'] ?? null;
		$req_share_count = $request_params['shareCount'] ?? null;
		$req_user_amount = $request_params['hardCodedUserAmount'] ?? null;
		$req_portfolio_value = $request_params['portfolioValue'] ?? null;
		$techlabs_portfolio_value = get_option( 'techlabs_portfolio_value', 10000 );
		$techlabs_spend_value = get_option( 'techlabs_spend_value', 10000 );

		$found_post = get_posts(
			array(
				'post_type' => 'share',
				's' => $req_share_symbol,
			)
		);
		$found_post_item = $found_post[0];
		$current_price = get_post_meta( $found_post_item->ID, 'share_price', true );
		$current_shares = get_post_meta( $found_post_item->ID, 'your_shares', true );
		$current_price = ! empty( $current_price ) ? floatval( $current_price ) - floatval( $req_share_amount ) : 0;
		$current_shares = ! empty( $current_shares ) ? floatval( $current_shares ) - floatval( $req_share_count ) : 0;
		update_post_meta( $found_post_item->ID, 'share_price', $current_price );
		update_post_meta( $found_post_item->ID, 'your_shares', $current_shares );

		if ( empty( $req_share_symbol ) || empty( $req_share_count ) ) {
			return new WP_Error(
				'rest_request_error',
				'Invalid request. Please use correct request for you query.',
				array( 'status' => 400 )
			);
		}

		$found_key = array_search( $req_share_symbol , array_column( $tech_lab_data, 'Symbol' ) );
		if ( ! $found_key ) {
			return new WP_Error(
				'rest_stock_error',
				'This stock or share does not exist.',
				array(
					'status' => 400,
					'hardCodedUserAmount' => $req_user_amount,
					'portfolioValue' => $req_portfolio_value,
				)
			);
		}

		$found_share = $tech_lab_data[ $found_key ];
		$tech_lab_data[ $found_key ] = $found_share;

		$new_portfolio_value = $techlabs_portfolio_value - $req_share_amount;
		$new_spend_value = $techlabs_spend_value + $req_share_amount;
		// Update data with bought share
		update_option( 'techlabs_share_data', $tech_lab_data );
		update_option( 'techlabs_spend_value', $new_spend_value );
		update_option( 'techlabs_portfolio_value', $new_portfolio_value );

		return new WP_REST_Response(
			array(
				'success'     => true,
				'message' => sprintf( 'Successfully sold %s shares of %s', $req_share_count, $found_post_item->post_title ),
				'newAmount'     => $new_spend_value,
				'newPortfolioValue' => $new_portfolio_value,
			)
		);
	}

	public function get_portfolio_value_api( WP_REST_Request $request ) {
		$techlabs_spend_value = get_option( 'techlabs_spend_value', 10000 );
		$techlabs_portfolio_value = get_option( 'techlabs_portfolio_value', 10000 );

		return new WP_REST_Response(
			array(
				'portfolio_value' => floatval( $techlabs_portfolio_value ),
				'spend_value' => floatval( $techlabs_spend_value ),
			)
		);
	}

	public function get_shares_api( WP_REST_Request $request ) {
		$shares_list = Helpers::get_shares_list();

		return new WP_REST_Response( $shares_list );
	}

	public function get_share_price_symbol_api( WP_REST_Request $request ) {
		$tech_lab_data = Helpers::get_csv_data();
		$symbol = $request->get_params()['symbol'] ?? '';
		$found_key = array_search( $symbol, array_column( $tech_lab_data, 'Symbol' ) );
		$share_price = '';
		$share_price = $tech_lab_data[ $found_key ]['Last Sale'] ?? '';

		return new WP_REST_Response(
			floatval( str_replace( '$', '', $share_price ) )
		);
	}

	public function get_percentage_change_api( WP_REST_Request $request ) {
		$tech_lab_data = Helpers::get_csv_data();
		$symbol = $request->get_params()['symbol'] ?? '';
		$found_key = array_search( $symbol, array_column( $tech_lab_data, 'Symbol' ) );

		$percentage_change = $tech_lab_data[ $found_key ]['% Change'] ?? '';

		return new WP_REST_Response(
			$percentage_change
		);
	}

	public function reset_portfolio_data_api( WP_REST_Request $request ) {
		// Reset tech lab data
		Helpers::reset_all_lab_data();

		return new WP_REST_Response(
			array(
				'success' => true,
				'message' => 'All portfolio data has been successfully reset.'
			)
		);
	}
}
