// Enviar dados para API 
const produto = document.getElementById('form-produto');

produto.addEventListener('submit', async (e) => {
    
    //e.preventDefault();

    nome_produto_inserido = document.getElementById('nome_produto').value;
    valor_inserido = document.getElementById('valor').value;
    unidade_inserido = document.getElementById('und').value;
    quantidade_inserido = document.getElementById('qtnd').value;

    const produto_inserido = {
        nome_produto: nome_produto_inserido,
        valor_produto: parseFloat(valor_inserido),
        unidade_produto: unidade_inserido,
        quantidade_produto: quantidade_inserido

    }

    await fetch('http://127.0.0.1:8000/salvar-produto',{
        method: 'POST',
        headers:{'Content-Type': 'application/json'},
        body: JSON.stringify(produto_inserido)
    })
    alert('Enviado!')

})

// enviar dados para api pedindo para apagar
const apagar_produto = document.getElementById('apagar-produto')
apagar_produto.addEventListener('submit', async (e) => {
    alert('apagar')
    apagarProduto = document.getElementById('apagar-item').value;

    const deleteProduct = {
        apagar_item: apagarProduto
    }

    await fetch('http://127.0.0.1:8000/apagar',{
        method: 'POST',
        headers:{'Content-Type': 'application/json'},
        body: JSON.stringify(deleteProduct)
    })
})

window.onload = atualizartabela;

// listar os produtos da tabela
async function atualizartabela() {
    const resposta = await fetch('http://127.0.0.1:8000/listar')
    const dados = await resposta.json()

    const corpo = document.getElementById('tabela-produtos')
    corpo.innerHTML = ''

    dados.forEach(item => {
        const linha = document.createElement('tr')
        linha.style.textAlign = 'center';
        const estiloCelula = 'style="background-color: #fff; font-size: 12px; padding: 5px 0;"';
        linha.innerHTML = `
            <td>${item.nome}</td>
            <td>R$ ${item.valor}</td>
            <td>${item.unidade}</td>
            <td>${item.quantidade}</td>
        `
        corpo.appendChild(linha)
    })
}

window.onload = atualizartabela;




