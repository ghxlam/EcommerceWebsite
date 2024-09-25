<html>
<head>
    <title>Dunder Mifflin</title>
    <style>
        .center {
            text-align: center; 
            margin-top: 50px;
        }
        .header {
            background-color: #333;
            color: #fff;
            padding: 10px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1 allign="center">Dunder Mifflin Office Supplies</h1>
    </div>
    <div class="center">
        <?= 'Welcome to Dunder Mifflin, we have an assortment of Office Supplies available for you!' ?>
    </div>
    <?php
        $cnx = new mysqli('localhost', 'ghxlam', '123456', 'Dunder_Mifflin');

        if ($cnx->connect_error)
            die('Connection failed: ' . $cnx->connect_error);
        
        $query = 'SELECT * FROM Products';
        $cursor = $cnx->query($query);
        while ($row = $cursor->fetch_assoc()) {
            echo '<a href="comparison.php?id=' . $row['product_name'] . '">';
            echo '<img src="' . $row["image_url"] . '" alt="Product Image">';
            echo '<p>' . $row['product_name'] . '</p>';
        }
        $cnx->close();
    ?>
    
    </body>
</html>