<?php
/**
 * Assets loaded for this theme
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

namespace Bloomberg\TechLabs\NextJS;

use WP_Post;

defined( 'ABSPATH' ) || exit;

/**
 * Functionality for loading assets, managing theme settings
 */
final class Assets {
	/**
	 * Assets constructor.
	 */
	public function __construct() {
		// Enqueue all stylesheets used in the theme.
		add_action( 'wp_enqueue_scripts', array( $this, 'enqueue_styles' ), 10, 0 );

		// BACK END (WP-ADMIN) SCRIPTS.
		add_action( 'admin_enqueue_scripts', array( $this, 'admin_enqueue_scripts' ), 10, 0 );
	}

	/**
	 * All front end stylesheets + scripts
	 */
	public function enqueue_styles() {
		wp_enqueue_style( 'main-css', get_template_directory_uri() . '/assets/css/main.css', array(), null );
		wp_enqueue_script( 'main-js', get_template_directory_uri() . '/assets/js/main.js', array(), null, false );
	}

	/**
	 * All back end stylesheets + scripts
	 */
	public function admin_enqueue_scripts() {
		wp_enqueue_style( 'admin-css', get_template_directory_uri() . '/assets/css/admin.css', array(), null );
		wp_enqueue_style( 'datatable-css', get_template_directory_uri()  . '/assets/css/dataTables.min.css', array(), null );
		wp_enqueue_script( 'admin-js', get_template_directory_uri() . '/assets/js/admin.js', array(), null, false );
		wp_enqueue_script( 'datatable-js', get_template_directory_uri()  . '/assets/js/dataTables.min.js', array(), null, false );
	}
}
