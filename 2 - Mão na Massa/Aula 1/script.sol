// SPDX-License-Identifier: MIT

// O script abaixo cria um contrato simples.

pragma solidity ^0.8.13;

contract Counter {
    uint8 number;
// Em solidity, "uint" é a declaração de um número inteiro.

// Permite definir manualmente o valor do contador.
    function setNumber(uint8 newNumber) public {
        number = newNumber;
    }

// Incrementa o valor do contador em uma unidade.
    function increment() public {
        number++;
    }

// Retorna o valor atual do contador.
    function getNumber() public view returns(uint8) {
        return number;
    }
}
