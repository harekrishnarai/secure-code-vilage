<?php
$allowed = ['home.php', 'about.php'];
$page = in_array($_GET['page'], $allowed) ? $_GET['page'] : 'home.php';
include($page);
?>
