<?php
/**
 * Bootstrap this theme
 *
 * @package techlabs
 */

namespace Bloomberg\TechLabs\NextJS;

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

use WP_Post;

defined( 'ABSPATH' ) || exit;

/**
 * Functionality for loading assets, managing theme settings
 */
final class Bootstrap {

	private static Bootstrap $instance;

	/**
	 * Bootstrap constructor.
	 */
	public function __construct() {
		new Assets();
		new CPT\Share();
		new CPT\Source();
		new Rest\TechLabsRoutes();
		new Options\DataOptions();
	}

	public static function get_instance() {
		self::$instance = ( self::$instance ?? new self() );
		return self::$instance;
	}
}
