<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Page Title</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="main.css">
    <script src="main.js"></script>
</head>
<body>
    <?php
    $girls =array( 1 => 'yinka','bola','adesuwa','love');
    $alphalbet = array(a, z);
    echo '<select name="girls">';
    foreach($girls as $key=>$values){
        echo"<option value=\"$key\">$values</option>";
    }
    echo'</select>';
    echo'<select name="alphalbet">';
    foreach($alphalbet as $values){
        echo "<option values =\"$values\">$values</option>";
    }
    echo'</select>';
    ?>
</body>
</html>
