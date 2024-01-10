<?php
$servidor = 'localhost';
$usuario = 'root';
$senha = '';
$banco = 'bot';
$conn  = mysqli_connect($servidor, $usuario, $senha, $banco);

if(!$conn ){
    // echo "Deu ruim";
} else{
    // echo "Conectado ao banco!";
}


?>