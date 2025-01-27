<?php

namespace Bloomberg\TechLabs\NextJS\CPT;

defined( 'ABSPATH' ) || exit;

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

/**
 * Configure share post type
 */
class Share {

	/**
	 * Class constructor
	 */
	public function __construct() {
		add_action( 'init', array( $this, 'register_post_type_share' ) );
		add_action( 'add_meta_boxes', array( $this, 'share_metaboxes' ) );
		add_action( 'save_post', array( $this, 'share_save_post' ), 10, 2 );
	}

	/**
	 * Post type for share
	 */
	public function register_post_type_share() {
		$labels = array(
			'name'                     => _x( 'Shares', 'post type general name', 'techlabs' ),
			'singular_name'            => _x( 'Share', 'post type singular name', 'techlabs' ),
			'add_new'                  => _x( 'Add New', 'share', 'techlabs' ),
			'add_new_item'             => __( 'Add New Share', 'techlabs' ),
			'edit_item'                => __( 'Edit Share', 'techlabs' ),
			'new_item'                 => __( 'New Share', 'techlabs' ),
			'view_item'                => __( 'View Share', 'techlabs' ),
			'view_items'               => __( 'View Shares', 'techlabs' ),
			'search_items'             => __( 'Search Shares', 'techlabs' ),
			'not_found'                => __( 'No shares found.', 'techlabs' ),
			'not_found_in_trash'       => __( 'No shares found in trash.', 'techlabs' ),
			'parent_item_colon'        => __( 'Parent Share:', 'techlabs' ),
			'all_items'                => __( 'All Shares', 'techlabs' ),
			'archives'                 => __( 'Shares Archive', 'techlabs' ),
			'attributes'               => __( 'Attributes', 'techlabs' ),
			'insert_into_item'         => __( 'Insert into share', 'techlabs' ),
			'uploaded_to_this_item'    => __( 'Uploaded to this share', 'techlabs' ),
			'featured_image'           => __( 'Featured image', 'techlabs' ),
			'set_featured_image'       => __( 'Set featured image', 'techlabs' ),
			'remove_featured_image'    => __( 'Remove featured image', 'techlabs' ),
			'use_featured_image'       => __( 'Use as featured image', 'techlabs' ),
			'menu_name'                => _x( 'Shares', 'admin menu', 'techlabs' ),
			'name_admin_bar'           => _x( 'Share', 'add new on admin bar', 'techlabs' ),
			'item_published'           => __( 'Share published', 'techlabs' ),
			'item_published_privately' => __( 'Share published privately', 'techlabs' ),
			'item_reverted_to_draft'   => __( 'Share is now a draft', 'techlabs' ),
			'item_scheduled'           => __( 'Share is scheduled to be published', 'techlabs' ),
			'item_updated'             => __( 'Share updated', 'techlabs' ),
		);
		$args   = array(
			'labels'          => $labels,
			'description'     => __( 'Available shares', 'techlabs' ),
			'public'          => true,
			'menu_icon'       => 'dashicons-chart-line',
			'supports'        => array( 'title', 'editor', 'excerpt', 'revisions', 'custom-fields' ),
			'show_in_rest'    => true,
			'show_in_menu' => true,
			'menu_position' => 20,
			'has_archive' => true,

		);

		register_post_type( 'share', $args );
	}

	/**
	 * Setup metabox for share post type.
	 */
	public function share_metaboxes() {
		add_meta_box(
			'postnamediv',
			esc_html__( 'Share Information' ),
			array( $this, 'share_metaboxes_html' ),
			'share',
			'side',
			'default'
		);
	}

	/**
	 * Metabox HTML for share post custom fields.
	 */
	public function share_metaboxes_html( $post ) {
		$custom = get_post_custom( $post->ID );
		$name = isset( $custom["name"][0] ) ? $custom["name"][0] : '';
		$symbol = isset( $custom["symbol"][0] ) ? $custom["symbol"][0] : '';
		$share_price = isset( $custom["share_price"][0] ) ? $custom["share_price"][0] : 0;
		$oneday_change = isset( $custom["1d_change"][0] ) ? $custom["1d_change"][0] : 0;
		$your_shares = isset( $custom["your_shares"][0] ) ? $custom["your_shares"][0] : 0;
		$avg_price = isset( $custom["avg_price"][0] ) ? $custom["avg_price"][0] : 0;
		$mkt_value = isset( $custom["mkt_value"][0] ) ? $custom["mkt_value"][0] : 0;
		$your_change = isset( $custom["your_change"][0] ) ? $custom["your_change"][0] : 0;
		?>
		<form method="post" action="post">
			<div class="form-input">
				<label><?php echo esc_html__( 'Name:' ); ?></label>
				<input type="text" name="name" value="<?php echo esc_attr( $name ); ?>" required>
			</div>
			<div class="form-input">
				<label><?php echo esc_html__( 'Symbol:' ); ?></label>
				<input type="text" name="symbol" value="<?php echo esc_attr( $symbol ); ?>" required>
			</div>
			<div class="form-input">
				<label><?php echo esc_html__( 'Share Price:' ); ?></label>
				<input type="number" name="share_price" value="<?php echo esc_attr( $share_price ); ?>" required>
			</div>
			<div class="form-input">
				<label><?php echo esc_html__( '1 Day Change:' ); ?></label>
				<input type="number" name="1d_change" value="<?php echo esc_attr( $oneday_change ); ?>" required>
			</div>
			<div class="form-input">
				<label><?php echo esc_html__( 'Your Shares:' ); ?></label>
				<input type="number" name="your_shares" value="<?php echo esc_attr( $your_shares ); ?>" required>
			</div>
			<div class="form-input">
				<label><?php echo esc_html__( 'Average Price:' ); ?></label>
				<input type="number" name="avg_price" value="<?php echo esc_attr( $avg_price ); ?>" required>
			</div>
			<div class="form-input">
				<label><?php echo esc_html__( 'Market Value:' ); ?></label>
				<input type="number" name="mkt_value" value="<?php echo esc_attr( $mkt_value ); ?>" required>
			</div>
			<div class="form-input">
				<label><?php echo esc_html__( 'Your Change:' ); ?></label>
				<input type="number" name="your_change" value="<?php echo esc_attr( $your_change ); ?>" required>
			</div>
		</form>
	<?php
	}

	/**
	 * Save share post meta information.
	 */
	public function share_save_post( $post_id, $post ) {
		update_post_meta( $post_id, 'name', $_POST['name'] );
		update_post_meta( $post_id, 'symbol', $_POST['symbol'] );
		update_post_meta( $post_id, 'share_price', $_POST['share_price'] );
		update_post_meta( $post_id, '1d_change', $_POST['1d_change'] );
		update_post_meta( $post_id, 'your_shares', $_POST['your_shares'] );
		update_post_meta( $post_id, 'avg_price', $_POST['avg_price'] );
		update_post_meta( $post_id, 'mkt_value', $_POST['mkt_value'] );
		update_post_meta( $post_id, 'your_change', $_POST['your_change'] );
	}
}
