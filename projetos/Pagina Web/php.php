// Aqui vamos buscar um usuário específico no banco de dados e retornar como JSON

$id = $_GET['id'];
$dsn = "mysql:host=localhost;dbname=meu_banco";
$user = "meu_usuario";
$pass = "minha_senha";
$dbh = new PDO($dsn, $user
