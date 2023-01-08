<?php 

// var_dump($_POST);

if (isset($_POST['absen'])) {
    $data = array(
        'status' => "200",
        'message' => 'berhasil',
        'data'   => $_POST['data'],
        'type'   => $_POST['type'],
    );
    
}else{
    $data = array(
        'status' => "200",
        'message' => 'data dikirimkan kosong / tidak valid', 
        'data'   => var_dump($_GET),
    );
}

echo json_encode($data);
// echo "hello";

