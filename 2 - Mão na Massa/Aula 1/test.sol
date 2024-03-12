// O script de teste abaixo confere o retorno correto ou incorreto do número inteiro declarado pelo comando uint.
// Tenha cuidado com operações matemáticas complexas. 
// O solidity na versão atual (mar. 2024), não é otimizado para trabalhar com redefinições de bits em uint de forma flexível.

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import {Test, console2} from "forge-std/Test.sol";
import {Counter} from "../src/Counter.sol";

contract CounterTest is Test {
    Counter public counter;

    function setUp() public {
        counter = new Counter();
        counter.setNumber(0);
    }

    function test_Increment() public {
        counter.increment();
        assertEq(counter.getNumber(), 1);
    }

// A função testFuzz faz com que o Foundry gere números aleatórios (x) para execução de testes.
// O programador pode declarar quantas vezes quer que o teste seja feito.

    function testFuzz_SetNumber(uint8 x) public {
        counter.setNumber(x);
        assertEq(counter.getNumber(), x);
    }
}
