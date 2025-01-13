<?php

namespace Bloomberg\TechLabs\NextJS\Utils;

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

abstract class Helpers {

	public static function get_techlab_data() {
		$stored_cvs_data = get_option( 'techlabs_share_data', array() );

		return $stored_cvs_data;
	}

	public static function store_techlab_data() {
		$csv_data = self::get_csv_data();
		$stored_cvs_data = get_option( 'techlabs_share_data', array() );
		$stored_portfolio_value = get_option( 'techlabs_portfolio_value', 10000 );
		$stored_spend_value = get_option( 'techlabs_spend_value', 10000 );

		if ( empty( $stored_cvs_data ) ) {
			update_option( 'techlabs_share_data', $csv_data );
		}

		if ( empty( $stored_portfolio_value ) ) {
			update_option( 'techlabs_portfolio_value', 10000 );
		}

		if ( empty( $stored_spend_value ) ) {
			update_option( 'techlabs_spend_value', 10000 );
		}
	}

	public static function get_csv_data() {
		$the_file = get_template_directory_uri() . '/db/data.csv';
		$csv_data = array_map( 'str_getcsv', file( $the_file ) );
		array_walk(
			$csv_data,
			function( &$a ) use ( $csv_data ) {
				$a = array_combine( $csv_data[0], $a );
			}
		);
		array_shift( $csv_data );

		return $csv_data;
	}

	public static function get_share_symbol_list() {
		$the_data = self::get_csv_data();
		$the_list = array();

		if ( empty( $the_data ) ) {
			return array();
		}

		foreach ( $the_data as $data ) {
			$the_list[] = array(
				'shareSymbol' => $data['Symbol'],
				'shareName' => $data['Name'],
			);
		}

		return $the_list;
	}

	public static function get_buy_share_list() {
		$the_data = self::get_csv_data();
		$the_list = array();

		if ( empty( $the_data ) ) {
			return array();
		}

		foreach ( $the_data as $data ) {
			$the_list[] = array(
				'shareSymbol' => $data['Symbol'],
				'shareName' => $data['Name'],
			);
		}

		return $the_list;
	}

	public static function get_sell_share_list() {

		$the_data = self::get_csv_data();
		$the_list = array();

		if ( empty( $the_data ) ) {
			return array();
		}

		foreach ( $the_data as $data ) {
			$the_list[] = array(
				'shareSymbol' => $data['Symbol'],
				'shareCount' => $data['Last Sale'] ?? '',
			);
		}

		return $the_list;
	}

	public static function get_shares_list() {
		$the_list = array();
		$shares_posts = get_posts(
			array(
				'post_type' => 'share',
				'posts_per_page' => -1
			)
		);
		if ( ! empty( $shares_posts ) ) {
			foreach ( $shares_posts as $share ) {
				$share_name = get_post_meta( $share->ID, 'name', true ) ?? '';
				$share_symbol = get_post_meta( $share->ID, 'symbol', true ) ?? '';
				$share_price = get_post_meta( $share->ID, 'share_price', true ) ?? 0;
				$oneday_change = get_post_meta( $share->ID, '1d_change', true ) ?? 0;
				$your_shares = get_post_meta( $share->ID, 'your_shares', true ) ?? 0;
				$avg_price = get_post_meta( $share->ID, 'avg_price', true ) ?? 0;
				$mkt_value = get_post_meta( $share->ID, 'mkt_value', true ) ?? 0;
				$your_change = get_post_meta( $share->ID, 'your_change', true ) ?? 0;

				$the_list[] = array(
					'symbol' => $share_symbol,
					'name' => $share_name,
					'sharePrice' => floatval( $share_price ),
					'1dChange' => floatval( $oneday_change ),
					'yourShares' => floatval( $your_shares ),
					'avgPrice' => floatval( $avg_price ),
					'mktValue' => floatval( $mkt_value ),
					'yourChange' => floatval( $your_change ),
				);
			}
		}

		return $the_list;
	}
	public static function get_share_price_symbol_list() {

		$the_data = self::get_csv_data();
		$the_list = array();

		if ( empty( $the_data ) ) {
			return array();
		}

		foreach ( $the_data as $data ) {
			$the_list[] = array(
				'shareSymbol' => $data['Symbol'],
				'shareCount' => $data['Last Sale'] ?? '',
			);
		}

		return $the_list;
	}
	public static function get_percentage_change_list() {

		$the_data = self::get_csv_data();
		$the_list = array();

		if ( empty( $the_data ) ) {
			return array();
		}

		foreach ( $the_data as $data ) {
			$the_list[] = array(
				'shareSymbol' => $data['Symbol'],
				'shareCount' => $data['% Change'] ?? '',
			);
		}

		return $the_list;
	}

	public static function reset_portfolio_value_data() {
		delete_option( 'techlabs_portfolio_value' );
		update_option( 'techlabs_portfolio_value', 10000 );
	}

	public static function reset_spend_amount_data() {
		delete_option( 'techlabs_spend_value' );
		update_option( 'techlabs_spend_value', 10000 );
	}

	public static function reset_all_lab_data() {
		// Reset portfolio + spend values
		delete_option( 'techlabs_share_data' );
		delete_option( 'techlabs_portfolio_value' );
		delete_option( 'techlabs_spend_value' );

		$shares_posts = get_posts(
			array(
				'post_type' => 'share',
				'posts_per_page' => -1,
			)
		);
		$posts_count = 0;
		if ( ! empty( $shares_posts ) ) {
			foreach ( $shares_posts as $share ) {
				wp_delete_post( $share->ID, true );
				$posts_count++;
			}
		}
		$posts_count = sprintf( '%s shares deleted', $posts_count );

		self::store_techlab_data();

		printf( '<div class="notice notice-success is-dismissible"><h4>Data Reset Successfully!</h4><p>%s</p></div>', $posts_count );
	}
}
