
<?php
$cnx = new mysqli("localhost", "ghxlam", "123456", "Dunder_Mifflin");

if ($cnx->connect_error) {
    die("Connection failed: " . $cnx->connect_error);
}

$product_name = $_GET['id'];

$query = "SELECT * FROM Products WHERE product_name = $product_name";
$result = $cnx->query($query);

if ($result) {
    $selected_product = $result->fetch_assoc();

    // Query to find a similar product
    // Example: finding a product with the same category or brand
    $selected_product_category = $selected_product['category']; // Assuming $selected_product contains the selected product's details
$product_id = $selected_product['id'];

// Check if the selected product is from Quill or Staples
if (substr($product_id, 0, 1) === 'q') {
    // If selected product is from Quill, find similar Staples products
    $similar_category = 's';
} elseif (substr($product_id, 0, 1) === 's') {
    // If selected product is from Staples, find similar Quill products
    $similar_category = 'q';
} else {
    // Handle other cases or errors
    echo "Invalid product ID format";
    exit;
}

// Construct the query to select similar products
$similar_query = "SELECT * FROM Products 
                  WHERE category = '{$similar_category}' 
                  AND SUBSTRING(id, 2) = SUBSTRING('$product_id', 2)";
    $similar_result = $cnx->query($similar_query);

    // Compare products and highlight the cheaper one
    if ($similar_result) {
        while ($row = $similar_result->fetch_assoc()) {
            if ($row['product_price'] < $selected_product['product_price']) {
                echo '<p>' . $row['product_name'] . ' is cheaper than ' . $selected_product['product_name'] . '</p>';
            } else {
                echo '<p>' . $selected_product['product_name'] . ' is cheaper than ' . $row['product_name'] . '</p>';
            }
        }
    } else {
        echo "Error: " . $cnx->error;
    }
} else {
    echo "Error: " . $cnx->error;
}

// Close the connection
$cnx->close();

/**
 * THIS FILE HAS SOME ERRORS AND DOES NOT WORK FYI
 */
?>


echo '<p>' . 'Price: ' . $row['product_price'] . '</p>';
echo '<p>' . 'Star Rating: ' . $row['review_score'] . '</p>';
echo '<p>' . 'Description : ' . $row['product_description'] . '</p>';