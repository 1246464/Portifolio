let transacoes = [];

function adicionarTransacao() {
  let descricao = document.getElementById("descricao").value;
  let valor = parseFloat(document.getElementById("valor").value);
  let data = document.getElementById("data").value;

  let transacao = { descricao: descricao, valor: valor, data: data };
  transacoes.push(transacao);

  console.log(transacoes);
}

document.querySelector("form").addEventListener("submit", function (event) {
  event.preventDefault();
  adicionarTransacao();
});

function adicionarTransacao() {
  let descricao = document.getElementById("descricao").value;
  let valor = parseFloat(document.getElementById("valor").value);
  let data = document.getElementById("data").value;

  let transacao = { descricao: descricao, valor: valor, data: data };
  transacoes.push(transacao);

  exibirTransacoes();
}

function exibirTransacoes() {
  let tabelaTransacoes = document.getElementById("tabela-transacoes");
  tabelaTransacoes.innerHTML = "";

  for (let transacao of transacoes) {
    let tr = document.createElement("tr");

    let tdDescricao = document.createElement("td");
    tdDescricao.textContent = transacao.descricao;
    tr.appendChild(tdDescricao);

    let tdValor = document.createElement("td");
    tdValor.textContent = transacao.valor.toFixed(2);
    tr.appendChild(tdValor);

    let tdData = document.createElement("td");
    tdData.textContent = transacao.data;
    tr.appendChild(tdData);

    tabelaTransacoes.appendChild(tr);
  }
}

function exibirSaldo() {
  let saldo = 0;

  for (let transacao of transacoes) {
    saldo += transacao.valor;
  }

  let saldoElement = document.getElementById("saldo");
  saldoElement.textContent = saldo.toFixed(2);
}

exibirSaldo();