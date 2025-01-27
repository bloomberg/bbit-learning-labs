<?php
get_header();
?>
<main class="content">
	<?php 
	while ( have_posts() ) :
		the_post();
	endwhile;
	?>
</main>
<?php 
get_footer();
