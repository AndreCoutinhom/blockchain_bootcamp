// Para desenvolver um Smart Contract nessa atividade, será utilizado o framework Foundry, que usa a linguagem Solidity.
// O Foundry tem base em algumas tecnologias principais:
// A primeira é o Forge, que serve para gerenciamento do projeto. Mais detalhes no link: https://book.getfoundry.sh/forge/
// A segunda é o Cast que interage diretamente com o contrato gerenciado pelo Forge. Mais detalhes no link: https://book.getfoundry.sh/cast/
// A terceira é o Anvil que serve como uma simulação própria blockchain. Mais detalhes no link: https://book.getfoundry.sh/anvil/
// A quarta é o Chisel que permite a escrita do código sem a inclusão do arquivo. Mais detalhes no link: https://book.getfoundry.sh/chisel/

// Foundry é um framework para o Linux. Há a necessidade de usar Git Bash ou WSL caso precise ser instalado no Windows.
// Para o Linux, o comando de instalação é `curl -L https://foundry.paradigm.xyz | bash`
// O projeto se inicia com o comando `forge init`. 
// Após se iniciar, o framework oferece templates de scripts e arquivos de teste.

// SPDX-License-Identifier: MIT

// Verifique as versões possíveis
pragma solidity ^0.8.24;

contract Flipper {
  bool value;

// O correto é `constructo r` o editor de código se recusa a escrever com um a palavra inteira.
  constructorr() {
   value = true;
  }

function getValue() returns(bool) {
  return value;
  }

// A função getValue pode ser declarada como external, internal, public ou private. A diferença entre cada uma está no nível de disponibilidade de recebimento do contrato e permissões de alteração do valor.

function flip() external {
  value = !value;
  }

// Na função acima o valor tem seus valores trocados ao serem declarados. Funciona de forma muito similar ao Javascript.

}

// Ao escrever um contrato, o compilador do Solidity/Ethereum lê e interpreta o contrato no formato JSON como valores em bytes.
