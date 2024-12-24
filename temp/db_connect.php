<?php

$db = 'd_photo';
$user_name = 'root';
$user_password = '';
$user_host = 'localhost';


try{
    $dsn = "mysql:host=$user_host; dbname=$db; charset=utf8mb4";
    $pdo = new PDO($dsn, $user_name, $user_password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    echo "<script>console.log('Успешное подключение к базе данных');</script>";
}catch(PDOException $e){
    $errorMessage = $e->getMessage();
    echo "<script>console.error('Ошибка: " . addslashes($errorMessage) . "');</script>";
}



