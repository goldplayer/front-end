<?php 

    // require_once 'db_connect.php';

    if($_SERVER['REQUEST_METHOD'] === 'POST'){
        $action = $_POST['action'] ?? '';
    
        switch ($action){
            case 'login':
                login();
                break;
            default: 
                http_response_code(400);
                echo 'Error action';
                break;
            }

    }


    function login(){
      
            $data = [
              'username' => $_POST['name'] ?? NULL,
              'second-name' => $_POST['second-name'] ?? NULL,
              'email' => $_POST['email'] ?? NULL,
              'password' => $_POST['password'] ?? NULL 
            ];
           
            file_put_contents('/logs/login.txt', $data . date('Y-m-d H:i:s'));
    }



?>