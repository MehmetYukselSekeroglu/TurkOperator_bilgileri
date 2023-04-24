<?php
header("Content-Type: application/json; utf-8;");
ini_set("display_errors", 0);
error_reporting(0);


if (isset($_GET)){
    $telno = htmlspecialchars($_GET["phone"]);

    if(!empty($telno)){
        if (strlen($telno) < 10 || strlen($telno) > 10 ){
            echo json_encode(["success" => "false", "message" => "numara olması gerekenden uzun veya kısa"]);
            die();
        }
        
        $TurkTelekom = ["501", "505", "506","507","552","553","554","555","559"];
        $TurkCell = ["530","531","532","533","534","535", "536", "537", "538", "539"];
        $Vodafone = ["541", "542", "543", "544", "545", "546", "547", "548", "549"];

        $abone_numarasi = substr($telno, 0, 3);
         
        if ( in_array($abone_numarasi, $TurkTelekom)){
            echo json_encode(["success" => "true", "operatör" => "TürkTelekom"]);
            die();
        }elseif( in_array($abone_numarasi, $TurkCell)){
            echo json_encode(["success" => "true", "operatör" => "Türkcell"]);
            die();
        }elseif ( in_array($abone_numarasi, $Vodafone) ) {
            echo json_encode(["success" => "true", "operatör" => "Vodafone"]);
            die();
        }elseif( $abone_numarasi == "551"){
            echo json_encode(["success" => "true", "operatör" => "BimCell Sanal operaötörü | TürkTelekom"]);
            die();
        }elseif( $abone_numarasi == "516"){
            echo json_encode(["success" => "true", "operatör" => "Bursa mobile | Turkcell"]);
            die();
        }elseif( $abone_numarasi == "561"){
            echo json_encode(["success" => "true", "operatör" => "61cell | Türkcell"]);
            die();
        }else{
            echo json_encode(["success" => "false", "message" => "bulunamadı"]);
            die();
        }

    }else{
        echo json_encode(["success" => "false", "message" => "telno not set"]);
        die();
    }

}


?>