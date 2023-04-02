// Aqui vamos fazer uma requisição AJAX para buscar os dados de um usuário específico e exibir na tela
function buscarUsuario(id) {
	var xhr = new XMLHttpRequest();
	xhr.onreadystatechange = function() {
		if (xhr.readyState === 4 && xhr.status === 200) {
			var usuario = JSON.parse(xhr.responseText);
			document.getElementById('nome').textContent = usuario.nome;
			document.getElementById('email').textContent = usuario.email;
		}
	};
	xhr.open('GET', 'buscar_usuario.php?id=' + id, true);
	xhr.send();
}
