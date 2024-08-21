```SQL
CREATE TABLE product (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    photo VARCHAR(255),
    category VARCHAR(100),
    price DECIMAL(10, 2) NOT NULL,
    description VARCHAR(255)
);
```

```SQL
CREATE TABLE Users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(20),
    password VARCHAR(255) NOT NULL
);
```

```sql
INSERT INTO product (id, name, photo, category, price, description) VALUES
(1, 'Caesar Salad', 'food_1.png', 'Salad', 150.00, 'A classic Caesar salad with romaine lettuce, croutons, and Parmesan cheese.'),
(2, 'Greek Salad', 'food_2.png', 'Salad', 180.00, 'Fresh Greek salad with cucumbers, tomatoes, olives, and feta cheese.'),
(3, 'Pasta Carbonara', 'food_3.png', 'Pasta', 250.00, 'Creamy pasta with pancetta, eggs, and Parmesan cheese.'),
(4, 'Spaghetti Bolognese', 'food_4.png', 'Pasta', 220.00, 'Classic spaghetti with a rich meat sauce.'),
(5, 'Chicken Alfredo', 'food_5.png', 'Pasta', 275.00, 'Pasta with a creamy Alfredo sauce and grilled chicken.'),
(6, 'Vegetable Noodles', 'food_6.png', 'Noodles', 200.00, 'Stir-fried noodles with mixed vegetables.'),
(7, 'Chicken Chow Mein', 'food_7.png', 'Noodles', 230.00, 'Noodles with chicken and a savory sauce.'),
(8, 'Beef Stroganoff Noodles', 'food_8.png', 'Noodles', 270.00, 'Noodles with beef and creamy Stroganoff sauce.'),
(9, 'Chocolate Cake', 'food_9.png', 'Cake', 300.00, 'Rich and moist chocolate cake with a creamy frosting.'),
(10, 'Carrot Cake', 'food_10.png', 'Cake', 280.00, 'Spiced carrot cake with cream cheese frosting.'),
(11, 'Cheesecake', 'food_11.png', 'Cake', 320.00, 'Classic cheesecake with a graham cracker crust.'),
(12, 'Paneer Tikka', 'food_12.png', 'Pure Veg', 220.00, 'Grilled paneer cubes marinated in spices.'),
(13, 'Vegetable Curry', 'food_13.png', 'Pure Veg', 240.00, 'Mixed vegetables cooked in a rich curry sauce.'),
(14, 'Dal Tadka', 'food_14.png', 'Pure Veg', 200.00, 'Lentils cooked with spices and herbs.'),
(15, 'Chicken Sandwich', 'food_15.png', 'Sandwich', 180.00, 'Sandwich with grilled chicken and fresh vegetables.'),
(16, 'Veg Club Sandwich', 'food_16.png', 'Sandwich', 200.00, 'Triple-layered sandwich with assorted vegetables and cheese.'),
(17, 'Grilled Cheese Sandwich', 'food_17.png', 'Sandwich', 160.00, 'Classic grilled cheese sandwich.'),
(18, 'Chicken Roll', 'food_18.png', 'Rolls', 190.00, 'Rolled tortilla with spiced chicken and vegetables.'),
(19, 'Paneer Roll', 'food_19.png', 'Rolls', 210.00, 'Rolled tortilla with spiced paneer and vegetables.'),
(20, 'Vegetable Spring Roll', 'food_20.png', 'Rolls', 170.00, 'Crispy rolls filled with mixed vegetables.'),
(21, 'Apple Pie', 'food_21.png', 'Deserts', 220.00, 'Warm apple pie with a flaky crust.'),
(22, 'Brownie', 'food_22.png', 'Deserts', 250.00, 'Fudgy chocolate brownie with nuts.'),
(23, 'Ice Cream Sundae', 'food_23.png', 'Deserts', 270.00, 'Vanilla ice cream with chocolate sauce and toppings.'),
(24, 'Caesar Salad', 'food_24.png', 'Salad', 150.00, 'A classic Caesar salad with romaine lettuce, croutons, and Parmesan cheese.'),
(25, 'Pasta Primavera', 'food_25.png', 'Pasta', 260.00, 'Pasta with a variety of fresh vegetables.'),
(26, 'Pad Thai Noodles', 'food_26.png', 'Noodles', 250.00, 'Thai-style stir-fried noodles with shrimp and peanuts.'),
(27, 'Red Velvet Cake', 'food_27.png', 'Cake', 330.00, 'Rich red velvet cake with cream cheese frosting.'),
(28, 'Mixed Vegetable Salad', 'food_28.png', 'Salad', 170.00, 'A salad with a variety of fresh vegetables.'),
(29, 'Pasta Pesto', 'food_29.png', 'Pasta', 240.00, 'Pasta with a basil pesto sauce.'),
(30, 'Beef and Broccoli Noodles', 'food_30.png', 'Noodles', 260.00, 'Noodles with beef and broccoli in a savory sauce.'),
(31, 'Fruit Tart', 'food_31.png', 'Deserts', 280.00, 'Tart filled with pastry cream and fresh fruit.'),
(32, 'Mango Mousse', 'food_32.png', 'Deserts', 290.00, 'Light and airy mango mousse with a hint of cream.');

```