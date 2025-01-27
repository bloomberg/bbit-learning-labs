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
 * Configure source post type
 */
class Source {

	/**
	 * Class constructor
	 */
	public function __construct() {
		add_action( 'init', array( $this, 'register_post_type_source' ) );
	}

	/**
	 * Post type for source
	 */
	public function register_post_type_source() {
		$labels = array(
			'name'                     => _x( 'Sources', 'post type general name', 'techlabs' ),
			'singular_name'            => _x( 'Source', 'post type singular name', 'techlabs' ),
			'add_new'                  => _x( 'Add New', 'Source', 'techlabs' ),
			'add_new_item'             => __( 'Add New Source', 'techlabs' ),
			'edit_item'                => __( 'Edit Source', 'techlabs' ),
			'new_item'                 => __( 'New Source', 'techlabs' ),
			'view_item'                => __( 'View Source', 'techlabs' ),
			'view_items'               => __( 'View Sources', 'techlabs' ),
			'search_items'             => __( 'Search Sources', 'techlabs' ),
			'not_found'                => __( 'No sources found.', 'techlabs' ),
			'not_found_in_trash'       => __( 'No sources found in trash.', 'techlabs' ),
			'parent_item_colon'        => __( 'Parent Source:', 'techlabs' ),
			'all_items'                => __( 'All Sources', 'techlabs' ),
			'archives'                 => __( 'Sources Archive', 'techlabs' ),
			'attributes'               => __( 'Attributes', 'techlabs' ),
			'insert_into_item'         => __( 'Insert into source', 'techlabs' ),
			'uploaded_to_this_item'    => __( 'Uploaded to this source', 'techlabs' ),
			'featured_image'           => __( 'Featured image', 'techlabs' ),
			'set_featured_image'       => __( 'Set featured image', 'techlabs' ),
			'remove_featured_image'    => __( 'Remove featured image', 'techlabs' ),
			'use_featured_image'       => __( 'Use as featured image', 'techlabs' ),
			'menu_name'                => _x( 'Sources', 'admin menu', 'techlabs' ),
			'name_admin_bar'           => _x( 'Source', 'add new on admin bar', 'techlabs' ),
			'item_published'           => __( 'Source published', 'techlabs' ),
			'item_published_privately' => __( 'Source published privately', 'techlabs' ),
			'item_reverted_to_draft'   => __( 'Source is now a draft', 'techlabs' ),
			'item_scheduled'           => __( 'Source is scheduled to be published', 'techlabs' ),
			'item_updated'             => __( 'Source updated', 'techlabs' ),
		);

		$args   = array(
			'labels'          => $labels,
			'description'     => __( 'Available Sources', 'techlabs' ),
			'public'          => true,
			'menu_icon'       => 'dashicons-database-add',
			'supports'        => array( 'title', 'editor', 'excerpt', 'revisions' ),
			'show_in_rest'    => true,
			'show_in_menu' => true,
			'menu_position' => 20,
			'has_archive' => true,

		);

		register_post_type( 'source', $args );
	}
}
